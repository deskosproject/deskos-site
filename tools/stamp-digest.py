#!/usr/bin/env python3
"""Stamp the digest `:stable` serves into the home page.

The home page names the digest a reader can verify. Written by hand it would be
stale the day after a publication, so the workflow that regenerates the evidence
page runs this too: it asks the public registry which digest `:stable` serves and
replaces the value between the `data-stable-digest` markers.

Usage:
    python3 tools/stamp-digest.py           # update index.html
    python3 tools/stamp-digest.py --check    # exit 1 when it is stale
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGE = ROOT / "index.html"
STABLE_TAG_API = (
    "https://quay.io/api/v1/repository/deskos/deskos-core-centos-stream-10"
    "/tag/?specificTag=stable"
)
MARKER = re.compile(r'(<code class="mono" data-stable-digest>)[^<]*(</code>)')


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "DeskOS-evidence/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def stable_digest() -> str:
    """The digest `:stable` serves, read from the public registry API."""
    tags = json.loads(fetch(STABLE_TAG_API)).get("tags") or []
    if not tags:
        raise SystemExit("quay serves no :stable tag for the reference workstation")
    digest = tags[0].get("manifest_digest") or ""
    if not digest.startswith("sha256:"):
        raise SystemExit(f":stable returned {digest!r}, not a digest")
    return digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="exit 1 instead of writing when stale"
    )
    args = parser.parse_args()

    digest = stable_digest()
    page = PAGE.read_text()
    if len(MARKER.findall(page)) != 1:
        raise SystemExit(f"{PAGE.name} needs exactly one data-stable-digest marker")

    stamped = MARKER.sub(lambda m: f"{m.group(1)}{digest}{m.group(2)}", page)
    if stamped == page:
        print(f"the page already names {digest}")
        return 0
    if args.check:
        print(f"the page names another digest; :stable serves {digest}", file=sys.stderr)
        return 1
    PAGE.write_text(stamped)
    print(f"stamped {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
