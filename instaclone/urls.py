from django.conf.urls import url
from . import views
from  django.conf.urls import url
from django .conf import settings
from django.conf.urls.static import static



urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^accounts/profile/$',views.profile,name = 'profile'),
    url(r'^profile/(\d+)',views.other_profile,name = 'visitprofile'),
    url(r'^search/profile$', views.search, name='profileresults'),
    url(r'^timeline$', views.timeline, name='timeline'),
    url(r'^edit_profile$', views.edit_profile, name='edit'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)