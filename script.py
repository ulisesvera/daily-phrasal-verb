
# Library imports
import json 
from pprint  import pprint
import random
import cgitb

cgitb.enable()
#import web

def getRandomVerb(a,b):
    try:
        # We get the json file content (phrasal verbs)
        with open('phrasal_verbs.json') as dataFile:
            phrasalVerbs = json.load(dataFile)

        # We get a random position to get the daily phrasal verb
        #for x in range(len(phrasalVerbs)):
        #    randomPosition = random.randint(0,len(phrasalVerbs))
        randomPosition = random.randint(0,len(phrasalVerbs))

        # Now, we have the choosen item
        #print("Content-Type: javascript/json")
        print(phrasalVerbs[randomPosition])
        #web.header('Content-Type', 'application/json')
        return json.dumps(phrasalVerbs[randomPosition])
    except ValueError:
        print("Ups, there is an error: ",ValueError)

#getRandomVerb()
