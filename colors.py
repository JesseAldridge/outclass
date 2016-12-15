# -*- coding: utf-8 -*-

# foreground, background pairs that are unreadable together
# (including when flux is running)
unreadable_pairs = {
  (93, None),
  (97, None), (30, 100), (31, 101), (30, 104), (96, 106),            (31, 41),
              (31, 100), (33, 101), (34, 104), (92, 106), (93, 107), (35, 41), (36, 42),
              (33, 100), (35, 101), (90, 104),                       (36, 41),
              (34, 100), (37, 101),
              (35, 100), (91, 101), (94, 104),
              (36, 100), (95, 101),
              (90, 100),
              (94, 100),


}

def build_color_table():
  readable_pairs = set()
  fg_vals = range(30, 32) + range(33, 38) + range(90, 96) + [97, 98]
  bg_vals = [None, 100, 101, 104, 106, 107, 41, 42]
  out_str = ''.join(['{:<5}'.format(val or '~') for val in [' '] + bg_vals]) + '\n'
  for fg in fg_vals:
    out_str += '{:<4}'.format(fg)
    for bg in bg_vals:
      bg_part = '' if bg is None else '\033[{}m'.format(bg)
      color_start = '\033[{}m{}'.format(fg, bg_part)
      color_end = '\033[0m'
      if (fg, bg) in unreadable_pairs:
        out_str += '  -  '
      else:
        readable_pairs.add((fg, bg))
        out_str += '{}  x  {}'.format(color_start, color_end)
    out_str += '\n'
  return readable_pairs, out_str

if __name__ == '__main__':
  print build_color_table()[1]
