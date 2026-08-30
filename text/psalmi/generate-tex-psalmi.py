#! /usr/bin/env python3

import os
import re
import pdb

CHAPTER_VSPACE = {}
CHAPTER_VSPACE[1] = "\\psalmEnd"
CHAPTER_VSPACE[2] = "\\psalmEndNewPage"
CHAPTER_VSPACE[3] = "\\psalmEnd"
CHAPTER_VSPACE[4] = "\\psalmEnd"
CHAPTER_VSPACE[5] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[6] = "\\psalmEndNewPage"
CHAPTER_VSPACE[7] = "\\psalmEnd"
CHAPTER_VSPACE[8] = "\\psalmEnd"
CHAPTER_VSPACE[9] = "\\psalmEnd"
CHAPTER_VSPACE[10] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[11] = "\\psalmEnd"
CHAPTER_VSPACE[12] = "\\psalmEndNewPage"
CHAPTER_VSPACE[13] = "\\psalmEnd"
CHAPTER_VSPACE[14] = "\\psalmEnd"
CHAPTER_VSPACE[15] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[16] = "\\psalmEndNewPage"
CHAPTER_VSPACE[17] = "\\psalmEndNewPage"
CHAPTER_VSPACE[18] = "\\psalmEndDecorate{1}"
CHAPTER_VSPACE[19] = "\\psalmEnd"
CHAPTER_VSPACE[20] = "\\psalmEnd"
CHAPTER_VSPACE[21] = "\\psalmEndNewPage"
CHAPTER_VSPACE[22] = "\\psalmEnd"
CHAPTER_VSPACE[23] = "\\psalmEnd"
CHAPTER_VSPACE[24] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[25] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[26] = "\\psalmEndNewPage"
CHAPTER_VSPACE[27] = "\\psalmEnd"
CHAPTER_VSPACE[28] = "\\psalmEndNewPage"
CHAPTER_VSPACE[29] = "\\psalmEnd"
CHAPTER_VSPACE[30] = "\\psalmEnd"
CHAPTER_VSPACE[31] = "\\psalmEnd"
CHAPTER_VSPACE[32] = "\\psalmEnd"
CHAPTER_VSPACE[33] = "\\psalmEndNewPage"
CHAPTER_VSPACE[34] = "\\psalmEnd"
CHAPTER_VSPACE[35] = "\\psalmEnd"
CHAPTER_VSPACE[36] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[37] = "\\psalmEnd"
CHAPTER_VSPACE[38] = "\\psalmEndNewPage"
CHAPTER_VSPACE[39] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[40] = "\\psalmEnd"
CHAPTER_VSPACE[41] = "\\psalmEnd"
CHAPTER_VSPACE[42] = "\\psalmEnd"
CHAPTER_VSPACE[43] = "\\psalmEnd"
CHAPTER_VSPACE[44] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[45] = "\\psalmEndNewPage"
CHAPTER_VSPACE[46] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[47] = "\\psalmEndNewPage"
CHAPTER_VSPACE[48] = "\\psalmEnd"
CHAPTER_VSPACE[49] = "\\psalmEnd"
CHAPTER_VSPACE[50] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[51] = "\\psalmEndNewPage"
CHAPTER_VSPACE[52] = "\\psalmEnd"
CHAPTER_VSPACE[53] = "\\psalmEnd"
CHAPTER_VSPACE[54] = "\\psalmEnd"
CHAPTER_VSPACE[55] = "\\psalmEnd"
CHAPTER_VSPACE[56] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[57] = "\\psalmEndDecorate{1}"
CHAPTER_VSPACE[58] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[59] = "\\psalmEndNewPage"
CHAPTER_VSPACE[60] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[61] = "\\psalmEndNewPage"
CHAPTER_VSPACE[62] = "\\psalmEndDecorate{1}"
CHAPTER_VSPACE[63] = "\\psalmEndNewPage"
CHAPTER_VSPACE[64] = "\\psalmEnd"
CHAPTER_VSPACE[65] = "\\psalmEnd"
CHAPTER_VSPACE[66] = "\\psalmEnd"
CHAPTER_VSPACE[67] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[68] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[69] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[70] = "\\psalmEndDecorate{3.0}"
CHAPTER_VSPACE[71] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[72] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[73] = "\\psalmEnd"
CHAPTER_VSPACE[74] = "\\psalmEnd"
CHAPTER_VSPACE[75] = "\\psalmEnd"
CHAPTER_VSPACE[76] = "\\psalmEndNewPage"
CHAPTER_VSPACE[77] = "\\psalmEnd"
CHAPTER_VSPACE[78] = "\\psalmEndDecorate{2.0}"
CHAPTER_VSPACE[79] = "\\psalmEnd"
CHAPTER_VSPACE[80] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[81] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[82] = "\\psalmEndNewPage"
CHAPTER_VSPACE[83] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[84] = "\\psalmEnd"
CHAPTER_VSPACE[85] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[86] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[87] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[88] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[89] = "\\psalmEndNewPage"
CHAPTER_VSPACE[90] = "\\psalmEnd"
CHAPTER_VSPACE[91] = "\\psalmEnd"
CHAPTER_VSPACE[92] = "\\psalmEnd"
CHAPTER_VSPACE[93] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[94] = "\\psalmEndNewPage"
CHAPTER_VSPACE[95] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[96] = "\\psalmEnd"
CHAPTER_VSPACE[97] = "\\psalmEnd"
CHAPTER_VSPACE[98] = "\\psalmEndNewPage"
CHAPTER_VSPACE[99] = "\\psalmEnd"
CHAPTER_VSPACE[100] = "\\psalmEnd"
CHAPTER_VSPACE[101] = "\\psalmEnd"
CHAPTER_VSPACE[102] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[103] = "\\psalmEndNewPage"
CHAPTER_VSPACE[104] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[105] = "\\psalmEndDecorate{2.5}"
CHAPTER_VSPACE[106] = "\\psalmEndNewPage"
CHAPTER_VSPACE[107] = "\\psalmEnd"
CHAPTER_VSPACE[108] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[109] = "\\psalmEnd"
CHAPTER_VSPACE[110] = "\\psalmEnd"
CHAPTER_VSPACE[111] = "\\psalmEndNewPage"
CHAPTER_VSPACE[112] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[113] = "\\psalmEnd"
CHAPTER_VSPACE[114] = "\\psalmEnd"
CHAPTER_VSPACE[115] = "\\psalmEndNewPage"
CHAPTER_VSPACE[116] = "\\psalmEnd"
CHAPTER_VSPACE[117] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[118] = "\\psalmEndDecorateNewPage"
CHAPTER_VSPACE[119] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[120] = "\\psalmEndExtra{2}"
CHAPTER_VSPACE[121] = "\\psalmEndNewPage"
CHAPTER_VSPACE[122] = "\\psalmEndDecorate{1.5}"
CHAPTER_VSPACE[123] = "\\psalmEndDecorate{1.0}"
CHAPTER_VSPACE[124] = "\\psalmEndNewPage"
CHAPTER_VSPACE[125] = "\\psalmEndExtra{2}"
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
CHAPTER_VSPACE[139] = "\\psalmEnd"
CHAPTER_VSPACE[140] = "\\psalmEnd"
CHAPTER_VSPACE[141] = "\\psalmEnd"
CHAPTER_VSPACE[142] = "\\psalmEnd"
CHAPTER_VSPACE[143] = "\\psalmEnd"
CHAPTER_VSPACE[144] = "\\psalmEnd"
CHAPTER_VSPACE[145] = "\\psalmEnd"
CHAPTER_VSPACE[146] = "\\psalmEnd"
CHAPTER_VSPACE[147] = "\\psalmEnd"
CHAPTER_VSPACE[148] = "\\psalmEnd"
CHAPTER_VSPACE[149] = "\\psalmEnd"
CHAPTER_VSPACE[150] = "\\psalmEnd"

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


