#!/usr/bin/env python3
"""Zenn の RSS を取得して _data/zenn.json を生成する。

標準ライブラリのみで動くので、依存パッケージのインストールは不要。
"""

import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

# ---- 設定 ------------------------------------------------------------
USERNAME = "naoyabone"          # Zenn のユーザー名
LIMIT = 5                        # トップに載せる件数
OUT_PATH = "_data/zenn.json"     # 出力先
# ---------------------------------------------------------------------

FEED_URL = f"https://zenn.dev/{USERNAME}/feed?include_scraps=false"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "bosakun-github-io/1.0 (+https://bosakun.github.io)"},
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        return res.read()


def parse(xml_bytes: bytes, limit: int) -> list:
    root = ET.fromstring(xml_bytes)
    items = []

    for item in root.findall("./channel/item")[:limit]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()

        if not title or not link:
            continue

        raw_date = (item.findtext("pubDate") or "").strip()
        try:
            date = parsedate_to_datetime(raw_date).strftime("%Y-%m-%d")
        except (TypeError, ValueError):
            date = ""

        items.append({"title": title, "link": link, "date": date})

    return items


def main() -> int:
    try:
        xml_bytes = fetch(FEED_URL)
    except Exception as e:
        print(f"[error] フィードを取得できませんでした: {e}", file=sys.stderr)
        return 1

    try:
        items = parse(xml_bytes, LIMIT)
    except ET.ParseError as e:
        print(f"[error] フィードを解析できませんでした: {e}", file=sys.stderr)
        return 1

    if not items:
        # 記事0件と一時的な取得失敗を区別できないため、既存ファイルは残す
        print("[warn] 記事が0件でした。既存の zenn.json を維持します。", file=sys.stderr)
        return 0

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"[ok] {len(items)} 件を {OUT_PATH} に書き出しました。")
    return 0


if __name__ == "__main__":
    sys.exit(main())

