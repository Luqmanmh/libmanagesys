from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book, Folder
from .forms import FileUploadForm
from django.http import HttpResponse
import os
import pdf2image
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from django.core.paginator import Paginator


def gverif(request):
    return render(request, "googlec1a42a4e2b9a75aa.html")

def index(request, file_root):
    infolder_all = Folder.objects.filter(parent_folder_id = file_root).order_by('folder_name')
    infile_all = Book.objects.filter(parent_folder_id = file_root).order_by('Title')

    if Folder.objects.get(pk = file_root).parent_folder is not None:
        par = Folder.objects.get(pk = file_root).parent_folder.id
    else:
        par = 1;
        
    pagdfold = Paginator(infolder_all, 50)
    foldpage = request.GET.get("folder_page")
    infolder = pagdfold.get_page(foldpage)
    
    pagdfile = Paginator(infile_all, 50)
    filepage = request.GET.get("file_page")
    infile = pagdfile.get_page(filepage)
    
    cont = {
        "infolder" : infolder, 
        "infile" : infile,
        "root" : file_root,
        "par" :  par
    }
    return render(request, 'online.html', cont)



def blink(request):
    return render(request, 'blink.html')
    # return redirect('online', file_root=1)


def check_admin(user):
   return user.is_superuser

@login_required(login_url='loginadm')
@user_passes_test(check_admin)
def manage(request, file_root):
    infolder = Folder.objects.filter(parent_folder_id = file_root).order_by("folder_name")
    infile = Book.objects.filter(parent_folder_id = file_root).order_by("Title")
    allfold = Folder.objects.exclude(pk = 1)
    
    if Folder.objects.get(pk = file_root).parent_folder is not None:
        par = Folder.objects.get(pk = file_root).parent_folder.id
    else:
        par = 1;
    form = FileUploadForm()

    cont = {
        "infolder" : infolder, 
        "infile" : infile,
        "root" : file_root,
        "form" : form,
        "par" : par,
        "allfold" : allfold
    }
    return render(request, 'manage.html', cont)


@login_required(login_url='loginusr')
def userpanel(request):
    if request.method == 'POST':
        uid = request.POST.get("uid")
        username = request.POST.get('username')
        email = request.POST.get('cemail')
        password = request.POST.get('cpass1')
        confirm_password = request.POST.get('cpass2')
        
        if not all([username, email, password, confirm_password]):
            messages.info(request, 'Please fill all fields')
            return redirect('userpanel')
        else: 
            if password == confirm_password:
                user = User.objects.get(pk=uid)

                if User.objects.filter(username=username).exclude(pk=uid).exists():
                    messages.info(request, 'Username taken')
                    return redirect('/userpanel/')

                elif User.objects.filter(email=email).exclude(pk=uid).exists():
                    messages.info(request, 'Email taken')
                    return redirect('/userpanel/')

                else:
                    user.username = username
                    user.email = email
                    user.set_password(password)
                    user.save()
                    messages.info(request, 'Edit successful')
                    login(request, user)
                    return redirect('online', file_root=1)
            else:
                messages.info(request, 'Password does not match')
                return redirect('/userpanel/')
    else:
        return render(request, 'userpanel.html')


# def loginusr(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('online', file_root=1)
#         else:
#             messages.error(request, "There was an error logging in. Please try again.")
#             return redirect('loginusr')
#     return render(request, 'login.html')



def loginadm(request):
    if request.method == "POST":
        username = request.POST['username']
        if username is None:
            messages.error(request, "Username cannot be empty")
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('manage', file_root=1)
            else:
                messages.error(request, "User is not an admin, use an admin account")
                return redirect('loginadm')    
        else:
            messages.error(request, "Username or Password is incorrect. Please try again.")
            return redirect('loginadm')
    return render(request, 'login_adm.html')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('cemail')
        password = request.POST.get('cpass1')
        confirm_password = request.POST.get('cpass2')
        
        if not all([username, email, password, confirm_password]):
            messages.info(request, 'Please Fill All FIeld')
            return redirect('register')
        else: 
            if password==confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, 'Register Successfull')
                    user.save()
                    return redirect('loginusr')
            else:
                messages.info(request, 'Password does not match')
                return redirect('register')  
    else:
        return render(request, 'register.html')
    
def dev_page(request):
    return render(request, "dev.html")



