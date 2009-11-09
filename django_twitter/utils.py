import urllib, urllib2
import twitter

from django.conf import settings

from pressweb.tweet.models import TwitterAccount, get_twitter_password

def twitter_account(pk):
    twitter_account = TwitterAccount.objects.get(pk=pk)
    if twitter_account:
        twitter_password = get_twitter_password(settings.SECRET_KEY, twitter_account.password, decode=True)
        return twitter_account_raw(twitter_account.username, twitter_password)

def twitter_account_raw(username, password):
    return twitter.Api(username=username, password=password)

def verify_account(account):
    if account is None:
        return False
    url = 'http://twitter.com/account/verify_credentials.json'
    try:
        json = account._FetchUrl(url)
    except account._urllib.HTTPError:
        return False
    return True

def bitlify(url):
    import simplejson as json
    
    create_api = 'http://api.bit.ly/shorten'
    data = urllib.urlencode(dict(version="2.0.1", longUrl=url, login=settings.BITLY_LOGIN, apiKey=settings.BITLY_API_KEY))
    link = urllib2.urlopen(create_api, data=data).read().strip()
    
    return json.loads(link)["results"][url]["shortUrl"]