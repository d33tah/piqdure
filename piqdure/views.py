from django.http import HttpResponse
import django.template
from piqdure.models import Url
from django.db.models import Q
from django.shortcuts import render_to_response

question_mark_png = """
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciDQp4bWxuczp4bGluaz0iaHR0
cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgDQp3aWR0aD0iMjIwcHgiIGhlaWdodD0iMzg1cHgi
Pg0KPHRleHQgZm9udC1zaXplPSI1MDAiIHk9IjM2MCIgZm9udC1mYW1pbHk9IlRpbWVzIE5ldyBS
b21hbiI+PzwvdGV4dD4NCjwvc3ZnPg0K
"""

def main(request):
    return HttpResponse("""
  <FRAMESET rows="10, 200">
      <FRAME src="/upperbar">
      <FRAME src="/pics">
  </FRAMESET>
    """)

def pics(request):
    our_ip = request.META['REMOTE_ADDR']
    our_pics = list(Url.objects.filter(Q(ip__exact=our_ip)).order_by('-number')[:4])
    placeholder_url = Url()
    placeholder_url.url = "data:image/svg+xml;base64," + question_mark_png.replace('\n', '')
    if len(our_pics) < 4:
        our_pics += [placeholder_url] * (4 - len(our_pics))
    their_pics = list(Url.objects.filter(~Q(ip__exact=our_ip)).order_by('-number')[:4])
    if len(their_pics) < 4:
        their_pics += [placeholder_url] * (4 - len(their_pics))
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
