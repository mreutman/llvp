#! /usr/bin/env python3

import os
import re
import pdb

VSPACE_PRE = {}
VSPACE_PRE[1] = r"\skipII"
VSPACE_PRE[2] = r"\skipI"
VSPACE_PRE[3] = r"\skipI"
VSPACE_PRE[4] = r"\skipII"
VSPACE_PRE[5] = r""
VSPACE_PRE[6] = r""
VSPACE_PRE[7] = r"\skipI"
VSPACE_PRE[8] = r"\skipI"
VSPACE_PRE[9] = r"\newpage"

VSPACE_POST = {}
VSPACE_POST[1] = r"\skipII"
VSPACE_POST[2] = r"\skipII"
VSPACE_POST[3] = r"\skipII"
VSPACE_POST[4] = r"\newpage"
VSPACE_POST[5] = r"\skipI"
VSPACE_POST[6] = r"\skipI"
VSPACE_POST[7] = r"\indentOn\skipI"
VSPACE_POST[8] = r"\indentOff\skipII"
VSPACE_POST[9] = r"\skipI"


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
  text = s[2].rstrip() # removes ending whitespace and '\n'

  is_count = s[1][0] != 'x'

  text = text.replace("¿", "¿~")
  text = text.replace("?", "~?")
  text = text.replace(";", "~;")
  text = text.replace("«", "«~")
  text = text.replace("»", "~»")
  text = text.replace(KEY_PRINTER_LINEBREAK, TEX_LINEBREAK)
  text = text.replace(KEY_PRINTER_NEWPAGE, TEX_NEWPAGE)

  # Title
  if s[1][0] == 't':
    text = text.replace("Ċ", "C")
    text = text.replace("Ġ", "G")
    text = text.replace("W", "V")
    text = text.replace("Á", "A")
    text = text.replace("Ó", "O")
    text = text.replace("É", "E")
    text = text.replace("Ú", "U")
    text = text.replace("Í", "I")
    text = text.replace("Ý", "Y")
    text = text.replace("À", "A")
    text = text.replace("Ò", "O")
    text = text.replace("È", "E")
    text = text.replace("Ù", "U")
    text = text.replace("Ì", "I")
    text = text.replace("Ỳ", "Y")
    text = text.replace("Â", "A")
    text = text.replace("Ô", "O")
    text = text.replace("Ê", "E")
    text = text.replace("Û", "U")
    text = text.replace("Î", "I")
    text = text.replace("Ŷ", "Y")

    text = text.replace("ċ", "c")
    text = text.replace("ġ", "g")
    text = text.replace("w", "v")
    text = text.replace("á", "a")
    text = text.replace("ó", "o")
    text = text.replace("é", "e")
    text = text.replace("ú", "u")
    text = text.replace("í", "i")
    text = text.replace("ý", "y")
    text = text.replace("à", "a")
    text = text.replace("ò", "o")
    text = text.replace("è", "e")
    text = text.replace("ù", "u")
    text = text.replace("ì", "i")
    text = text.replace("ỳ", "y")
    text = text.replace("â", "a")
    text = text.replace("ô", "o")
    text = text.replace("ê", "e")
    text = text.replace("û", "u")
    text = text.replace("î", "i")
    text = text.replace("ŷ", "y")

    print("\\odeChapter{" + ode + "}{" + text + "}\n")

    # HACK
    if ode == "8":
      print(r"\leftskip=3.75em")

  # Exposition
  elif s[1][0] == 'x':
    print(text + "\n")

  # Line Number
  else:
    count = s[1]
    phantom = ""

    if count == "10":
      print(VSPACE_PRE[int(ode)])

    elif count != "10":
      phantom = r"\phantom{0}"

    print(r"\odeVerse{" + phantom + count + "}" + text + "\n")

    if count == "1":
      print("\n")

      print(VSPACE_POST[int(ode)])

  # if current_ode != ode:
    # print("\\odeChapter{" + ode + "}\n")
    # current_ode = ode

  # if not is_count:
    # print(text + "\n")
  # else:
    # if count == "10":
      # print(REF_VSPACE[int(ode)])
      # print("\\indentOn\n")
      # count_arg = count
    # else:
      # count_arg = "\\phantom{0}" + count

    # print("\\odeCount{" + count_arg + "}" + text + "\n")

    # if count == "1":
      # print("\\indentOff\n")
      # print(ODE_VSPACE[int(ode)])


  line = f.readline()

f.close()
