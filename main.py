"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line (at most 180 characters) for an
ordinary office stapler, treated as an ancient ritual artifact, to
$MAKEFUN_OUTPUT_DIR/entry.txt. No trailing newline: the file holds
exactly the placard text.
"""

import os

ENTRY = (
    "Stapler, c. 1987. Iron and regret. Bound 14,203 memos; "
    "the last, unread, still in its jaw. Gift of the Accounts Department."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
