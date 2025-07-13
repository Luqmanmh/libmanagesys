from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Book, Folder

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    
    def items(self):
        return ['blink', 'gverif', 'dev_page', "robots"]
    
    def location(self, item):
        return reverse(item)
    
class BookSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'
    
    def items(self):
        return Book.objects.all()
    
    def location(self, item):
        return reverse('book_detail', args=[item.id])
    
class FolderSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'
    
    def items(self):
        return Folder.objects.all()
    
    def location(self, item):
        return reverse('online', args=[item.id])