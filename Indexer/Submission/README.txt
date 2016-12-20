Assignment 2:
Goal: Implementing your own inverted index. Text processing and corpus statistics.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has references and detailed information regarding how to setup, compile and run the programs in the assignment.
The tasks are discussed below in brief:
-- Task1: Generating the corpus
		 The corpus is being generated using the raw wikipedia articles that we downloaded as a part of HW1 Q1. Each text file correponds to one Wikipedia article. The file name is same as that of the article title without underscores or hyphens. The correponding file for the code is Task1.py.
-- Task2: Implementing an inverted indexer and creating inverted indexes 
		 Implementation of an inverted indexer that consumes the corpus in Task 1 and produces an inverted index as output. The file for the code is Indexer.py. The indexer generates indexes for unigrams, bigrams and trigrams. 
-- Task3: Corpus Statistics.
		 For each inverted index in Task2 we generate a term frequency table and document frequency table. We aso generate an stop list using the unigram data.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

GENERAL USAGE NOTES:

-- This file contains instructions about installing softwares and running the programs in Windows Environment.
-- The instructions in the file may not match the installation procedures in other operating systems like Mac OS, Ubuntu OS etc.
-- However, the programs are independent of any operating systems and will run successfully in all platforms once the initial installation has been done. 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTALLATION GUIDE:

-- Download python 2.7.x from https://www.python.org/download/releases/2.7/
-- From Windows Home go to Control Panel -> System and Security -> System -> Advanced System Settings -> Environment Variables and add two new variables in 'PATH' -> [Home directory of Python]; [Home directory of Python]\Scripts
-- Open Command Prompt and upgrade pip using the following command: 'python -m pip install -U pip'
-- Install BeautifulSoup by using the command 'pip install beautifulsoup4'

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTRUCTIONS TO RUN THE PROGRAM:

-- Open Windows PowerShell
-- Navigate to the directory having the programs
-- Perform the following steps in order:
		1. Put all the raw text files having the downloaded web pages inside the folder 'raw_content'. My downloaded web pages are already provided in the above mentioned folder.
		2. Run Task1.py using the command 'python Task1.py'. It will generate the corpus after proessing and cleaning the web pages in the folder 'corpus'
		3. Run Indexer.py using the command 'python Indexer.py'. Follow the instructions and it will generate inverted indexes using the files in the folder 'corpus' and store the document frequency tables and term frequency tables in the present directory.


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

DESIRED RESULTS:

-- The programs create the following output  
	1. Task1.py generates the corpus from the web pages in the folder 'raw_content' and stores them in the folder 'corpus'
	2. Indexer.py generates the index for unigrams, bigrams and trigrams using the files in 'corpus' folder. It prints the document frequency table and term frequency table for unigrams, bigrams and trigrams in the present directory. The token count in each document for all the above three n-grams are stored in a data structure (dictionary in python) where the key is the document name and value is the number of tokens. The token count values are printed in the console while the indexer is run.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

MAP OF 'WHAT TO HAND IN' AND FILE NAMES:

ITEM 1 : Task1.py
         Indexer.py
ITEM 2 : README.txt
ITEM 3 : doc_freq_table_unigram.txt
		 doc_freq_table_bigram.txt
		 doc_freq_table_trigram.txt
		 term_freq_table_unigram.txt
		 term_freq_table_bigram.txt
		 term_freq_table_trigram.txt
ITEM 4 : Stoplist.txt
ITEM 5 : Bonus_Task\unigram_plot.png
		 Bonus_Task\bigram_plot.png
		 Bonus_Task\trigram_plot.png

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTRIBUTORS and CITATIONS:

-- https://www.crummy.com/software/BeautifulSoup/ : BeautifulSoup has been used for extracting links from web pages
-- https://learnpythonthehardway.org/book/ : Python Programming

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTACT DETAILS:

The author of the README can be contacted via:
Phone: (+1) 6173727648
E-Mail: nandi.t@husky.neu.edu