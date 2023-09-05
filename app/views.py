from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_webpage(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    if request.method=='POST':
        tn=request.POST['to']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        QSWO=Webpage.objects.all()
        a={'QSWO':QSWO}
        return render(request,'display_webpage.html',a)
        
    return render (request,'insert_webpage.html',d)