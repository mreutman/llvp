#! /usr/bin/env python3

import os
import re
import pdb

CHAPTER_VSPACE = {}
CHAPTER_VSPACE[1] = r"\psalmEnd{3}"
CHAPTER_VSPACE[2] = r"\psalmEndNewPage"
CHAPTER_VSPACE[3] = r"\psalmEndII"
CHAPTER_VSPACE[4] = r"\psalmEndII"
CHAPTER_VSPACE[5] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[6] = r"\psalmEndNewPage\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[7] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[8] = r"\psalmEnd{4}"
CHAPTER_VSPACE[9] = r"\psalmEndNewPage"
CHAPTER_VSPACE[10] = r"\psalmEnd{2}"
CHAPTER_VSPACE[11] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[12] = r"\psalmEnd{2}"
CHAPTER_VSPACE[13] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[14] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[15] = r"\psalmEndNewPage\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[16] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[17] = r"\psalmEndDecorateNewPage\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[18] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[19] = r"\psalmEnd{2}"
CHAPTER_VSPACE[20] = r"\psalmEndNewPage"
CHAPTER_VSPACE[21] = r"\psalmEnd{1}"
CHAPTER_VSPACE[22] = r"\psalmEnd{1}"
CHAPTER_VSPACE[23] = r"\psalmEndNewPage"
CHAPTER_VSPACE[24] = r"\psalmEnd{1}"
CHAPTER_VSPACE[25] = r"\psalmEnd{2}"
CHAPTER_VSPACE[26] = r"\psalmEndNewPage"
CHAPTER_VSPACE[27] = r"\psalmEnd{2}"
CHAPTER_VSPACE[28] = r"\psalmEndNewPage"
CHAPTER_VSPACE[29] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[30] = r"\psalmEndDecorateNewPage\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[31] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[32] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[33] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[34] = r"\psalmEndDecorate{2}"
CHAPTER_VSPACE[35] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[36] = r"\psalmEnd{2}"
CHAPTER_VSPACE[37] = r"\psalmEnd{2}"
CHAPTER_VSPACE[38] = r"\psalmEndNewPage"
CHAPTER_VSPACE[39] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[40] = r"\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[41] = r"\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[42] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[43] = r"\psalmEndNewPage\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[44] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[45] = r"\psalmEnd{2}"
CHAPTER_VSPACE[46] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[47] = r"\psalmEnd{1}"
CHAPTER_VSPACE[48] = r"\psalmEnd{2}"
CHAPTER_VSPACE[49] = r"\psalmEnd{1}"
CHAPTER_VSPACE[50] = r"\psalmEndNewPage"
CHAPTER_VSPACE[51] = r"\psalmEnd{2}"
CHAPTER_VSPACE[52] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[53] = r"\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[54] = r"\psalmEnd{2}"
CHAPTER_VSPACE[55] = r"\psalmEndNewPage"
CHAPTER_VSPACE[56] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[57] = r"\psalmEnd{2}"
CHAPTER_VSPACE[58] = r"\psalmEndNewPage"
CHAPTER_VSPACE[59] = r"\psalmEnd{3}"
CHAPTER_VSPACE[60] = r"\psalmEndNewPage"
CHAPTER_VSPACE[61] = r"\psalmEnd{2}"
CHAPTER_VSPACE[62] = r"\psalmEndNewPage"
CHAPTER_VSPACE[63] = r"\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[64] = r"\psalmEnd{2}"
CHAPTER_VSPACE[65] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[66] = r"\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[67] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[68] = r"\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[69] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[70] = r"\psalmEndNewPage\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[71] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[72] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[73] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[74] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[75] = r"\psalmEndNewPage"
CHAPTER_VSPACE[76] = r"\psalmEnd{2}"
CHAPTER_VSPACE[77] = r"\psalmEnd{2}"
CHAPTER_VSPACE[78] = r"\psalmEndNewPage"
CHAPTER_VSPACE[79] = r"\psalmEnd{2}"
CHAPTER_VSPACE[80] = r"\psalmEndDecorate{2}"
CHAPTER_VSPACE[81] = r"\psalmEndDecorateNewPage\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[82] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[83] = r"\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[84] = r"\psalmEnd{2}"
CHAPTER_VSPACE[85] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[86] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[87] = r"\psalmEnd{2}"
CHAPTER_VSPACE[88] = r"\psalmEndNewPage"
CHAPTER_VSPACE[89] = r"\psalmEnd{3}"
CHAPTER_VSPACE[90] = r"\psalmEnd{3}"
CHAPTER_VSPACE[91] = r"\psalmEndNewPage"
CHAPTER_VSPACE[92] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[93] = r"\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[94] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[95] = r"\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[96] = r"\psalmEnd{1}"
CHAPTER_VSPACE[97] = r"\psalmEnd{1}"
CHAPTER_VSPACE[98] = r"\psalmEndNewPage"
CHAPTER_VSPACE[99] = r"\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[100] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[101] = r"\psalmEndNewPage"
CHAPTER_VSPACE[102] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[103] = r"\psalmEnd{3}"
CHAPTER_VSPACE[104] = r"\psalmEnd{2}"
CHAPTER_VSPACE[105] = r"\psalmEnd{2}"
CHAPTER_VSPACE[106] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[107] = r"\psalmEnd{2}"
CHAPTER_VSPACE[108] = r"\psalmEnd{1}"
CHAPTER_VSPACE[109] = r"\psalmEndNewPage"
CHAPTER_VSPACE[110] = r"\psalmEnd{2}"
CHAPTER_VSPACE[111] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[112] = r"\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[113] = r"\psalmEnd{2}"
CHAPTER_VSPACE[114] = r"\psalmEnd{2}"
CHAPTER_VSPACE[115] = r"\psalmEndNewPage\psalmEndDecorate{1}"
CHAPTER_VSPACE[116] = r"\psalmEndDecorate{2}"
CHAPTER_VSPACE[117] = r"\psalmEndDecorate{2}"
CHAPTER_VSPACE[118] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[119] = r"\psalmEnd{2}"
CHAPTER_VSPACE[120] = r"\psalmEnd{2}"
CHAPTER_VSPACE[121] = r"\psalmEndNewPage"
CHAPTER_VSPACE[122] = r"\psalmEnd{2}"
CHAPTER_VSPACE[123] = r"\psalmEnd{2}"
CHAPTER_VSPACE[124] = r"\psalmEndNewPage"
CHAPTER_VSPACE[125] = r"\psalmEnd{2}"
CHAPTER_VSPACE[126] = r"\psalmEnd{2}"
CHAPTER_VSPACE[127] = r"\psalmEndNewPage"
CHAPTER_VSPACE[128] = r"\psalmEnd{3}"
CHAPTER_VSPACE[129] = r"\psalmEnd{3}"
CHAPTER_VSPACE[130] = r"\psalmEndNewPage"
CHAPTER_VSPACE[131] = r"\psalmEndDecorate{2}"
CHAPTER_VSPACE[132] = r"\psalmEndNewPage"
CHAPTER_VSPACE[133] = r"\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[134] = r"\psalmEndNewPage"
CHAPTER_VSPACE[135] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[136] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[137] = r"\psalmEndNewPage"
CHAPTER_VSPACE[138] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[139] = r"\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[140] = r"\psalmEnd{2}"
CHAPTER_VSPACE[141] = r"\psalmEnd{2}"
CHAPTER_VSPACE[142] = r"\psalmEnd{2}"
CHAPTER_VSPACE[143] = r"\psalmEndNewPage"
CHAPTER_VSPACE[144] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[145] = r"\psalmEnd{2}"
CHAPTER_VSPACE[146] = r"\psalmEndDecorateNewPage"
CHAPTER_VSPACE[147] = r"\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[148] = r"\psalmEndNewPage"
CHAPTER_VSPACE[149] = r"\psalmEnd{2}"
CHAPTER_VSPACE[150] = r"\psalmEnd{2}"

KEY_PRINTER_LINEBREAK = "$PRX"
TEX_LINEBREAK = r"\linebreak"

def print_chapter(_chapter, _inscript, _body):
  if _inscript:
    text = r"\psalmInscription{" + _inscript + "} " + _body
  else:
    text = _body

  #text = text.replace("¿", "¿~")
  #text = text.replace("?", "~?")
  #text = text.replace(";", "~;")
  #text = text.replace("«", "«~")
  #text = text.replace("»", "~»")
  text = text.replace(KEY_PRINTER_LINEBREAK, TEX_LINEBREAK)
  text = text + CHAPTER_VSPACE[_chapter]

  print(r"\psalmChapter{" + str(_chapter) + "}\n")
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
      r"\psalmVerse{" + str(verse) + "}" + text + " ")

    current_verse = verse

  else:
    if current_verse == verse:
      body = body + text + " "
    else:
      body = (body + 
        r"\psalmVerse{" + str(verse) + "}" + text + " ")

    current_verse = verse

  line = f.readline()

print_chapter(current_chapter, inscript.rstrip(), body.rstrip())

f.close()


