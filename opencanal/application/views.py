from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'current_date': now})