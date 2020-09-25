"""
Create By - Avijit Samanta
Date - 25/09/2020

Problem Statement:- You are given few sentences as a list (Python list of sentences). Take a query string as an input
from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of
relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one
with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool
"""


def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    sc = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                # print(f"Matching {word1} with {word2}")
                sc += 1
    return sc


if __name__ == '__main__':
    # print(matchingWords("This is good", "Python is good"))
    sentences = ["Python is good", "This is snake", "Avijit is a good boy", "Subscribe my youtube channel"]
    query = input("Please enter the query string\n")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)]
    # print(sortedSentScore)
    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f"\"{item}\": with a score of {score}")

    # a = [1, 3, 2]
    # b = [4, 5, 6]
    # print(sorted(zip(a, b)))
