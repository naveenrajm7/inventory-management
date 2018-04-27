from django.urls import path, re_path
from . import views
from accounts.views import login_view, logout_view, UserRegisterView
app_name = 'webapp'
urlpatterns = [
    re_path(r'^$', views.index, name= 'index'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'details'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('login/', login_view , name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('about/', views.about, name = 'about'),
    path('home/', views.HomeView.as_view(),name = 'home'),

    path('home/add', views.MasterInAdd.as_view(),name = 'master-add'),
    path('home/update', views.update_master, name = "master-update"),

    # /consum/add/
    path('consum/add/', views.ConsumInAdd.as_view(), name ='consum-add'),
    path('consum/', views.ConsumInView.as_view(), name ='consum'),

    path('issue/add/', views.IssueInAdd.as_view(), name ='issue-add'),
    path('issue/', views.IssueInView.as_view(), name ='issue'),

    path('whouse/add/', views.WhouseInAdd.as_view(), name ='whouse-add'),
    path('whouse/', views.WhouseInView.as_view(), name ='whouse'),
    re_path(r'^whouse/(?P<pk>[0-9]+)/$', views.WhouseInUpdate.as_view(), name ='whouse-update'),
    re_path(r'^whouse/(?P<pk>[0-9]+)/delete/$', views.WhouseInDelete.as_view(), name ='whouse-delete'),

    path('item/add/', views.ItemInAdd.as_view(), name ='item-add'),
    path('item/', views.ItemInView.as_view(), name ='item'),
    re_path(r'^item/(?P<pk>[0-9]+)/$', views.ItemInUpdate.as_view(), name ='item-update'),
    re_path(r'^item/(?P<pk>[0-9]+)/delete/$', views.ItemInDelete.as_view(), name ='item-delete'),
    # display fsn list
    path('fsn/', views.fast_moving, name = 'fsn'),
    path('reorder/', views.reorder, name = 'reorder')

]
