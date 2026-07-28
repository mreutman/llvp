#! /usr/bin/env python3

import os
import re
import sys
import pdb

from pathlib import Path

KEY_PRINTER_LINEBREAK = "$PRX"
KEY_PRINTER_NEWPAGE   = "$PRP"
TEX_LINEBREAK = "\\linebreak"
TEX_NEWPAGE   = "\\newpage"

if len(sys.argv) < 2:
  print(f"Usage: ./{sys.argv[0]} <path_to_file>")
  sys.exit(1)

path = Path(sys.argv[1]).expanduser().resolve()
f = open(path, "r")

current_group = 0
line = f.readline()
while line:
  if '#' == line[0]:
    line = f.readline()
    continue

  s = line.split('^')
  group = s[0]
  count = s[1]
  ref   = s[2]
  text  = s[3].rstrip() # removes ending whitespace and '\n'

  is_count = s[1][0] != 'x'

  text = text.replace("¿", "¿~")
  text = text.replace("?", "~?")
  text = text.replace(":", "~:")
  text = text.replace(";", "~;")
  text = text.replace("«", "«~")
  text = text.replace("»", "~»")
  #text = text.replace("?~»", "?»")
  #text = text.replace("«~¿", "«¿")
  #text = text.replace("j", "į")
  #text = text.replace("J", "Į")
  #text = text.replace("w", "ų")
  #text = text.replace("W", "Ų")
  text = text.replace(KEY_PRINTER_LINEBREAK, TEX_LINEBREAK)
  text = text.replace(KEY_PRINTER_NEWPAGE, TEX_NEWPAGE)

  if not is_count:
    print("\\mysteryChapter{" + text + "}\n")
  
  else:
    phantom = ""
    if count != "10":
      phantom = "\\phantom{0}"

    print("\\mysteryCount{" + phantom + count + "}" + text + " " +
          "\\mysteryReference{" + ref + "}\n")

    if count == "10":
      print("\\mysteryEnd")

  line = f.readline()

f.close()
