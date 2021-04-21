#!/bin/bash


OSID="XXXXX"
EXAM_REPORT="OSCP-OS-$OSID-Exam-Report.pdf"
LAB_REPORT="OSCP-OS-$OSID-Lab-Report.pdf"
ZIP_PACKAGE="OSCP-OS-$OSID-Exam-Report.7z"
ZIP_LAB_PACKAGE="OSCP-OS-$OSID-Lab-Report.7z"


if [ ! -e /usr/share/pandoc/data/templates/eisvogel.latex ]
then
    sudo cp ressources/eisvogel.latex /usr/share/pandoc/data/templates/
fi


echo "Generating exam report..."
pandoc exam_report.md -o $EXAM_REPORT \
--from markdown+yaml_metadata_block+raw_html \
--template res/eisvogel \
--table-of-contents \
--toc-depth 6 \
--number-sections \
--top-level-division=chapter \
--highlight-style zenburn

echo "Generating lab report..."
pandoc lab_report.md -o $LAB_REPORT \
--from markdown+yaml_metadata_block+raw_html \
--template res/eisvogel \
--table-of-contents \
--toc-depth 6 \
--number-sections \
--top-level-division=chapter \
--highlight-style zenburn
#echo "Creating 7z package..."
7z a $ZIP_LAB_PACKAGE -pOS-$OSID $LAB_REPORT
7z a $ZIP_PACKAGE -pOS-$OSID $EXAM_REPORT