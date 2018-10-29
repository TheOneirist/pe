"""
Name: Chris Mankos
Date: 9/18/2018

Purpose:
To implement a simple markov chain generator that takes in Dr. Seuss books
and attempts to spit out sentences in his style

Input:
.txt files

Output:
To the console? Undecided the best method. How to rate and award? Undecided

"""

"""
http://www.jmlr.org/papers/volume12/collobert11a/collobert11a.pdf
What can I use from paper? Undecided. They have vast amounts of data
I think. I only want to use specific examples, not all of Oxford dic.
Come back to after a deeper read.

Broad strokes, 3 working pieces:
    Parsing the input
    Classifying the input
    Mathmagicking into output
"""


# PARSING INPUT

# Opens a file and feeds it to functions that analyze it
def parser():

    grinchFile = open("grinch.txt", 'r') # Read from the .txt file in same dir
    grinchList = grinchFile.readlines() # turn .txt into list
    grinchFile.close() # no longer need the grinch file

    clean(grinchList)

# Strips away capitalization.
# COME BACK TO - also want it to strip punctuation.
# COME BACK TO - want to make it mark beginning of sentences
def clean(pList):
    cleanList = [l.upper() for l in pList]
    return cleanList



