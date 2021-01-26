from django.conf import settings
from django.urls import path,re_path
from django.conf.urls.static import static


from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search_results,name='search_results'),
    path('image/',views.add_image,name='upload_image'),
    path('profile/',views.profile_info, name = 'profile'),
    re_path('comment/(\d+)',views.comment,name = 'comment'),
    path('follow/(\d+)', views.follow, name = 'follow'),
    path('unfollow/(\d+)', views.unfollow, name='unfollow'),
    re_path('likes/(\d+)/', views.like_images,name='likes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)