# -*- coding: utf-8 -*-

# foreground, background pairs that are unreadable together
# (including when flux is running)
unreadable_pairs = {
  (35, None), (30, 100), (31, 101), (30, 104), (36, 106), (37, 107), (31, 41), (32, 42),
              (31, 100), (33, 101),            (92, 106), (93, 107), (35, 41), (36, 42),
              (32, 100), (35, 101), (90, 104), (96, 106), (97, 107), (36, 41), (31, 42),
              (33, 100), (37, 101),            (33, 106),            (32, 41), (33, 42),
              (35, 100), (91, 101), (94, 104), (91, 106),                      (35, 42),
              (36, 100), (95, 101), (98, 104), (95, 106),            (90, 41), (90, 42),
  (93, None), (90, 100), (92, 101),                                            (92, 42),
  (97, None), (94, 100), (96, 101),                                            (96, 42),
              (98, 100),

}

def build_color_table():
  readable_pairs = set()
  fg_vals = [30, 31, 32, 33, 35, 37, 90, 91, 92, 93, 95, 96, 97, 98]
  bg_vals = [None, 100, 101, 104, 106, 107, 41, 42]
  out_str = ''.join(['{:<7}'.format(val or '~') for val in [' '] + bg_vals]) + '\n'
  for fg in fg_vals:
    out_str += '{:<4}'.format(fg)
    for bg in bg_vals:
      bg_part = '' if bg is None else '\033[{}m'.format(bg)
      color_start = '\033[{}m{}'.format(fg, bg_part)
      color_end = '\033[0m'
      if (fg, bg) in unreadable_pairs:
        out_str += '   -   '
      else:
        readable_pairs.add((fg, bg))
        out_str += '{}  foo  {}'.format(color_start, color_end)
    out_str += '\n'
  return readable_pairs, out_str

if __name__ == '__main__':
  print build_color_table()[1]
