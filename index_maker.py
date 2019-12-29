import csv

TEX_PREAMBLE = ('\\documentclass{article}\n'
				'\\usepackage[utf8]{inputenc}\n'
				'\\usepackage[english]{babel}\n'
				'\\usepackage{sectsty}\n'
				'\\usepackage{multicol}\n'
				'\\setlength{\\columnsep}{1cm}\n'
				'\\setcounter{secnumdepth}{0}\n'
				'\\allsectionsfont{\\centering} \n'
				'\\begin{document}\n'
				)

TEX_POST_DOC = ('\\end{document}')


def make_start_page(letter_title):
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
		indexes_for_page += '\\textbf{' + row[0] + '} ' + row[1] + '[b.' + row[2] + '/pg.' + row[3] + ']\\\\'
	indexes_for_page += '\\end{multicols}\n\\newpage\n'
	return indexes_for_page


# open file and read into index_dict
with open('401_index.csv', newline='') as csvfile:
	index_dict = sorted(csv.reader(csvfile))
	for row in index_dict:
		print(row)

