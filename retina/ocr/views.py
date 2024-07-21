from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import RegistrationForm, PostDocument
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Document
from .parse import parse_pdf
# Create your views here.


@login_required(login_url="/login")
def upload(request):

    if request.method == 'POST':
        # you basically access the dictionary of requests.FILES and the key that you pass is the name you assign to the input tag on the html
        form = PostDocument(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.author = request.user
            document_path = document.document.path  # get the path of the document

            document.save()
            return redirect('/document_view')
    else:
        form = PostDocument()

    context = {
        "form": form,
    }

    return render(request, 'ocr/upload.html', context)


@login_required(login_url="/login")
def home(request):
    return render(request, 'ocr/home.html')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/upload')
    else:
        form = RegistrationForm()

    context = {
        "form": form,
    }

    return render(request, 'registration/signup.html', context)


@login_required(login_url="/login")
def view_document(request):  # view where the user will see
    user = request.user
    try:
        document = Document.objects.filter(author=user).latest('created_at')
        # Use 'file' instead of 'document' if 'file' is your FileField name
        document_path = document.document.path
        corpus = document.corpus = parse_pdf(document_path)

        context = {
            "document_path": document_path,
            "corpus": corpus,  # Including corpus if needed
        }
    except Document.DoesNotExist:
        context = {
            "error": "No document found for this user."
        }

    return render(request, 'ocr/document_view.html', context)
