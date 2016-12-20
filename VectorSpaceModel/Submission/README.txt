Assignment 2:
Goal: Introduction to Lucene. Retrieval and scoring using Cosine Similarity

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has references and detailed information regarding how to setup, compile and run the programs in the assignment.

The tasks are discussed below in brief:
-- Task1: Introduction to Lucene
		  Download Lecene and do a local setup for the same. Go through the Lucene documentation and the provided code to perform the     following:
			 A. Index the raw documents of Assignment 3 using "SimpleAnalyzer".
			 B. Perform search operation for the four queries provided in Task2 and return top 100 results for each query using the default document scoring/ranking function provided by Lucene.
		 
-- Task2: Use the "Sustainable Energy" Wikipedia corpus and implement the Vector Space Cosine Similarity ranking algorithm to provide 
		  a ranked list of documents for a file with one or more queries. Submit the output from this run for the top 100 search results.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

GENERAL USAGE NOTES:

-- This file contains instructions about installing softwares and running the programs in Windows Environment.
-- The instructions in the file may not match the installation procedures in other operating systems like Mac OS, Ubuntu OS etc.
-- However, the programs are independent of any operating systems and will run successfully in all platforms once the initial installation has been done. 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTALLATION GUIDE:

-- Download python 2.7.x from https://www.python.org/download/releases/2.7/
-- From Windows Home go to Control Panel -> System and Security -> System -> Advanced System Settings -> Environment Variables and add two new variables in 'PATH' -> [Home directory of Python]; [Home directory of Python]\Scripts
-- Open Command Prompt and upgrade pip using the following command: 'python -m pip install -U pip'
-- Install BeautifulSoup by using the command 'pip install beautifulsoup4'

-- Download Java 1.8 from  https://www.java.com/en/download/
-- Do a local setup of Java by adding proper Environment Variables and Path
-- Download Lucene from https://archive.apache.org/dist/lucene/java/4.7.2/ and do a local set up of the same.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

INSTRUCTIONS TO RUN THE PROGRAM:

-- In order to run Task1, perform the following steps:
     A. Make a new project in Java and use the LuceneImplementation.java file provided as a part of Submission. 
	 B. Add the three following jars into your project's list of referenced libraries:
	    1. lucene-core-VERSION.jar
		2. lucene-queryparser-VERSION.jar
		3. lucene-analyzers-common-VERSION.jar
	C. Put all the corpus files inside the folder named 'Corpus'. My corpus is already present there.
	D. Run the java program.
	E. Enter the path of the parent directory of the 'Corpus' folder when you see the following prompt -- 'Enter the relative path from where you want to run the code: (e.g. /Usr/ or c:\\temp)'. The same path also contains the 'QueryFile.txt' having the list of queries.
	F. The program will generate the index for the corpus given to it and store the same in the folder named 'index' provided along with the submission. It will read the queries from 'QueryFile.txt', perform a search operation for the provided queries and store the search results for top 100 documents in 'Ranked_doc_list_Lucene.txt' file.
	
-- In order to run Task2, perform the following steps:
	  A. Open Windows PowerShell
	  B. Navigate to the directory having the programs.
	  C. Perform the following steps in order:
	     1. Put all the corpus files inside the folder named 'Corpus'. My corpus is already present there.
		 2. Run Task2.py using the command 'python Task1.py'. 
		 3. It will produce an inverted index first. Next, it will read the queries from 'QueryFile.txt' and for each query it will perform search operation and store the search results for top 100 documents in 'Ranked_doc_list_VSM.txt' file.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

DESIRED RESULTS:

-- The programs create the following output  
	1. Task1 after running successfully generates a ranked list of documents in the file 'Ranked_doc_list_Lucene.txt' using the Lucene System.
	2. Task2 after running successfully generates a ranked list of documents in the file 'Ranked_doc_list_VSM.txt' using the Vector Space Model.
	
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

MAP OF 'WHAT TO HAND IN' AND FILE NAMES:

ITEM 1 : README.txt
ITEM 2 : LuceneImplementation.java
		 Task2.py
ITEM 3 : Implementation_Report.txt
ITEM 4 : Ranked_doc_list_Lucene.txt
		 Ranked_doc_list_VSM.txt
ITEM 5 : Top5_SearchResultComparison.txt 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTRIBUTORS and CITATIONS:

-- Information Retrieval in Practice by Croft, Metzler, Strohman.
-- https://www.crummy.com/software/BeautifulSoup/ : BeautifulSoup has been used for extracting links from web pages
-- https://learnpythonthehardway.org/book/ : Python Programming
-- http://www.slideshare.net/dalal404/document-similarity-with-vector-space-model
-- http://nlp.stanford.edu/IR-book/html/htmledition/dot-products-1.html
-- http://nlp.stanford.edu/IR-book/html/htmledition/queries-as-vectors-1.html
-- https://www.elastic.co/guide/en/elasticsearch/guide/current/scoring-theory.html

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTACT DETAILS:

The author of the README can be contacted via:
Phone: (+1) 6173727648
E-Mail: nandi.t@husky.neu.edu