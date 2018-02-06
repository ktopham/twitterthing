from requests_oauthlib import OAuth1Session
import secrets
import json

def get_tweet_txt(tweet_list):
    text_lst = []
    for tweet in tweet_list:
        text_lst.append(tweet['text'])
    return text_lst

client_key = secrets.api_key
client_secret = secrets.api_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
tweets = json.loads(r.text)
#print(tweets['statuses'][0]['text'])
texts = get_tweet_txt(tweets['statuses'])
for t in texts:
    print(t)
