#! /usr/bin/env python3

import os
import re
import pdb

CHAPTER_VSPACE = {}
CHAPTER_VSPACE[1] = "\\psalmEnd"
CHAPTER_VSPACE[2] = "\\psalmEndExtra"
CHAPTER_VSPACE[3] = "\\psalmEndNewPage"
CHAPTER_VSPACE[4] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[5] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[6] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[7] = "\\psalmEndNewPage"
CHAPTER_VSPACE[8] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[9] = "\\psalmEndExtra"
CHAPTER_VSPACE[10] = "\\psalmEndNewPage"
CHAPTER_VSPACE[11] = "\\psalmEnd"
CHAPTER_VSPACE[12] = "\\psalmEndExtra"
CHAPTER_VSPACE[13] = "\\psalmEndNewPage"
CHAPTER_VSPACE[14] = "\\psalmEnd"
CHAPTER_VSPACE[15] = "\\psalmEnd"
CHAPTER_VSPACE[16] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[17] = "\\psalmEndNewPage"
CHAPTER_VSPACE[18] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[19] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[20] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[21] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[22] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[23] = "\\psalmEnd"
CHAPTER_VSPACE[24] = "\\psalmEndNewPage"
CHAPTER_VSPACE[25] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[26] = "\\psalmEndNewPage"
CHAPTER_VSPACE[27] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[28] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[29] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[30] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[31] = "\\psalmEndNewPage"
CHAPTER_VSPACE[32] = "\\psalmEnd"
CHAPTER_VSPACE[33] = "\\psalmEnd"
CHAPTER_VSPACE[34] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[35] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[36] = "\\psalmEndNewPage"
CHAPTER_VSPACE[37] = "\\psalmEnd"
CHAPTER_VSPACE[38] = "\\psalmEnd"
CHAPTER_VSPACE[39] = "\\psalmEndNewPage"
CHAPTER_VSPACE[40] = "\\psalmEnd"
CHAPTER_VSPACE[41] = "\\psalmEndNewPage"
CHAPTER_VSPACE[42] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[43] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[44] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[45] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[46] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[47] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[48] = "\\psalmEndNewPage"
CHAPTER_VSPACE[49] = "\\psalmEnd\\psalmEndPictureNewPage"
CHAPTER_VSPACE[50] = "\\psalmEnd"
CHAPTER_VSPACE[51] = "\\psalmEndNewPage"
CHAPTER_VSPACE[52] = "\\psalmEnd"
CHAPTER_VSPACE[53] = "\\psalmEnd"
CHAPTER_VSPACE[54] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[55] = "\\psalmEndNewPage"
CHAPTER_VSPACE[56] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[57] = "\\psalmEndNewPage"
CHAPTER_VSPACE[58] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[59] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[60] = "\\psalmEnd"
CHAPTER_VSPACE[61] = "\\psalmEndNewPage"
CHAPTER_VSPACE[62] = "\\psalmEnd"
CHAPTER_VSPACE[63] = "\\psalmEnd"
CHAPTER_VSPACE[64] = "\\psalmEnd"
CHAPTER_VSPACE[65] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[66] = "\\psalmEnd"
CHAPTER_VSPACE[67] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[68] = "\\psalmEndExtra"
CHAPTER_VSPACE[69] = "\\psalmEndNewPage"
CHAPTER_VSPACE[70] = "\\psalmEnd"
CHAPTER_VSPACE[71] = "\\psalmEnd"
CHAPTER_VSPACE[72] = "\\psalmEndExtra"
CHAPTER_VSPACE[73] = "\\psalmEndNewPage"
CHAPTER_VSPACE[74] = "\\psalmEnd"
CHAPTER_VSPACE[75] = "\\psalmEnd"
CHAPTER_VSPACE[76] = "\\psalmEnd"
CHAPTER_VSPACE[77] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[78] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[79] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[80] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[81] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[82] = "\\psalmEndExtra"
CHAPTER_VSPACE[83] = "\\psalmEndNewPage"
CHAPTER_VSPACE[84] = "\\psalmEnd"
CHAPTER_VSPACE[85] = "\\psalmEndNewPage"
CHAPTER_VSPACE[86] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[87] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[88] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[89] = "\\psalmEnd"
CHAPTER_VSPACE[90] = "\\psalmEnd"
CHAPTER_VSPACE[91] = "\\psalmEnd"
CHAPTER_VSPACE[92] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[93] = "\\psalmEnd"
CHAPTER_VSPACE[94] = "\\psalmEnd"
CHAPTER_VSPACE[95] = "\\psalmEndNewPage"
CHAPTER_VSPACE[96] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[97] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[98] = "\\psalmEnd"
CHAPTER_VSPACE[99] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[100] = "\\psalmEndNewPage"
CHAPTER_VSPACE[101] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[102] = "\\psalmEnd"
CHAPTER_VSPACE[103] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[104] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[105] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[106] = "\\psalmEnd"
CHAPTER_VSPACE[107] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[108] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[109] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[110] = "\\psalmEndNewPage"
CHAPTER_VSPACE[111] = "\\psalmEnd"
CHAPTER_VSPACE[112] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[113] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[114] = "\\psalmEnd"
CHAPTER_VSPACE[115] = "\\psalmEndNewPage"
CHAPTER_VSPACE[116] = "\\psalmEnd"
CHAPTER_VSPACE[117] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[118] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[119] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[120] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[121] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[122] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[123] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[124] = "\\psalmEnd"
CHAPTER_VSPACE[125] = "\\psalmEndExtra"
CHAPTER_VSPACE[126] = "\\psalmEnd"
CHAPTER_VSPACE[127] = "\\psalmEndNewPage"
CHAPTER_VSPACE[128] = "\\psalmEnd"
CHAPTER_VSPACE[129] = "\\psalmEnd"
CHAPTER_VSPACE[130] = "\\psalmEnd"
CHAPTER_VSPACE[131] = "\\psalmEnd"
CHAPTER_VSPACE[132] = "\\psalmEnd"
CHAPTER_VSPACE[133] = "\\psalmEnd"
CHAPTER_VSPACE[134] = "\\psalmEnd"
CHAPTER_VSPACE[135] = "\\psalmEndNewPage"
CHAPTER_VSPACE[136] = "\\psalmEnd"
CHAPTER_VSPACE[137] = "\\psalmEnd"
CHAPTER_VSPACE[138] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[139] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[140] = "\\psalmEnd"
CHAPTER_VSPACE[141] = "\\psalmEnd"
CHAPTER_VSPACE[142] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[143] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[144] = "\\psalmEnd"
CHAPTER_VSPACE[145] = "\\psalmEndNewPage"
CHAPTER_VSPACE[146] = "\\psalmEnd"
CHAPTER_VSPACE[147] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[148] = "\\psalmEnd"
CHAPTER_VSPACE[149] = "\\psalmEnd"
CHAPTER_VSPACE[150] = "\\psalmEnd\\psalmEndPictureNewPage"

KEY_PRINTER_LINEBREAK = "$PRX"
TEX_LINEBREAK = "\\linebreak"

def print_chapter(_chapter, _inscript, _body):
  if _inscript:
    text = "\\psalmInscription{" + _inscript + "} " + _body
  else:
    text = _body

  text = text.replace("¿", "¿~")
  text = text.replace("?", "~?")
  text = text.replace(";", "~;")
  text = text.replace("«", "«~")
  text = text.replace("»", "~»")
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


