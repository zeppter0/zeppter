from django import template

register = template.Library()

from myuser.models import MyUeers

@register.filter(name="user")
def user(id):
    return MyUeers.objects.get(pk=id).photo