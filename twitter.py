import oauth2 as oauth
import json

CONSUMER_KEY = "ak5NYDfYRqHl29gZ2nypeXBvi"
CONSUMER_SECRET = "Ddq8OkB24qtDh4BqLizTKEgLmfbpTMuyelRDspHGgM87LtSnOU"
ACCESS_KEY = "93727272-RxRhGxpy6oH0VY73mOBF0GrPsbj7R3nbbPBZewLjr"
ACCESS_SECRET = "JHK8xUN5o7phnt4qqBg0oFpSLs0h8op0WEmQkRmLryESJ"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/favorites/list.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']
