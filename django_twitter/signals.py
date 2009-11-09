import twitter
import urllib2
from django_bitly.models import Bittle
from django.core.urlresolvers import reverse

def post_to_twitter(sender, instance, *args, **kwargs):
    """ 
    Post new saved Tweet objects to Twitter.
    """
    
    # avoid to post the same record twice
    if not kwargs.get('created'):
        return False
        
    content_object = instance.content_object
    if hasattr(content_object, 'network'):
        networks = [content_object.network]
    elif hasattr(content_object, 'networks'):
        networks = content_object.networks.all()
    else:
        return False
        
    # create the twitter message
    mesg = str(instance.tweet).decode('utf-8')

    for network in networks:
        if not network.twitter:
            continue
        
        # get url to link to
        if not hasattr(instance.content_object, 'get_absolute_url'):
            # For now we're assuming any object without a get_absolute_url is
            # a PressRelease. Will probably want to make this more flexible in
            # the future.
            content_object = reverse('release-detail', kwargs={
                'region_slug': network.region.slug,
                'network_slug': network.slug,
                'year': instance.content_object.start_date.year,
                'slug': instance.content_object.slug}
            )
        bittle = Bittle.objects.bitlify(content_object)
        mesg = "%s %s" % (instance.tweet, bittle.shortUrl)
            
        
        # twitter account information
        username = network.twitter.username
        password = network.twitter.get_password()
        
        try:
            twitter_api = twitter.Api(username, password)
            twitter_api.PostUpdate(mesg)
        except urllib2.HttpError, ex:
            print str(ex)
            return False
