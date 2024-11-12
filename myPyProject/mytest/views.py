from lib2to3.fixes.fix_input import context
from .models import Member, Project
from django.shortcuts import render

# memberss = [
#     {'id':1, 'name': 'Liza Loik'},
#     {'id': 2, 'name': 'Kirill'},
#     {'id': 3, 'name': 'Dima'},
#     {'id': 4, 'name': 'Serega'},
#     {'id': 5, 'name': 'Valera'},
# ]



def home(request):
    return render(request, 'mytest/home.html', )

def members(request):
    memberss = Member.objects.all()
    context = {'memberss':memberss}
    return render(request, 'mytest/members.html', context)

def mem(request, pk):
    mem = Member.objects.get(id=pk)
    context1 = {'mem': mem}
    return render(request, 'mytest/mem.html', context1)

def about_project(request):
    context = {'project':Project.objects.get(id=1)}
    return render(request, 'mytest/about_project.html', context)
# Create your views here.
