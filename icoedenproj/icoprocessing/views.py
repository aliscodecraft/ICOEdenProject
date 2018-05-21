from datetime import datetime
from datetime import datetime
from pytz import UTC
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from . import forms
from . import models

def process_ico_form(request):

    if request.method =='GET':
        icoform = forms.ICOForm()

        return render(request, 'icoprocessing/icoform.html', {'form': icoform})

    else:
        icoform = forms.ICOForm(request.POST)
        print (icoform)
        if icoform.is_valid():
            print ('valid')
        else:
            print('not valid')

        print (icoform.cleaned_data)
        return render(request, 'icoprocessing/icoform.html', {'form': icoform})



def process_ico_form1(request):
    if request.method == 'POST':

        DATE_TIME_FORMAT = 'YYYY-MM-DD HH'

        icoform = forms.ICOForm(request.POST)

        if icoform.is_valid(): #Validation de l'ensemble des champs du formulaire.

            icoform.save()


        #return render(request, 'icoprocessing/icoform.html', {'form': icoform})
        return HttpResponseRedirect('/ico/icoform')
    else:
        icoform = forms.ICOForm()

        return render(request, 'icoprocessing/icoform.html', {'form': icoform})








