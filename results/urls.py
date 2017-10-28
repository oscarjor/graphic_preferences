from django.conf.urls import include, url
from results import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^results/', views.index, name='index'),
    url(r'^getresults/', views.getresults, name='getresults'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)