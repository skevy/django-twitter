from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

# from signals import post_to_twitter

import random, zlib, base64

def get_twitter_password(key, text, decode=False):
    rand = random.Random(key).randrange
    xortext = lambda text: "".join([chr(ord(c)^rand(256)) for c in text])
    if not decode:
        text = base64.encodestring(xortext(zlib.compress(text)))
    else:
        text = zlib.decompress(xortext(base64.decodestring(text)))
    return text


class TwitterAccount(models.Model):
    """
    Stores twitter accounts
    """
    username = models.CharField(_("username"), max_length=200, unique=True, null=False, blank=False)
    password = models.CharField(_("password"), max_length=200, null=False, blank=False)
    description = models.CharField(_("description"), max_length=200, help_text="One line description of this account")
    default_message = models.CharField(_("default message"), max_length=140, help_text="A default message to tweet if none is provided")

    def __unicode__(self):
        return self.username
    
    class Meta:
        verbose_name = _("twitter account")
        verbose_name_plural = _("twitter accounts")
        
    def get_password(self):
        return get_twitter_password(settings.SECRET_KEY, self.password, decode=True)

    def save(self):
        self.password = get_twitter_password(settings.SECRET_KEY, self.password)
        super(TwitterAccount, self).save()

# class Tweet(models.Model):
#     """
#     An object representing a Tweet for a particular object.
#     
#     Should be added as an inline to the admin of models you want to tweet
#     links to.
#     
#     example:
#     from django.contrib.contenttypes import generic
#     from pressweb.tweet.models import Tweet
# 
#     class TweetInline(generic.GenericTabularInline):
#         model = Tweet
#     """
#     
#     content_type = models.ForeignKey(ContentType)
#     object_id = models.PositiveIntegerField()
#     content_object = generic.GenericForeignKey('content_type', 'object_id')
#     
#     # accounts = models.ManyToManyField(TwitterAccount)
#     tweet = models.CharField(max_length=140, help_text="Please enter no more than 118 characters to allow room for a shortened link to this item.")
#     
#     # Timestamps
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_modified = models.DateTimeField(auto_now=True)
# 
#     class Meta:
#         ordering = ["-date_created",]
# 
#     def __unicode__(self):
#         return self.tweet
# 
#     @models.permalink
#     def get_absolute_url(self):
#         return ('Tweet', [self.id])
# 
# models.signals.post_save.connect(post_to_twitter, sender=Tweet)