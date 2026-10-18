#!/usr/bin/env python3
"""刷新 README 里的易变数字（零依赖）。

更新内容：
- 合并表格里的 star 快照（按仓库链接匹配）
- merged / repositories / lines 三个徽章
- "N merged PRs across M repositories" 这句话
- "Also opened" 区块的每仓库 open PR 数、合计，以及已归零的行

用法：
    GITHUB_TOKEN=$(gh auth token) python3 scripts/refresh_stats.py            # 写入
    GITHUB_TOKEN=$(gh auth token) python3 scripts/refresh_stats.py --check    # 只检查（CI 用）
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

README = Path(__file__).resolve().parents[1] / "README.md"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
USER = "skyzhao1223"
REPO_LINK = re.compile(r"github\.com/([\w.-]+/[\w.-]+)")


def api(path: str) -> dict:
    url = path if path.startswith("http") else f"https://api.github.com{path}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "content-hub-stats-refresh")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 429) and attempt < 2:
                time.sleep(20)
                continue
            raise
    return {}


def stars(slug: str) -> int:
    return int(api(f"/repos/{slug}").get("stargazers_count", 0))


def merged_count(slug: str) -> int:
    """搜索接口会漏最近的合并，用 REST 取两者较大值。"""
    q = urllib.parse.quote(f"repo:{slug} author:{USER} type:pr is:merged")
    search = int(api(f"/search/issues?q={q}&per_page=1").get("total_count", 0))
    rest = 0
    for page in (1, 2):
        pulls = api(f"/repos/{slug}/pulls?state=closed&per_page=100&sort=updated&direction=desc&page={page}")
        if not isinstance(pulls, list) or not pulls:
            break
        rest += sum(1 for p in pulls if p.get("user", {}).get("login") == USER and p.get("merged_at"))
        oldest = pulls[-1].get("updated_at", "")[:10]
        if oldest and oldest < "2026-08-01":
            break
    return max(search, rest)


def open_count(slug: str) -> int:
    q = urllib.parse.quote(f"repo:{slug} author:{USER} type:pr is:open")
    return int(api(f"/search/issues?q={q}&per_page=1").get("total_count", 0))


def fmt_stars(n: int) -> str:
    if n >= 10000:
        return f"{round(n / 1000)}k"
    if n >= 1000:
        return f"{n / 1000:.1f}".rstrip("0").rstrip(".") + "k"
    return str(n)


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    text = README.read_text(encoding="utf-8")
    original = text

    slugs: list[str] = []
    for slug in REPO_LINK.findall(text):
        if slug not in slugs and not slug.startswith(USER + "/"):
            slugs.append(slug)

    info = {s: {"stars": stars(s)} for s in slugs}
    time.sleep(1)
    for slug in slugs:
        info[slug]["merged"] = merged_count(slug)
        info[slug]["open"] = open_count(slug)
        time.sleep(2.5)

    # 1) 合并表格的 star 快照
    def fix_row(match: re.Match[str]) -> str:
        slug = match.group(2)
        return f"{match.group(1)}{fmt_stars(info[slug]['stars'])}★{match.group(3)}"

    text = re.sub(r"(\| \[`[^`]+`\]\(https://github\.com/([\w.-]+/[\w.-]+)\) \| )[\d.]+k?★( \|)", fix_row, text)

    # 2) 徽章与合计句
    total_merged = sum(info[s]["merged"] for s in slugs if info[s]["merged"] > 0)
    repo_count = sum(1 for s in slugs if info[s]["merged"] > 0)
    text = re.sub(r"merged%20PRs-\d+", f"merged%20PRs-{total_merged}", text)
    text = re.sub(r"repositories-\d+", f"repositories-{repo_count}", text)
    additions = sum(int(a) for a, _ in re.findall(r"\| \+(\d+)/\u2212(\d+) \|", text))
    deletions = sum(int(b) for _, b in re.findall(r"\| \+(\d+)/\u2212(\d+) \|", text))
    text = re.sub(r"lines-%2B[\d.]+k", f"lines-%2B{additions / 1000:.1f}k", text)
    text = re.sub(r"\*\*\d+ merged PRs across \d+ repositories\*\*", f"**{total_merged} merged PRs across {repo_count} repositories**", text)

    # 3) Also opened 区块：每仓库 open 数 + 合计 + 归零行
    block = re.search(r"<details>.*?</details>", text, re.S)
    if block:
        body = block.group(0)
        for slug in slugs:
            name = re.escape(slug.split("/")[1])
            body = re.sub(rf"(\| \[`{name}`\]\([^)]+\) \| [^|]+ \| )\d+( \|)", rf"\g<1>{info[slug]['open']}\g<2>", body)
        body = re.sub(r"(\| \[`[^`]+`\]\(https://github\.com/([\w.-]+/[\w.-]+)\) \| [^|]+ \| )0( \|)", "", body)
        open_total = sum(info[s]["open"] for s in slugs)
        body = re.sub(r"Also opened — \d+ PRs", f"Also opened — {open_total} PRs", body)
        text = text.replace(block.group(0), body)

    if text == original:
        print("已是最新，无需改动")
        return 0
    if check_only:
        print("README 需要更新（--check 模式不写入）")
        return 1
    README.write_text(text, encoding="utf-8")
    print(f"已刷新: merged={total_merged} repos={repo_count} open={sum(info[s]['open'] for s in slugs)} additions=+{additions}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
