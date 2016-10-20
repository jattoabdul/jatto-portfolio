from django.conf.urls import url
from django.conf.urls import include
from jatto import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^resume/', views.resume, name='resume'),
    url(r'^contact/', include('contact_form.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^portfolio/', include('work.urls')),
]