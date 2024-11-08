from lib2to3.fixes.fix_input import context

from django.shortcuts import render

memberss = [
    {'id':1, 'name': 'Liza Loik'},
    {'id': 2, 'name': 'Kirill'},
    {'id': 3, 'name': 'Dima'},
    {'id': 4, 'name': 'Serega'},
    {'id': 5, 'name': 'Valera'},
]



def home(request):
    return render(request, 'mytest/home.html', )

def members(request):
    context = {'memberss':memberss}
    return render(request, 'mytest/members.html', context)

def mem(request, pk):
    mem = None
    for m in memberss:
        if m['id'] == int(pk):
            mem = m
    context1 = {'mem': mem}
    return render(request, 'mytest/mem.html', context1)
# Create your views here.
