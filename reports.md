# Reports

## Installation

- MarkdownPP
pip install MarkdownPP

- Pandoc
https://github.com/jgm/pandoc/releases
https://github.com/jgm/pandoc/releases/download/2.11.3.2/pandoc-2.11.3.2-1-amd64.deb

```bash
sudo dpkg -i pandoc.*.deb
```

- LaTeX (eg. TeX Live) in order to get pdflatex or xelatex

```bash
sudo apt install texlive-full
```

- Eisvogel Pandoc LaTeX PDF Template (already include)
https://github.com/Wandmalfarbe/pandoc-latex-template/blob/master/eisvogel.tex

## Reports scripts

- ./new_report.sh will generate a new directory with everything to start writing a report
- into report directory (date), you'll find a script ./generate.sh, it will generate everything pdf, and 7z