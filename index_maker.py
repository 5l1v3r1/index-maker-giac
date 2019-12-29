#!/bin/python3

import csv
import argparse
import os

ALPHABET_DICT = {
				 'A':[],  'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[], 'H':[], 'I':[], 'J':[], 'K':[], 'L':[], 'M':[],
				 'N':[], 'O':[], 'P':[], 'Q':[], 'R':[], 'S':[], 'T':[], 'U':[], 'V':[], 'W':[], 'X':[], 'Y':[], 'Z':[]
                }

TEX_PREAMBLE = ('\\documentclass{article}\n'
				'\\usepackage[utf8]{inputenc}\n'
				'\\usepackage[english]{babel}\n'
				'\\usepackage{sectsty}\n'
				'\\usepackage[document]{ragged2e}\n'
				'\\usepackage{multicol}\n'
				'\\setlength{\\columnsep}{1cm}\n'
				'\\setcounter{secnumdepth}{0}\n'
				'\\allsectionsfont{\\centering} \n'
				'\\begin{document}\n'
				)

TEX_POST_DOC = ('\\end{document}')


def make_index_page_title(letter_title):
	tex_page_start = ('\\begin{multicols}{2}\n'
					  '[\n'
					  '\\section{' + letter_title +
					  '}\n'
					  ']\n'
					  )
	return tex_page_start


def make_index_for_page(rows):
	indexes_for_page = ''
	for row in rows:
		indexes_for_page += '\\textbf{' + row[0] + '} ' + row[1] + '[b.' + row[2] + '/pg.' + row[3] + ']\\\\\n'
	indexes_for_page += '\\end{multicols}\n\\newpage\n'
	
	return indexes_for_page


def make_index_pages():
	pages = ''
	for key in sorted(ALPHABET_DICT.keys()):
		pages += make_index_page_title(key)
		pages += make_index_for_page(ALPHABET_DICT[key])

	return pages


def make_index(infile, outfile):
	# open file and read into index_dict
	with open(infile, newline='') as csvfile:
		index_dict = sorted(csv.reader(csvfile))
		#for row in index_dict:
		#	print(row)


	# Make dictionary to hold by letter
	for letter in ALPHABET_DICT:
		for row in index_dict:
			if (row[0][0].upper() == letter):
				ALPHABET_DICT[letter].append(row)



	document = TEX_PREAMBLE
	document += make_index_pages()
	document += TEX_POST_DOC

	with open('generated_index.tex', 'w') as newfile:
		newfile.write(document)

	print(outfile)
	os.system('pdflatex -output-directory=. -jobname=' + outfile + ' generated_index.tex')
	os.system('rm *.tex')
	os.system('rm *.aux')
	os.system('rm *.log')


description = "Makes a PDF index from CSV file suitable for use in GIAC Exams\n"
description += "Must have latex installed.  On Ubuntu use 'sudo apt install texlive-full'\n"
description += "Warning - texlive-full is a large download and can take a while.\n"
description += "Do Not use an extension on the outfile arg.  pdf will be placed automatically\n"

parser = argparse.ArgumentParser(description=description)
parser.add_argument('-i', '--infile', type=str, help='Name of csv file to be used', required=True)
parser.add_argument('-o', '--outfile', type=str, help='Name of pdf to be produced.  Do not type file extension', default='index')

args = parser.parse_args()


make_index(args.infile, args.outfile)
