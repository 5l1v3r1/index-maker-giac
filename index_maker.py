import csv

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


# open file and read into index_dict
with open('401_index.csv', newline='') as csvfile:
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

with open('generated_index.tex', 'w') as outfile:
	outfile.write(document)


