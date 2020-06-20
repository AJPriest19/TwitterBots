import tweepy
import datetime
import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("DxOOBKpfsfsZEtyUd7lYvyWGU", "HwGniIxaNLcG2nVR9EVf7V9uqJA2R8fXLrqRUO2roLI0B0jAPJ")
auth.set_access_token("1274342046011133952-SxcLDs2vRv5GYk0ugfQsaQN5tlMzea", "ybs3Jc4jhHrEc47tY81o6iL46Qx8ZEP96BoPFb98wDHBx")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create a tweet
api.update_status("Test")

#email: onvohlnckemnnxhfkf@ttirv.org
#pw: BigChungus123
