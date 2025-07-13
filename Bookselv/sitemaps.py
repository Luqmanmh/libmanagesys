from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Book, Folder

class StaticSitemap(Sitemap):
    def items(self):
        return ['blink', 'gverif', 'dev_page']
    
    def location(self, item):
        return reverse(item)
    
class BookSitemap(Sitemap):
    def items(self):
        return Book.objects.all()
    
    def location(self, item):
        return reverse('book_detail', args=[item.id])
    
class FolderSitemap(Sitemap):
    def items(self):
        return Folder.objects.all()
    
    def location(self, item):
        return reverse('online', args=[item.id])