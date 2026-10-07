"""固定场景，用来复现题面里的锚点。"""

import json

from . import core


def _line(obj):
    print(json.dumps(obj, ensure_ascii=False))


def run(name):
    if name == "wildcard":
        cert = {"san": ["dns:*.example.com"]}
        _line({"match": core.match(cert, "x.y.example.com", core.Counter())})
        return 0
    if name == "plain":
        cert = {"san": ["example.com"]}
        _line({"match": core.match(cert, "example.com", core.Counter())})
        return 0
    if name == "cn":
        cert = {"san": ["dns:other.com"], "cn": "example.com"}
        _line({"match": core.match(cert, "example.com", core.Counter())})
        return 0
    if name == "case":
        cert = {"san": ["dns:Example.COM"]}
        _line({"match": core.match(cert, "example.com", core.Counter())})
        return 0
    if name == "work":
        cert = {"san": ["dns:n%04d.example.com" % i for i in range(800)]}
        counter = core.Counter()
        for i in range(800):
            core.match(cert, "n%04d.example.com" % i, counter)
        _line({"names": 800, "scanned": counter.scanned})
        return 0
    raise SystemExit("未知场景：" + name)
