#!/usr/bin/python
import sys, random

import jellyfish

import colors


def tag_line(entry, get_line=lambda x: x, similarity=.8):
  full_line = get_line(entry)
  full_line.rstrip('\n')
  for cluster in Cluster.clusters:
    if cached_jaro(get_line(cluster.key_entry), full_line) > similarity:
      return cluster.cluster_id
  else:
    new_cluster = Cluster(entry)
    return new_cluster.cluster_id


class Cluster:
  clusters = []

  def __init__(self, entry):
    self.count = 1
    self.cluster_id = len(Cluster.clusters)
    self.key_entry = entry
    Cluster.clusters.append(self)


def cached_jaro(key_line, other_line, mem={}):
  if not (key_line, other_line) in mem:
    mem[key_line, other_line] = jellyfish.jaro_distance(key_line, other_line)
  return mem[key_line, other_line]


if __name__ == '__main__':
  orig_readable_pairs, _ = colors.build_color_table()
  readable_pairs = []
  cluster_id_to_color_pair = {}
  while True:
    if not readable_pairs:
      readable_pairs = list(orig_readable_pairs)
      random.shuffle(readable_pairs)

    try:
      in_line = raw_input().decode('utf8')
      cluster_id = tag_line(in_line)
      if cluster_id not in cluster_id_to_color_pair:
        cluster_id_to_color_pair[cluster_id] = readable_pairs.pop()

      fg, bg = cluster_id_to_color_pair[cluster_id]
      bg_part = '' if bg is None else '\033[{}m'.format(bg)
      color_start = '\033[{}m{}'.format(fg, bg_part)
      color_end = '\033[0m'
      print '{}{}{}'.format(color_start, in_line, color_end)
    except EOFError:
      break
