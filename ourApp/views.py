from django.shortcuts import render
import datetime
from  ourApp.models import News
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'index.html', {})

#def time(request):
#	return render(request, 'time.html', {'current_date':datetime.datetime.now()})
#
#def dtime(request, offset):
#	return render(request, 'dtime.html', {'date':(datetime.datetime.now()+datetime.timedelta(hours=offset)), 'hours':offset})
@login_required
def news(request):
	return render(request, 'news.html', {'News':News.objects.filter(viewer = request.user)})

def accounts(request):
	return render(request, 'accounts.html', )