from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Dog, Toy
from .forms import FeedingForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

# @login_required
# def cats_detail(request, cat_id):
#     cat = Cat.objects.get(id=cat_id)
#     toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
#     feeding_form = FeedingForm()
#     return render(request, 'cats/detail.html',
#      {'cat': cat, 'feeding_form': feeding_form, 'toys' : toys_cat_doesnt_have })

# @login_required
# def assoc_toy(request, cat_id, toy_id):
#     Cat.objects.get(id=cat_id).toys.add(toy_id)
#     return redirect('cats_detail', cat_id=cat_id)

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    print(dog)
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request,'dogs/detail.html', {'dog': dog, 'feeding_form': feeding_form, 'toys': toys_dog_doesnt_have})

def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'toys/index.html', {'toys': toys })


def toys_detail(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    return render(request, 'toys/detail.html', {'toy': toy})

def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('dogs_detail', dog_id=dog_id)

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('dogs_detail', dog_id=dog_id)



class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/dogs/'

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']
    success_url = '/dogs/'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    # success_url = '/toys/'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['color']

class ToyDelete(DeleteView):
    model = Toy
    success_url='/toys/'