#! /usr/bin/env python3

import os
import re
import pdb

CHAPTER_VSPACE = {}
CHAPTER_VSPACE[1] = "\\psalmEndII"
CHAPTER_VSPACE[2] = "\\psalmEndNewPage"
CHAPTER_VSPACE[3] = "\\psalmEndII"
CHAPTER_VSPACE[4] = "\\psalmEndII"
CHAPTER_VSPACE[5] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[6] = "\\psalmEndNewPage"
CHAPTER_VSPACE[7] = "\\psalmEndII"
CHAPTER_VSPACE[8] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[9] = "\\psalmEndI"
CHAPTER_VSPACE[10] = "\\psalmEndII"
CHAPTER_VSPACE[11] = "\\psalmEndII"
CHAPTER_VSPACE[12] = "\\psalmEndNewPage"
CHAPTER_VSPACE[13] = "\\psalmEndI"
CHAPTER_VSPACE[14] = "\\psalmEndII"
CHAPTER_VSPACE[15] = "\\psalmEndII"
CHAPTER_VSPACE[16] = "\\psalmEndNewPage"
CHAPTER_VSPACE[17] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[18] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[19] = "\\psalmEndI"
CHAPTER_VSPACE[20] = "\\psalmEndI"
CHAPTER_VSPACE[21] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[22] = "\\psalmEndII"
CHAPTER_VSPACE[23] = "\\psalmEndI"
CHAPTER_VSPACE[24] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[25] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[26] = "\\psalmEndNewPage"
CHAPTER_VSPACE[27] = "\\psalmEndII"
CHAPTER_VSPACE[28] = "\\psalmEndNewPage"
CHAPTER_VSPACE[29] = "\\psalmEndII"
CHAPTER_VSPACE[30] = "\\psalmEndI"
CHAPTER_VSPACE[31] = "\\psalmEndI"
CHAPTER_VSPACE[32] = "\\psalmEndNewPage"
CHAPTER_VSPACE[33] = "\\psalmEndI"
CHAPTER_VSPACE[34] = "\\psalmEndNewPage"
CHAPTER_VSPACE[35] = "\\psalmEndII"
CHAPTER_VSPACE[36] = "\\psalmEndNewPage"
CHAPTER_VSPACE[37] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[38] = "\\psalmEndI"
CHAPTER_VSPACE[39] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[40] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[41] = "\\psalmEndNewPage"
CHAPTER_VSPACE[42] = "\\psalmEndI"
CHAPTER_VSPACE[43] = "\\psalmEndI"
CHAPTER_VSPACE[44] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[45] = "\\psalmEndI"
CHAPTER_VSPACE[46] = "\\psalmEndNewPage"
CHAPTER_VSPACE[47] = "\\psalmEndI"
CHAPTER_VSPACE[48] = "\\psalmEndII"
CHAPTER_VSPACE[49] = "\\psalmEndI"
CHAPTER_VSPACE[50] = "\\psalmEndNewPage"
CHAPTER_VSPACE[51] = "\\psalmEndNewPage" # START HERE
CHAPTER_VSPACE[52] = "\\psalmEndI"
CHAPTER_VSPACE[53] = "\\psalmEndI"
CHAPTER_VSPACE[54] = "\\psalmEndI"
CHAPTER_VSPACE[55] = "\\psalmEndI"
CHAPTER_VSPACE[56] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[57] = "\\psalmEndDecorate{1}"
CHAPTER_VSPACE[58] = "\\psalmEndII"
CHAPTER_VSPACE[59] = "\\psalmEndNewPage"
CHAPTER_VSPACE[60] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[61] = "\\psalmEndNewPage"
CHAPTER_VSPACE[62] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[63] = "\\psalmEndNewPage"
CHAPTER_VSPACE[64] = "\\psalmEndI"
CHAPTER_VSPACE[65] = "\\psalmEndI"
CHAPTER_VSPACE[66] = "\\psalmEndI"
CHAPTER_VSPACE[67] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[68] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[69] = "\\psalmEndII"
CHAPTER_VSPACE[70] = "\\psalmEndDecorate{3.0}"
CHAPTER_VSPACE[71] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[72] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[73] = "\\psalmEndI"
CHAPTER_VSPACE[74] = "\\psalmEndI"
CHAPTER_VSPACE[75] = "\\psalmEndI"
CHAPTER_VSPACE[76] = "\\psalmEndNewPage"
CHAPTER_VSPACE[77] = "\\psalmEndI"
CHAPTER_VSPACE[78] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[79] = "\\psalmEndI"
CHAPTER_VSPACE[80] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[81] = "\\psalmEndII"
CHAPTER_VSPACE[82] = "\\psalmEndNewPage"
CHAPTER_VSPACE[83] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[84] = "\\psalmEndI"
CHAPTER_VSPACE[85] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[86] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[87] = "\\psalmEndII"
CHAPTER_VSPACE[88] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[89] = "\\psalmEndNewPage"
CHAPTER_VSPACE[90] = "\\psalmEndI"
CHAPTER_VSPACE[91] = "\\psalmEndI"
CHAPTER_VSPACE[92] = "\\psalmEndI"
CHAPTER_VSPACE[93] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[94] = "\\psalmEndNewPage"
CHAPTER_VSPACE[95] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[96] = "\\psalmEndI"
CHAPTER_VSPACE[97] = "\\psalmEndI"
CHAPTER_VSPACE[98] = "\\psalmEndNewPage"
CHAPTER_VSPACE[99] = "\\psalmEndI"
CHAPTER_VSPACE[100] = "\\psalmEndI"
CHAPTER_VSPACE[101] = "\\psalmEndI"
CHAPTER_VSPACE[102] = "\\psalmEndII"
CHAPTER_VSPACE[103] = "\\psalmEndNewPage"
CHAPTER_VSPACE[104] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[105] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[106] = "\\psalmEndNewPage"
CHAPTER_VSPACE[107] = "\\psalmEndI"
CHAPTER_VSPACE[108] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[109] = "\\psalmEndI"
CHAPTER_VSPACE[110] = "\\psalmEndI"
CHAPTER_VSPACE[111] = "\\psalmEndNewPage"
CHAPTER_VSPACE[112] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[113] = "\\psalmEndI"
CHAPTER_VSPACE[114] = "\\psalmEndI"
CHAPTER_VSPACE[115] = "\\psalmEndNewPage"
CHAPTER_VSPACE[116] = "\\psalmEndI"
CHAPTER_VSPACE[117] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[118] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[119] = "\\psalmEndII"
CHAPTER_VSPACE[120] = "\\psalmEndII"
CHAPTER_VSPACE[121] = "\\psalmEndNewPage"
CHAPTER_VSPACE[122] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[123] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[124] = "\\psalmEndNewPage"
CHAPTER_VSPACE[125] = "\\psalmEndII"
CHAPTER_VSPACE[126] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[127] = "\\psalmEndNewPage"
CHAPTER_VSPACE[128] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[129] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[130] = "\\psalmEndNewPage"
CHAPTER_VSPACE[131] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[132] = "\\psalmEndNewPage"
CHAPTER_VSPACE[133] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[134] = "\\psalmEndNewPage"
CHAPTER_VSPACE[135] = "\\psalmEndNewPage"
CHAPTER_VSPACE[136] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[137] = "\\psalmEndNewPage"
CHAPTER_VSPACE[138] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[139] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[140] = "\\psalmEndI"
CHAPTER_VSPACE[141] = "\\psalmEndI"
CHAPTER_VSPACE[142] = "\\psalmEndII"
CHAPTER_VSPACE[143] = "\\psalmEndNewPage"
CHAPTER_VSPACE[144] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[145] = "\\psalmEndI"
CHAPTER_VSPACE[146] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[147] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[148] = "\\psalmEndNewPage"
CHAPTER_VSPACE[149] = "\\psalmEndI"
CHAPTER_VSPACE[150] = "\\psalmEndI"

