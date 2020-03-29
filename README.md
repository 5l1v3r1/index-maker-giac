# index-maker-giac
Just a little index maker for GIAC exam books since I was having problems with voltaire

# Requirements
 - Only tested on Ubuntu 19.04
 - Must have texlive-full package installed `sudo apt install texlive-full`
 - Make executeabe with `chmod a+x index_maker.py`
 - Run `./index_maker.py -h` for help
 - Must provide CSV file with four fields
   - index_entry, description, book, page #
   - make sure there are no commas in file except to seperate fields

# Known Issues
 - Does not work if '#' or '&' characters in any filed of CSV
   - Best to just not use these characters
 - Only Works with UTF-8 Characters
 - if index entry is a number like '806.11' it will not appear in index
