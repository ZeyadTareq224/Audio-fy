from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import AudibleForm
from .models import Audible

import PyPDF2
import gtts
import shutil



def pdf_to_audio(book, page_number, filename):
    #read the desired pdf
    bookToRead = open(book, 'rb')
    fileReader = PyPDF2.PdfFileReader(bookToRead)
    #generate txt out of pdF
    pageToRead = fileReader.getPage(page_number)
    txt = pageToRead.extractText()
    tts = gtts.gTTS(txt)
    tts.save(f"{filename}_page{page_number}.mp3")
    shutil.move(f'{filename}_page{page_number}.mp3', f"static/media/audios/{filename}_page{page_number}.mp3")


# Create your views here.
def home(request):
    form = AudibleForm(request.POST)

    if request.method == "POST" and request.user.is_authenticated:
        form = AudibleForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()

            return redirect('saved-pdfs')
    context = {'form': form}
    return render(request, 'core/home.html', context)

    
def FAQ(request):
    return render(request, 'core/FAQ.html')



@login_required(login_url='/')
def convert_pdf_to_audio(request, pk):
    fileToConvert = Audible.objects.get(id=pk)
    page_number = int(fileToConvert.page)
    try:
        print("passs")
        pdf_to_audio(fileToConvert.book.path, page_number, fileToConvert.book)
        print("passs")
        fileToConvert.is_converted = True
        print("passs")
        fileToConvert.save()
        print("passs")

    except:
        return HttpResponse("sorry this page is not convertable")
    return redirect('history')


@login_required(login_url='')
def history(request):
    audios = Audible.objects.filter(author=request.user, is_converted=True)
    print(audios)
    context = {'audios': audios}
    return render(request, 'core/history.html', context)


@login_required()
def saved_pdfs(request):
    pdfs = Audible.objects.filter(author=request.user, is_converted=False)# unconverted pdfs
    context = {'pdfs': pdfs}
    return render(request, 'core/saved_pdfs.html', context)


@login_required()
def delete_pdf(request, pk):
    pdfToDelete = Audible.objects.get(id=pk)
    if request.method == "POST":
        pdfToDelete.delete()
        return redirect('saved-pdfs')
    context = {'pdf': pdfToDelete}
    return render(request, 'core/delete_pdf.html', context)    