KEY_PRINTER_LINEBREAK = "$PRX"
TEX_LINEBREAK = "\\linebreak"

def print_chapter(_chapter, _inscript, _body):
  if _inscript:
    text = "\\psalmInscription{" + _inscript + "} " + _body
  else:
    text = _body

  #text = text.replace("¿", "¿~")
  #text = text.replace("?", "~?")
  #text = text.replace(";", "~;")
  #text = text.replace("«", "«~")
  #text = text.replace("»", "~»")
  text = text.replace(KEY_PRINTER_LINEBREAK, TEX_LINEBREAK)
  text = text + CHAPTER_VSPACE[_chapter]

  print("\\psalmChapter{" + str(_chapter) + "}\n")
  print(text + "\n")

path = os.path.dirname(os.path.realpath(__file__))
f = open(path + "/psalmi.csv", "r")

current_chapter = 0
current_verse = 0
inscript = ""
body = ""

line = f.readline()
while line:
  if '#' == line[0]:
    line = f.readline()
    continue

  s = line.split('^')
  chapter = int(s[0])
  verse = int(s[1])
  is_inscript = s[2][0] == 'i'
  text = s[3].rstrip() # removes ending whitespace and '\n'

  if current_chapter != chapter:
    if current_chapter != 0:
      print_chapter(current_chapter, inscript.rstrip(), body.rstrip())

    current_chapter = chapter
    inscript = ""
    body = ""

  if is_inscript:
    inscript = (inscript +
      "\\psalmVerse{" + str(verse) + "}" + text + " ")

    current_verse = verse

  else:
    if current_verse == verse:
      body = body + text + " "
    else:
      body = (body + 
        "\\psalmVerse{" + str(verse) + "}" + text + " ")

    current_verse = verse

  line = f.readline()

print_chapter(current_chapter, inscript.rstrip(), body.rstrip())

f.close()


