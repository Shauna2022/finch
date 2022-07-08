from django.shortcuts import render
from .models import Finch


def about(request):
  return render(request, 'about.html')

def Finchs_index(request):
  Finchs = Finch.objects.all()
  return render(request, 'Finchs/index.html', { 'Finchs': Finchs })

def finchs_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finchs/detail.html', { 'finch': finch })