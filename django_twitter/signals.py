import twitter
import urllib2
from django_bitly.models import Bittle
from django.core.urlresolvers import reverse
from django_twitter.models import TwitterAccount

def post_to_twitter(sender, instance, **kwargs):
    """ 
    Post new saved Tweet objects to Twitter.
    """

    if instance.pk: #only post the tweet if it's a new record. 
        return False 
    
    accounts = TwitterAccount.objects.all()
    
    for account in accounts:
        bittle = Bittle.objects.bitlify(instance.get_absolute_url())
        mesg = "%s: %s" % ("New Blog Post", bittle.shortUrl)
        username = account.username
        password = account.get_password()
        try:
           twitter_api = twitter.Api(username, password)
           twitter_api.PostUpdate(mesg)
        except urllib2.HttpError, ex:
           print str(ex)
           return False