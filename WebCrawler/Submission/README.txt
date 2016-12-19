Assignment 1:
Goal: Implementing your own web crawler. Perform focused crawling

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SYNOPSIS:

This readme file has references and detailed information regarding how to setup, compile and run the programs in the assignment.
The progrms are discussed below in brief:
-- Task1: A web crawler that starts from the following seed URL "https://en.wikipedia.org/wiki/Sustainable_energy" and crawls upto depth 5 or  maximum of 1000 unique URLs. Pages in a shallower depth are more important than deeper ones, also within each individual page, hyperlinks appearing earlier on the webpage should be crawled first.
-- Task2: The web crawler should be able to consume two arguments: a URL and a keyword to be matched against anchor text or text within a URL. It starts with the seed URL "https://en.wikipedia.org/wiki/Sustainable_energy" and crawls to a depth 5 at most using the keyword "solar". It should return at most 1000 URLs for each of the following:
	A: Breadth first crawling
	B: Depth first crawling
-- Task3: Repetation of the Task1 using the seed "https://en.wikipedia.org/wiki/Solar_power"

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

-- The program creates a file named 'crawled_urls' which lists all the URLs that has been crawled.
-- The contents of all webpages that has been crawled are stored in individual files along with their URLs.
-- The files are created in the same directory where we have the program.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTRIBUTORS and CITATIONS:

-- https://www.crummy.com/software/BeautifulSoup/ : BeautifulSoup has been used for extracting links from web pages
-- https://www.udacity.com/course/intro-to-computer-science--cs101 : Basics of Python Programming and web crawling
-- https://learnpythonthehardway.org/book/ : Python Programming

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTACT DETAILS:

The author of the README can be contacted via:
Phone: (+1) 6173727648
E-Mail: nandi.t@husky.neu.edu