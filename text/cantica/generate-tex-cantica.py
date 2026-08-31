#! /usr/bin/env python3

import os
import re
import sys
import pdb

VSPACE_PRE = {}
VSPACE_PRE[1] = r"\skipI"
VSPACE_PRE[2] = r"\skipII"
VSPACE_PRE[3] = r"\skipII"
VSPACE_PRE[4] = r"\skipI"
VSPACE_PRE[5] = r"\skipI"
VSPACE_PRE[6] = r"\skipI"
VSPACE_PRE[7] = r"\skipI"
VSPACE_PRE[8] = r"\skipI"
VSPACE_PRE[9] = r"\skipI"

VSPACE_POST = {}
VSPACE_POST[1] = r"\psalmEndDecorate{2.5}"
VSPACE_POST[2] = r"\psalmEndDecorateNewPage"
VSPACE_POST[3] = r"\psalmEndDecorateNewPage"
VSPACE_POST[4] = r"\psalmEndDecorate{3.0}"
VSPACE_POST[5] = r"\psalmEndDecorate{1.0}"
VSPACE_POST[6] = r"\psalmEndDecorateNewPage"
VSPACE_POST[7] = r"\indentOn\leftskip=3.75em\psalmEndDecorateNewPage"
VSPACE_POST[8] = r"\indentOff\leftskip=0em\psalmEndDecorate{0.69}"
VSPACE_POST[9] = r""
VSPACE_POST[10] = r"\skipII"
VSPACE_POST[11] = r"\skipIII"
VSPACE_POST[12] = r"\newpage"
VSPACE_POST[13] = r"\skipII"
VSPACE_POST[14] = r"\skipIII"
VSPACE_POST[15] = r"\skipII"
VSPACE_POST[16] = r"\skipIII"
VSPACE_POST[17] = r"\skipIII"
VSPACE_POST[18] = r"\skipIII"
VSPACE_POST[19] = r"\newpage"
VSPACE_POST[20] = r"\skipI"
VSPACE_POST[21] = r"\newpage"
VSPACE_POST[22] = r"\skipII"
VSPACE_POST[23] = r"\skipII"
VSPACE_POST[24] = r"\skipII"
VSPACE_POST[25] = r"\skipI"
VSPACE_POST[26] = r"\skipII"
VSPACE_POST[27] = r"\newpage"
VSPACE_POST[28] = r"\psalmEndDecorateNewPage"
VSPACE_POST[29] = r"\skipIII"
VSPACE_POST[30] = r"\skipII"
VSPACE_POST[31] = r"\newpage"
VSPACE_POST[32] = r"\skipIII"
VSPACE_POST[33] = r"\skipII"
VSPACE_POST[34] = r"\newpage"
VSPACE_POST[35] = r"\skipIII"
VSPACE_POST[36] = r"\skipII"
VSPACE_POST[37] = r"\newpage"
VSPACE_POST[38] = r""

start = None
end = None
prev = None

if len(sys.argv) == 2:
  start = sys.argv[1]
elif len(sys.argv) == 3:
  start = sys.argv[1]
  end = sys.argv[2]

KEY_PRINTER_LINEBREAK = "$PRX"
KEY_PRINTER_NEWPAGE   = "$PRP"
TEX_LINEBREAK = "\\linebreak"
TEX_NEWPAGE   = "\\newpage"

path = os.path.dirname(os.path.realpath(__file__))
f = open(path + "/cantica-vetus.csv", "r")

line = f.readline()
while line:
  if '#' == line[0]:
    line = f.readline()
    continue

  s = line.split('^')
  ode = s[0]
  text = s[2].rstrip() # removes ending whitespace and '\n'

  if ode == 'n':
    ode = str(int(prev) + 1)
  elif ode == 'c':
    ode = prev

  if start and int(ode) < int(start):
    line = f.readline()
    prev = ode
    continue

  if end and int(ode) > int(end):
    break

  if prev and int(prev) != int(ode):
    print(VSPACE_POST[int(prev)] + "\n")

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
    #if ode == "8":
    #  print(r"\leftskip=3.75em")

  # Exposition
  elif s[1][0] == 'x':
    #first_char = text[0]
    #rest_of_text = text[1:]
    #text = f"\\firstLetter{{{first_char}}}{rest_of_text}"
    print(text + "\n")

  # Line Number
  else:
    count = s[1]
    phantom = ""

    if count == "8":
      print(VSPACE_PRE[int(ode)] + "\n")

    print(r"\odeVerse{" + count + "}" + text + "\n")

  prev = ode
  line = f.readline()

f.close()
