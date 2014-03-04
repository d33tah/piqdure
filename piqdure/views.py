from django.http import HttpResponse
import django.template
from piqdure.models import Url
from django.db.models import Q
from django.shortcuts import render_to_response

def main(request):
    return HttpResponse("""
  <FRAMESET rows="10, 200">
      <FRAME src="/upperbar">
      <FRAME src="/pics">
  </FRAMESET>
    """)
def pics(request):
    our_ip = request.META['REMOTE_ADDR']
    our_pics = Url.objects.filter(Q(ip__exact=our_ip))[:4]
    their_pics = Url.objects.filter(~Q(ip__exact=our_ip))[:4]
    return render_to_response('main.html', {'our_pics': our_pics, 'their_pics': their_pics})

def upperbar(request):
    url = request.POST.get('url', None)
    our_ip = request.META['REMOTE_ADDR']
    if url:
        obj = Url()
        obj.url = url
        obj.ip = our_ip
        obj.save()
    html = '<form method="post"><input name="url"/></form>'
    return HttpResponse(html)
