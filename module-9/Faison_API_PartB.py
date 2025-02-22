#DeJanae Faison 2/23/2025 Assignment 9.2 APIs
#Selected API

#import API request
import requests
#import json
import json

#get the url and set it to a variable
response = requests.get('https://www.dnd5eapi.co/api/monsters/adult-black-dragon/')

#print the status code and view the data in the json file
print(response.status_code)
#print(response.json())

#function to format 
def jsonPrint(obj):
    text = json.dumps(obj, sort_keys=True,indent=4)
    print(text)

jsonPrint(response.json())

#Sources:
#Custer, C. (2024, December 5). How to Use an API in Python – Dataquest. Dataquest. https://www.dataquest.io/blog/api-in-python/
