import json 
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''


# Opening JSON file 
# returns JSON object as  
# a dictionary 
data = json.loads(f) 


  
# Iterating through the json 
def testOneWord():
    toSearch = 'Nicholas' 
   
   # for i in data: 
        #if (i['Word'] == toSearch.lower()):
           # print(i["Rank"])
  
toSearch1 = 'Sen. Susan Collins, Republican of Maine, congratulated President-elect Joe Biden on Monday, becoming only the third senator in her party to recognize his election.' 
toSearch3 = "There are at least 100 billion stars in the Milky Way, according to NASA estimates, of which about 4 billion are sunlike. If only 7 of those stars have habitable planets, there could be as many as 300 million potentially habitable Earths in our galaxy."
    
def calcScoreForTweet(toSearch):
    # New York Times Tweets on Novemer 9th, 2020

    no_punct = ""
    for char in toSearch.lower():
        if char not in punctuations:
            no_punct = no_punct + char

    splitCleanedInput = no_punct.split()

    hapTotal = 0
    wordCount = 0
    
    for word in splitCleanedInput:
        
        for i in data: 
            if (i['Word'] == word):
                #print(word)
                #print(i["Happiness Score"])
                wordCount += 1
                hapTotal += i["Happiness Score"]

    if wordCount == 0:
        return 0
    return(hapTotal/wordCount)


        



# Closing file 


"""
credit:
https://www.programiz.com/python-programming/examples/remove-punctuation

"""