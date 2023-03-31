from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .form import EmpForm

# Importazioni
import random
from .models import Student
from .form import EmpForm
from .form import PostForm
from .models import PostBlog


# Definiamo "members"

def members(request):
    mymembers = Student.objects.all().values()
    print(Student.objects.all().values())
    template = loader.get_template('visualizza.html')

    context = {
          'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def test(request):
    template3 = loader.get_template('mysecondhtml.html')

    context = {
        'firstname': 'Simone',
        'lastname': 'Ramundi',
    }

    return HttpResponse(template3.render(context, request))

def index(request):
    template1 = loader.get_template('index.html')
    return HttpResponse(template1.render())


# creiamo la view
def modulo(request):
    templateModule = loader.get_template('modulo.html')

    stu = EmpForm()

    return render(request, "modulo.html", {'form': stu})



# Definiamo "template_view"

def template_view(request):
    myForm = EmpForm(request.POST)
    stu = EmpForm()

    if myForm.is_valid():
        nome = myForm.cleaned_data['first_name']
        cognome = myForm.cleaned_data['last_name']

        num = random.randint(0, 100000)
        num1 = random.randint(0, 100000)

        stringa = str(num1)
        stringa = Student(num, nome, cognome)
        stringa.save()
        print(stringa.first_name)

    return render(request, "modulo.html", {'form': stu})


# Definiamo "form"

def form(request):
    myForm = PostForm(request.POST)
    library = PostForm()

    if myForm.is_valid():
        titolo = myForm.cleaned_data['titolo']
        contenuto = myForm.cleaned_data['contenuto']
        autore = myForm.cleaned_data['autore']
        tag = myForm.cleaned_data['tag']
        data = myForm.cleaned_data['data']

        num = random.randint(0, 100000)
        num1 = random.randint(0, 100000)

        stringa = str(num1)
        stringa = PostBlog(num, titolo, contenuto, autore, tag, data)
        stringa.save()

        context = {}

    return render(request, "library.html", {'form': library})


# Definisco "post"

def post(request):
    mymembers = PostBlog.objects.all().values()
    print(PostBlog.objects.all().values())
    template = loader.get_template('library_online.html')

    context = {
          'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def library_online(request):
        autore = ""
        tag = ""

        myForm = (request.POST)
        dizionario = myForm.dict()

        if(len(dizionario)) != 0:
            nome = dizionario
            autore = (nome["sr"])
            tag = (nome["tg"])

            if autore and not tag:
                mydata = PostBlog.objects.filter(autore=autore).values()
            elif tag and not autore:
                mydata = PostBlog.objects.filter(tag=tag).values()
            else:
                mydata = PostBlog.objects.filter(autore=autore, tag=tag).values()

            context = {
                'mymembers': mydata,
            }
        return render(request, "library_online.html", context)


def library_searching(request):
    return render(request, "library_searching.html",)

# def delete:
def delete(request, id):

  member = PostBlog.objects.get(id=id)
  member.delete()

  return render(request, "delete.html")

# main
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

# vista
def vista(request):
    mymembers = PostBlog.objects.all().values()
    template = loader.get_template('vista.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

# details
def details(request, id):
    mymember = PostBlog.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

