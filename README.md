# Docker-Api-Project

The goal of this project is to analyze the conversations, I will use Bottle to create an API, and 
NLTK to make a sentiment analysisis.

For this project I use mongoDB atlas to store all my data. In the file connections.py, I stablish the connection to atlas. 
With the populate.py I create the chats database, with the chats.json from the input folder. I will during the project to test the API and the analisys.

The API has been made with bottle, the code is in api.py, there are 4 get functions and 3 post functions. 

One of this get functions get's the sentiment of a chat, provided by the user, using NLTK library, the code can be found in functions.py 