from django.conf.urls import url
from . import views
from  django.conf.urls import url
from django .conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView 



urlpatterns =[
    url('^$',views.index,name='index'),
    url('accounts/profile/',views.profile,name = 'profile'),
    url('profile/(\d+)',views.other_profile,name = 'visitprofile'),
    url('search/profile', views.search, name='profileresults'),
    url('timeline', views.timeline, name='timeline'),
    url('update_profile', views.update_profile, name='update'),
    # url('logout/', views.LogoutView.as_view(), {"next_page": '/'}),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
