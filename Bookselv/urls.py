from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

sitemaps = {
    'static': StaticSitemap(),
    'books': BookSitemap(),
    'folders': FolderSitemap(), 
}

urlpatterns = [
    path('', views.blink, name='blink'),
    path('googlec1a42a4e2b9a75aa.html', views.gverif, name='gverif'),
    path('collection/<int:file_root>', views.index, name='online'),
    # path('login/', views.loginusr, name='loginusr'),
    path('login/', views.loginadm, name='loginadm'),
    # path('register/', views.register, name='register'),
    path('logoutusr/', views.logoutusr, name='logoutusr'),
    # path('userpanel/', views.userpanel, name='userpanel'),
    path('manage/f/<int:file_root>', views.manage, name='manage'),
    path('uploadfile/<int:file_root>', views.fileup, name='fileupload'),
    path('createfolder/<int:file_root>', views.folderup, name='createfolder'),
    # path('download/<int:pk>/', views.download_file, name='download'),
    path('deletefile/<int:pk>', views.delete_file, name='deletefile'),
    path('deletefold/<int:pk>', views.delete_folder_and_contents, name='deletefold'),
    path('move/<str:type>/<int:pk>/', views.move, name='move'),
    path('fileedit/<int:file_root>/<int:book_id>/', views.fileedit, name='fileedit'),
    path('manage/s/', views.search_file, name='search'),
    path('collection/s/', views.search_fileu, name='searchon'),
    path('developer', views.dev_page, name='dev_page'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="sitemap"),
    path('robots.txt', TemplateView.as_view(template_name = "robots.txt", content_type = "text/plain")),
    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += staticfiles_urlpatterns()
