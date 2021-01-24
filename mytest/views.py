from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import NameForm

import speech_recognition as sr
# Create your views here.


def imageupload(request):
    if request.method in "POST":
        print(sr.__version__)
        r = sr.Recognizer()

        file_audio = sr.AudioFile('mytest/fev.mp3')

        with file_audio as source:
            audio_text = r.record(source)

        print(type(audio_text))
        print(r.recognize_google(audio_text))
        return HttpResponse(r.recognize_google(audio_text))



  
    return render(request,"test/cemera.html")
