import tweepy
import random
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate with Twitter (X)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#load affirmations from file
with open("affirmations.txt", 'r') as file:
    affirmations = [line.strip() for line in file if line.strip()]

    #pick a random affirmation
    affirmation = random.choice(affirmations)   
    api.update_status(affirmation)

    print("✅ Tweet sent:", affirmation)