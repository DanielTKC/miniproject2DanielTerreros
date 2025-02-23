"""

INF601 - Programming in Python

Assignment # Mini Project 2
I, Daniel Terreros, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance
and have accurately cited all sources in adherence to academic standards. I understand that failing to
comply with this integrity statement may result in consequences, including disciplinary actions as
determined by my course instructor and outlined in institutional policies. By signing this statement, I
acknowledge my commitment to upholding the principles of academic integrity.

"""
import os
import pandas as pd
from collections import Counter

import matplotlib.pyplot as plt

# Create charts directory if it doesn't exist
os.makedirs("charts", exist_ok=True)

#Ignore common words
ignore_words = {
    "a", "an", "at", "in", "on", "of", "the", "with", "by", "and", "or", "but", "to", "&",
    "my", "for", "i", "you", "-"
}


 #Get the titles
netflix_titles = pd.read_csv("netflix_titles.csv", index_col=0)

# Get all the words from titles
all_words = []
for title in netflix_titles["title"]:
    words = str(title).lower().split()
    all_words.extend([word for word in words if word not in ignore_words])

#Count the word frequency and return the 10 most common
word_counts = Counter(all_words)
most_common = word_counts.most_common(10)

print(most_common)