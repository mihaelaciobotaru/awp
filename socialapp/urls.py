from django.conf.urls import url

from socialapp import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.EditPostView.as_view(),
        name='edit_post'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.DeletePostView.as_view(),
        name='delete_post'),
    url(r'^post/(?P<pk>\d+)/$', views.post_details, name='post_details'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profile/(?P<pk>\d+)', views.profile_view, name='profile_view'),
    url(r'^profile_edit/(?P<pk>\d+)', views.profile_edit, name='profile_edit'),
]
