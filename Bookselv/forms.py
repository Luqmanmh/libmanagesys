from django import forms
from .models import Book, Folder

class FileUploadForm(forms.Form):
    title = forms.CharField(max_length=255, label="Judul")
    writer = forms.CharField(max_length=255, label="Penulis")
    publisher = forms.CharField(max_length=255, label="Penerbit", required=False)
    ddc = forms.CharField(max_length=10, label="DDC", required=False)
    count = forms.CharField(max_length=128, label="Jumlah", required=False)
    synopsis = forms.CharField(widget=forms.Textarea, label="Sinopsis", required=False)
    folder = forms.ChoiceField(choices=[], label="Kelas Buku", required=False)
    file = forms.FileField(label="Gambar", required=False)

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['folder'].choices = [(f.id, f.folder_name) for f in Folder.objects.all().exclude(folder_name="Home")]