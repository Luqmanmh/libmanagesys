from django import forms
from .models import Book, Folder

class FileUploadForm(forms.Form):
    title = forms.CharField(max_length=255, label="Judul")
    writer = forms.CharField(max_length=255, label="Penulis")
    publisher = forms.CharField(max_length=255, label="Penerbit")
    ddc = forms.CharField(max_length=10, label="DDC")
    count = forms.CharField(max_length=128, label="Jumlah")
    synopsis = forms.CharField(widget=forms.Textarea, label="Sinopsis")
    folder = forms.ChoiceField(choices=[], label="Kelas Buku")
    file = forms.FileField(label="Gambar")

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['folder'].choices = [(f.id, f.folder_name) for f in Folder.objects.all().exclude(folder_name="Home")]