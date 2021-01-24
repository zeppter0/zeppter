from django.http import HttpResponse
from django.template.loader import get_template

import speech_recognition as sr


def robots(request):



    return HttpResponse(request, get_template("include/robot.txt"))