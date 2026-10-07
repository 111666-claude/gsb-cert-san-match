"""证书 SAN/CN 与主机名匹配。"""

import fnmatch


class Counter:
    """记录比较次数。"""

    def __init__(self):
        self.scanned = 0


def match(cert, host, counter):
    san = cert.get("san", [])
    for item in san:
        counter.scanned += 1
        if item.startswith("dns:"):
            pattern = item[4:]
            if fnmatch.fnmatchcase(host, pattern):
                return True
        elif item.startswith("ip:"):
            if item[3:] == host:
                return True
    if cert.get("cn"):
        counter.scanned += 1
        if cert["cn"] == host:
            return True
    return False
