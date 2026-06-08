#! /usr/bin/env python3

import os
import re
import pdb

ODE_VSPACE = {}
ODE_VSPACE[1] = "\\newpage"
ODE_VSPACE[2] = "\\newpage"
ODE_VSPACE[3] = "\\psalmEndDecorateNewPage"
ODE_VSPACE[4] = "\\psalmEndDecorate{1.0}"
ODE_VSPACE[5] = "\\newpage"
ODE_VSPACE[6] = "\\psalmEndPictureNewPage"
ODE_VSPACE[7] = "\\psalmEndDecorate{1.0}"
ODE_VSPACE[8] = "\\psalmEndDecorateNewPage"
ODE_VSPACE[9] = "\\psalmEndDecorateNewPage"

REF_VSPACE = {}
REF_VSPACE[1] = ""
REF_VSPACE[2] = "\\vspace*{1\\baselineskip}\n"
REF_VSPACE[3] = "\\vspace*{1\\baselineskip}\n"
REF_VSPACE[4] = "\\vspace*{1\\baselineskip}\n"
REF_VSPACE[5] = "\\vspace*{1\\baselineskip}\n"
REF_VSPACE[6] = ""
REF_VSPACE[7] = ""
REF_VSPACE[8] = ""
REF_VSPACE[9] = "\\vspace*{1\\baselineskip}\n"

KEY_PRINTER_LINEBREAK = "$PRX"
KEY_PRINTER_NEWPAGE   = "$PRP"
TEX_LINEBREAK = "\\linebreak"
TEX_NEWPAGE   = "\\newpage"

path = os.path.dirname(os.path.realpath(__file__))
f = open(path + "/cantica-vetus.csv", "r")

current_ode = 0
line = f.readline()
while line:
  if '#' == line[0]:
    line = f.readline()
    continue

  s = line.split('^')
  ode = s[0]
  count = s[1]
  text = s[2].rstrip() # removes ending whitespace and '\n'

  is_count = s[1][0] != 'x'

  text = text.replace("¿", "¿~")
  text = text.replace("?", "~?")
  text = text.replace(";", "~;")
  text = text.replace("«", "«~")
  text = text.replace("»", "~»")
  text = text.replace(KEY_PRINTER_LINEBREAK, TEX_LINEBREAK)
  text = text.replace(KEY_PRINTER_NEWPAGE, TEX_NEWPAGE)

  if current_ode != ode:
    print("\\odeChapter{" + ode + "}\n")
    current_ode = ode

  if not is_count:
    print(text + "\n")
  else:
    if count == "10":
      print(REF_VSPACE[int(ode)])
      print("\\indentOn\n")
      count_arg = count
    else:
      count_arg = "\\phantom{0}" + count

    print("\\odeCount{" + count_arg + "}" + text + "\n")

    if count == "1":
      print("\\indentOff\n")
      print(ODE_VSPACE[int(ode)])


  line = f.readline()

f.close()
