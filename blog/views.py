from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Rhogiel Andoy"
    subjects = ["CS224", "CS221", "CS225", "CS214"]
    age = None

    if request.method == "POST":
        age = int(request.POST.get('age', 0))

    context = {
        'age': age,
        'name': name,
        'subjects': subjects,
    }

    return render(request, 'index.html', context)


def another_page(request):
    return render(request, 'pagetwo.html')


def another_page_one(request, pk):
    
    context = {
        'pk': pk,
    }

    return render(request, 'pagefour.html', context)


def page_three(request):
    return render(request, 'pagethree.html')
