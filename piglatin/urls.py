from django.conf.urls import url
from django.contrib import admin
### NEED THE VIEWS WE HAVE CREATED ###
# Views are just functions that return HttpResponses
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^translate/', views.translate, name="translate"),
    url(r'^about/', views.about, name="about")
]
