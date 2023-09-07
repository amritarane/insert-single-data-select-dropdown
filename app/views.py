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


def select_display(request):
    QSDO=Topic.objects.all()
    d={'QSDO':QSDO}
    if request.method=='POST':
        tnlist=request.POST.getlist('to')
        print(tnlist)
        QSWO=Webpage.objects.none()
        
        for tn in tnlist:
            QSWO=QSWO | Webpage.objects.filter(topic_name=tn)
    
        a={'QSWO':QSWO}
        return render(request,'display_webpage.html',a)
    
    return render (request,'select_display.html',d)



def checkbox(request):
    QSDO=Topic.objects.all()
    d={'QSDO':QSDO}
    
    return render(request,'checkbox.html',d)

def radio(request):
    
    QSDO=Topic.objects.all()
    d={'QSDO':QSDO}
    
    return render(request,'radio.html',d)