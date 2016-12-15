import unittest

import cluster_lines


class ClusterTest(unittest.TestCase):
  def test_tag_line(self):
    assert cluster_lines.tag_line(u'foo') == 0
    assert cluster_lines.tag_line(u'foot') == 0
    assert cluster_lines.tag_line(u'bar') == 1

if __name__ == '__main__':
  unittest.main()
