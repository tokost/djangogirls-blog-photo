from django.urls import re_path, path  # prec .conf a url nahradit re_path kvoli novsej verzii djanga 4.0.1
from django.views.generic import RedirectView # pridane kvoli Not Found: /favicon.ico

from . import views
								# url nahradit path. Je to dane verziou Djanga vyssou ako 2.
urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    re_path('register/', views.registerUser, name='register'),
    re_path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
#    re_path('', views.gallery, name='gallery'),
    re_path('gallery/', views.gallery, name='gallery'),     #  pridane kvoli kombinacii
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),  #  pridane kvoli kombinacii ale nie ako re_path
    path('add/', views.addPhoto, name='add'),   # pridane kvoli kombinacii
#    path('exit/', views.exit_app, name='add'),
]
