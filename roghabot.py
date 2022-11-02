import tweepy
from urllib.request import urlopen

#must have a separate file which contains all necessary keys
from keys import my_consumer_key 
from keys import my_consumer_secret 
from keys import my_access_token 
from keys import my_access_token_secret 
from keys import my_bearer_token 
from keys import client_id 
from keys import client_secret 

try:
    client=tweepy.Client(consumer_key=my_consumer_key, consumer_secret=my_consumer_secret, access_token=my_access_token, access_token_secret=my_access_token_secret)
    print("authentican success")
except:
    print("authentication failed")


def get_article():

    # Ag fáil an leathanach Vicipéid

    page = urlopen('https://ga.wikipedia.org/wiki/Speisialta:Random')
    vici_url = page.geturl()
    content = page.read().decode("utf8")

    title = content.split("<title>")[1].split(" - Vicipéid</title>")[0]


    return(title, vici_url)



def main():

    while True:

      #retrieving the two topics
        topaic1, url1 = get_article()
        topaic2, url2 = get_article()

        #constructing the sentence to be tweeted out
        ceist = str(topaic1 + " nó " + topaic2 + "?")

        #tweet the poll
        try:
            poll_tweet = client.create_tweet(text=ceist, poll_duration_minutes=1440, poll_options=[topaic1,topaic2])
            response1 = client.create_tweet(text=url1, in_reply_to_tweet_id=poll_tweet.data["id"])
            client.create_tweet(text=url2, in_reply_to_tweet_id=response1.data["id"])
            print("Poll success")
            break
        except:
            print("Poll failure")

if __name__ == "__main__":

    main()







