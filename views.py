from django.shortcuts import render
from ddl.models import autocomplete

def autosearch(request):
    result=autocomplete.objects.all()
    return render(request,'index.html',{"autocomplete":result})
