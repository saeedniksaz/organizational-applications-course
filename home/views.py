from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Person


class Home(View):
    def get(self, request):
        # return HttpResponse('Hello world!')
        return render(request=request, template_name='home/home.html')


class PersonListView(View):
    def get(self, request):
        template_name = 'home/users.html'
        persons = Person.objects.all()
        context = {"persons": persons}
        return render(request=request, template_name=template_name, context=context)
