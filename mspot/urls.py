from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'mspot'
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<slug:category_slug>/', views.movie_list, name='movie_list_by_gatunek'),
    path('<int:id>/<slug:slug>/', views.movie_detail, name='movie_detail'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
