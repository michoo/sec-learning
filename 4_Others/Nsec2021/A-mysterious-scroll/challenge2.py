#!/usr/bin/env python3

# import xml.dom.minidom

import zipfile
import lxml.etree
import re

        
result3 = []
linenum = 0
pattern = re.compile(r"(<w:rFonts w:ascii=)(.*)(\/>)", re.IGNORECASE)

with open ('document.xml', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        result3 = re.findall('(<w:rFonts w:ascii=.*?"\/>)', line)

print(list(set(result3)))


result2=list(set(result3))
#read input file
fin = open("document.xml", "rt")
#read file contents to string
data = fin.read()
for index, resultitem in enumerate(result2):
    textToFind = resultitem
    textToReplace = "{}{}{}{}{}{}".format(resultitem, "</w:rPr><w:t>",index,"</w:t>","<w:rPr>", resultitem)
    #data = re.sub(resultitem, textToReplace, resultitem)
#replace all occurrences of the required string
    data = data.replace(textToFind, textToReplace)
    print(index)
#close the input file
fin.close()
#open the input file in write mode
fin = open("document2.xml", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()
