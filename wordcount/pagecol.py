from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def about(request):
    return render(request,'aboutme.html')

def countpage(request):
    actualtext = request.GET['paragraph']
    divtext = actualtext.split()

    dicword = {}

    for word in divtext:
        if word in dicword:
            dicword[word] += 1
        else:
            dicword[word] = 1
    sortlist = sorted(dicword.items(), key=operator.itemgetter(1), reverse =True)
    return render(request,'countpage.html',{'wordlen':len(dicword),'divtext':divtext,'actualtext':actualtext,'dicword':dicword.items(),'sortlist':sortlist})
