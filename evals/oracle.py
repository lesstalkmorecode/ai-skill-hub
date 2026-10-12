"""Runner-owned checks: container for agent code, trusted fixtures in offline tests."""

import runpy
import sys

from cases import CASES


def main():
    module = runpy.run_path(sys.argv[1])
    for items, expected in CASES:
        actual = module["total"](items)
        if actual != expected:
            print(f"FAIL: {items!r}: expected {expected}, received {actual!r}")
            return 1
    print(f"PASS: {len(CASES)} independent total() cases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
