from django.contrib import admin
from models import TwitterAccount
from forms import TwitterForm
from django import forms as django_forms
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.forms.util import flatatt
from django.utils.encoding import force_unicode

# from pressweb.core.admin import PressWebGenericStackedInline

# class Twidget(django_forms.Textarea):
#     def __init__(self, attrs=None):
#         # The 'rows' and 'cols' attributes are required for HTML correctness.
#         self.attrs = {'cols': '40', 'rows': '10'}
#         if attrs:
#             self.attrs.update(attrs)
# 
#     def render(self, name, value, attrs=None):
#         if value is None: value = ''
#         value = force_unicode(value)
#         final_attrs = self.build_attrs(attrs, name=name)
#         return mark_safe(u'<textarea%s>%s</textarea> <strong id="status-field-char-counter" class="char-counter">118</strong>' % (flatatt(final_attrs),
#                 conditional_escape(force_unicode(value))))
# 
# class TweetForm(django_forms.ModelForm):
#     
#     tweet = django_forms.CharField(widget=Twidget(attrs={'class':'tweet', 'rows': '2', 'cols': '40',}), help_text="Please enter no more than 118 characters to allow room for a shortened link to this item.")
#     
#     class Media:
#         js = (
#         '/media/static/js/jquery-1.3.2.js',
#         '/media/static/js/twitter_count.js',
#         '/media/static/js/section-delete.js',
#         # '/media/static/js/section-add.js',
#         )
#         
# # class TweetInline(PressWebGenericStackedInline):
# #     model = Tweet
# #     form = TweetForm
# #     template = "admin/edit_inline/tweet_inline.html"
# #     extra = 1
# #         
# #     def formfield_for_manytomany(self, db_field, request=None, **kwargs):
# #         """
# #         Restrict the networks field to showing only networks this user can access.
# #         This overrides the formfield_for_manytomany provided by PressWebAdmin.
# #         """
# #         
# #         if request and db_field.name == 'accounts' and not request.user.is_superuser:
# #             editing_networks = request.user.get_profile().editing_networks.values_list('id', flat=True)
# #             kwargs['queryset'] = TwitterAccount.objects.filter(network__id__in=editing_networks)
# # 
# #         return super(TweetInline, self).formfield_for_manytomany(db_field, **kwargs)

class TweetAdmin(admin.ModelAdmin):
    form = TwitterForm
    list_display = ('username', 'description')
    
admin.site.register(TwitterAccount, TweetAdmin)
# admin.site.register(Tweet)
