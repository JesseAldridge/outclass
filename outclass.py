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


def make_new_color():
  brightness = 128 * 3
  vals = []
  for _ in range(3):
    val = random.randrange(min(brightness, 256))
    vals.append(val)
    brightness -= val
  random.shuffle(vals)
  return vals



if __name__ == '__main__':
  orig_readable_pairs, _ = colors.build_color_table()
  cluster_id_to_color = {}
  while True:

    try:
      in_line = raw_input().decode('utf8')
      cluster_id = tag_line(in_line)
      if cluster_id not in cluster_id_to_color:
        cluster_id_to_color[cluster_id] = make_new_color()

      r,g,b = cluster_id_to_color[cluster_id]
      print '\033[38;2;{};{};{}m{}\033[0m'.format(r,g,b, in_line)
    except EOFError:
      break
