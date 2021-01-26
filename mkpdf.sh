#!/bin/sh
cd proof
for i in *.tex; do pdflatex $i;done
find {*.aux,*.log,*.nav,*.out,*.snm,*.gz,*.toc,*.dvi,*.vrb} -exec rm {} \;
