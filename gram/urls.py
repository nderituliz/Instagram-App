from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[

    url(r'', views.home_page),
    url(r'^profile/<str:username>', views.user_profile, name='userprofile'),
    url(r'^create/', views.create_profile, name='createprofile'),
    url(r'^uploads/',views.photo_upload,name='uploads'),

    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)