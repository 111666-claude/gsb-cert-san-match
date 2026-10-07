import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sanmatch import core


class SanMatchTest(unittest.TestCase):
    def test_exact_dns(self):
        cert = {"san": ["dns:example.com"]}
        self.assertTrue(core.match(cert, "example.com", core.Counter()))

    def test_missing(self):
        cert = {"san": ["dns:example.com"]}
        self.assertFalse(core.match(cert, "other.com", core.Counter()))

    def test_ip_literal(self):
        cert = {"san": ["ip:10.0.0.1"]}
        self.assertTrue(core.match(cert, "10.0.0.1", core.Counter()))

    def test_cn_only(self):
        cert = {"cn": "example.com"}
        self.assertTrue(core.match(cert, "example.com", core.Counter()))

    def test_empty_cert(self):
        self.assertFalse(core.match({}, "example.com", core.Counter()))

    def test_counter_counts(self):
        counter = core.Counter()
        core.match({"san": ["dns:example.com"]}, "example.com", counter)
        self.assertGreater(counter.scanned, 0)


if __name__ == "__main__":
    unittest.main()
