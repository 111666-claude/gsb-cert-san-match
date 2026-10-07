"""命令行入口。"""

import argparse

from . import samples


def main(argv=None):
    ap = argparse.ArgumentParser(prog="sanmatch")
    ap.add_argument("--sample", choices=["wildcard", "plain", "cn", "case", "work"])
    args = ap.parse_args(argv)
    if args.sample:
        return samples.run(args.sample)
    ap.print_help()
    return 2


if __name__ == "__main__":
    unittest_main = None
    raise SystemExit(main())
