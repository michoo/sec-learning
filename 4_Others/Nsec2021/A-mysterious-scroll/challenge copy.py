#!/usr/bin/env python3

# import xml.dom.minidom

import zipfile
import lxml.etree
import re

def parseXML(root):
    """
    Parse the xml
    """
    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)


document = zipfile.ZipFile('x.docx')
xml_content = document.read('word/document.xml')
# root = lxml.etree.fromstring(xml_content)

# ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
# ns_pfx = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
# pgSz_el = root.find('.//w:pgSz', ns)
# pgMar_el = root.find('.//w:pgMar', ns)

# print(pgSz_el.get(ns_pfx + 'w'))           # 12240
# print(pgMar_el.get(ns_pfx + 'footer'))     # 720

#print(xml_content)

result = []
with open ('document.xml', 'rt') as myfile:
    for line in myfile:
        x = line.split("/></w:rPr><w:t>x</w:t></w:r>")
        if len(x) > 1:
            
            for item in x:
                y = item.split("<w:rFonts w:ascii=")
                if len(y) > 1:
                    result.append(y[1])
            print(list(set(result)))

result2=list(set(result))
#read input file
fin = open("document.xml", "rt")
#read file contents to string
data = fin.read()
for index, resultitem in enumerate(result2):
    textToFind = resultitem + "/></w:rPr><w:t>x</w:t></w:r>"
    textToReplace = "{}{}{}{}".format(resultitem, "/></w:rPr><w:t>x", index, "</w:t></w:r>")
#replace all occurrences of the required string
    data = data.replace(textToFind, textToReplace)
#close the input file
fin.close()
#open the input file in write mode
fin = open("document2.xml", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()


        
# errors = []
# linenum = 0
# pattern = re.compile(r">x", re.IGNORECASE)

# with open ('document.xml', 'rt') as myfile:    
#     for line in myfile:
#         linenum += 1
#         if pattern.search(line) != None:      # If a match is found 
#             errors.append((linenum, line.rstrip('\n')))
# for err in errors:                            # Iterate over the list of tuples
#     print("Line " + str(err[0]) + ": " + err[1])
#algo
#chercher /></w:rPr><w:t>x
#revenir jusqu' au precedent <w:rFonts w:ascii=
# liste unique
# iteration de liste unique et chercher tous les <w:rFonts w:ascii= + listelement + /></w:rPr><w:t>x
# remplacer par <w:rFonts w:ascii= + listelement + /></w:rPr><w:t> + compteur

compteur = 0
# for line in xml_content:
#         # For each line, check if line contains the string
#         # if '/></w:rPr><w:t>x' in line:
#         #     compteur=compteur+1
#         print(line)

print(compteur)
# # Replace the target string
# xml_content.replace('ram', 'abcd')



# # Write the file out again
# with file = open('document.xml', 'w') :
#   file.write(xml_content)