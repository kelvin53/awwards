from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^edit/profile$',views.edit_profile,name='edit-profile'),
    url(r'^awards/', views.rate, name='awards'),

    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^projectdetails/(\d+)',views.projectdetails,name ='projectdetails'),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
