from django.shortcuts import render, redirect
from .models import Category, Photo


def gallery(request):
    category= request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(Category__name=category)
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photosite/gallery.html', context)


def addPhoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        Image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != "":
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            Category=category,
            image=Image,
            description=data['description'],
        )
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photosite/add.html', context)


def Pictures(request, pk):
    photoz = Photo.objects.filter(id=pk)
    context = {"photoz": photoz}
    return render(request, 'photosite/Pictures.html', context)
