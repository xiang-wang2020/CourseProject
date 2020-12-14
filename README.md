# Video Demo
https://drive.google.com/file/d/1X6JIXAFP2zzAArOhJZVI2y-YqfIeZ-SR/view?usp=sharing

# How to set up:
1. download the package to your local computer
2. open a terminal and move into the folder
3. run "pip install -r packages.txt"
4. run python start.py
5. go to http://127.0.0.1:5000/ in your browser

# What does it do:
The goal is to replicate ExpertSearch System, a course project built by former CS410 students (Original Link: http://timan102.cs.illinois.edu/expertsearch//#). The essential function is to search and display ranked information of faculties from many universities. The algorithm behind ExpertSearch is relevance ranker. In this version, I used cosine similarity to rank the documents. The documents are turned into vectors, following the guidance of tf*idf algorithm, and ranked based on how similar they are from the query. Meanwhile, you are able to set up the must-include and must-exclude keywords and set up the number of results you want to see.

# Introduce my files:
Most of the data cleaning and processing work is in process.py.
start.py handles the backend, and templates/index.html handles the frontend. The search result will be displayed by templates/result. html. faculties.py includes 999 lines of crawled data from different universities, and every line is one section/person. testcase.txt includes some sample testcases for the grader.

