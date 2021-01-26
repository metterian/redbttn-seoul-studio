from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime,timedelta
from homepage.models import InstaData





def homepage(request):
    photo_list = list(InstaData.objects.all())

    for number in range(1,10):
        globals()['photo{}'.format(number)] = photo_list[(number-1)]

    context = {'photo1': photo1,
               'photo2': photo2,
               'photo3': photo3,
               'photo4': photo4,
               'photo5': photo5,
               'photo6': photo6,
               'photo7': photo7,
               'photo8': photo8,
               'photo9': photo9,

               }
    return render(request, 'index.html', context)



