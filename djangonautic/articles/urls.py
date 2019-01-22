from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles_list/',views.article_list),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail)
    # path(r'admin/', admin.site.urls),
    # path(r'about/',views.about),
    #path('^$',views.about)
]