@login_required(login_url='loginadm')
def fileup(request, file_root):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            folder = Folder.objects.get(id=form.cleaned_data['folder'])
            filesv = Book.objects.create(
                Title=form.cleaned_data['title'],
                img=form.cleaned_data['file'],
                parent_folder=folder,
                writer=form.cleaned_data['writer'],
                publisher=form.cleaned_data['publisher'],
                ddc = form.cleaned_data['ddc'],
                count=form.cleaned_data['count'],
                synopsis=form.cleaned_data['synopsis'],
            )
            filesv.save()

            return redirect(f"/manage/f/{file_root}")
    else:
        form = FileUploadForm()

    # return render(request, 'manage.html', {'form': form})

@login_required(login_url='loginadm')
def fileedit(request, file_root, book_id):
    book = Book.objects.get(id=book_id)
    book.Title=request.POST.get('newtitle')
    book.writer=request.POST.get('newwriter')
    book.publisher=request.POST.get('newpublisher')
    book.ddc=request.POST.get('newddc')
    book.count=request.POST.get('newcount')
    book.synopsis=request.POST.get('newsyn')
    book.parent_folder=Folder.objects.get(pk = request.POST.get('newfk'))
    if request.FILES.get('newimg') is not None:
        book.img.delete()
        book.img=request.FILES.get('newimg')
    book.save()

    return redirect(f"/manage/f/{request.POST.get('newfk')}")


@login_required(login_url='loginadm')
def folderup(request, file_root):
    foldname = request.POST['foldname']
    
    par_folder = Folder.objects.get(pk=file_root)
    
    newfold = Folder.objects.create(folder_name = foldname, parent_folder = par_folder)
    newfold.save()
    return redirect("/manage/f/" + str(file_root))
        

      
def delete_file(request, pk):
    file_root = Book.objects.get(pk = pk).parent_folder.id
    file_obj = get_object_or_404(Book, pk=pk)
    
    # file_path = file_obj.file.path
    
    if file_obj.img:
        # file_obj.file.delete(save=False)
        file_obj.img.delete()
    
    file_obj.delete()
    
    return redirect("/manage/f/" + str(file_root))


def logoutusr(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('online', file_root=1)


    
# @login_required(login_url='loginusr')
# def download_file(request, pk):
#     file_obj = get_object_or_404(Book, pk=pk)
    
#     file_path = file_obj.file.path
    
#     with open(file_path, 'rb') as f:
#         response = HttpResponse(f.read(), content_type=file_obj.file_type)
#         response['Content-Disposition'] = f'attachment; filename={file_obj.filename+file_obj.file_type}'
#         return response

  
    
@login_required(login_url='loginadm')
def move(request, type, pk):
    newfk = request.POST['newfk']
    newname = request.POST['newname']
    
    if type == "file":
        file = Book.objects.get(pk = pk)

        file.parent_folder_id = newfk
        file.save()
        
    elif type == "folder":
        folder = Folder.objects.get(pk = pk)
        
        # folder.parent_folder_id = newfk
        folder.folder_name = newname
        folder.save()
        
    return redirect("/manage/f/" + str(newfk))



def delete_folder_contents(folder):
    if Book.objects.filter(parent_folder=folder) is not None:
        for file_obj in Book.objects.filter(parent_folder=folder):
            file_obj.img.delete()
            file_obj.delete()

    if Folder.objects.filter(parent_folder=folder) is not None:
        for subfolder in Folder.objects.filter(parent_folder=folder):
            delete_folder_contents(subfolder)

    folder.delete()



def delete_folder_and_contents(request, pk):
    root = Folder.objects.get(pk = pk).parent_folder.id
    folder = get_object_or_404(Folder, pk = pk)
    delete_folder_contents(folder)
    return redirect('/manage/f/' + str(root))



def search_file(request):
    quest = request.GET.get('quest', '')
    resi = []
    reso = []
    
    resi = Book.objects.filter(Title__icontains = quest)
    reso = Folder.objects.filter(folder_name__icontains = quest)
    
    cont = {
        "infolder" : reso,
        "infile" : resi,
        "query" : quest,
        "root" : 1
    }

    return render(request, 'manage.html', cont)   


def search_fileu(request):
    quest = request.GET.get('quest', '')
    resi = []
    reso = []
    
    resi = Book.objects.filter(Title__icontains = quest)
    reso = Folder.objects.filter(folder_name__icontains = quest)
    
    cont = {
        "infolder" : reso,
        "infile" : resi,
        "query" : quest,
        "root" : 1
    }

    return render(request, 'online.html', cont)


@login_required(login_url='loginusr')
def view_pdf(request, file_id):
    flsrc = get_object_or_404(Book, pk=file_id)
    file_path = flsrc.file.path  # Correctly handle the file path
    
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404("File not found")
    
def book_detail(request, id):
    book = Book.objects.get(pk = id)
    
    cont= {
        "book":book,
    }
    return render(request, 'bookdet.html', cont)