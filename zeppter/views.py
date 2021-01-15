from django.http import HttpResponse
from django.template.loader import get_template


def robots(request):
    return HttpResponse(request, get_template("include/robot.txt"))