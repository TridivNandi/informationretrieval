Assignment 2:
Goal: Link Analysis and PageRank Implementation

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has references and detailed information regarding how to setup, compile and run the programs in the assignment.
The tasks are discussed below in brief:
-- Task1: Obtaining directed web graphs
		A. Building our own: Build a graph for the 100 URLs that we have crawled in HW1-Task1 by following their links and their corresponding in-link relationship. This graph is in the file 'G1_Graph.txt'
	    B. Using existing ones: Download the in-links file for the WT2g collection. The graph is in the file 'G2_Graph.txt'
-- Task2: Implementing and running PageRank 
		A. Implementation of the PageRank algorithm using the pseudo code provided. The code can be found in 'PageRankImpl.py' file.
		B. Execution of the iterative version of the PageRank algorithms on the two above-mentioned graphs respectively until their PageRank values "converge". To test for convergence, calculate the perplexity of the PageRank distribution using the formulae provided. 
-- Task3: Qualitative Analysis 
		Examination of the top 5 pages by PageRank and Top 5 by in-link counts for the above-mentioned graphs. Detailed speculation regarding why these pages have high PageRank values.

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
-- Run the program by using the command 'python <File_Name>.py'

OR

-- Navigate to the directory having the programs
-- Double click on the <FileName>.py file to run the program.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

DESIRED RESULTS:

-- The program prints in the console the following things in order:
	1. The perplexity values for each iteration
	2. The top 50 pages by their DOC ID and PageRank Score for the graph provided
	3. The top 5 pages as per their in-link counts for the graph provided
	4. Overall statistics for the graph displaying the total number of pages, total number of sinks and total number of sources for 
	the input graph.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

MAP OF 'WHAT TO HAND IN' AND FILE NAMES:

ITEM 1 : PageRankImpl.py
ITEM 2 : README.txt
ITEM 3 : G1_Graph.txt
ITEM 4 : Statistical_Report.txt
ITEM 5 : PerplexityValues_G1_Graph.txt
ITEM 6 : PerplexityValues_G2_Graph.txt
ITEM 7 : Top50PageRanks_G1_Graph
ITEM 8 : Top50PageRanks_G2_Graph
ITEM 9 : Task3_Speculation.txt

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTRIBUTORS and CITATIONS:

-- https://www.crummy.com/software/BeautifulSoup/ : BeautifulSoup has been used for extracting links from web pages
-- https://www.udacity.com/course/intro-to-computer-science--cs101 : Basics of Python Programming and web crawling
-- https://learnpythonthehardway.org/book/ : Python Programming

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTACT DETAILS:

The author of the README can be contacted via:
Phone: (+1) 6173727648
E-Mail: nandi.t@husky.neu.edu