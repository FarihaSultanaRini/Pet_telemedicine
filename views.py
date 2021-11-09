from django.shortcuts import render,get_object_or_404,redirect
from .models import Pet
from .form import InsertPet
from Landlord.landlord_models import Landlord
from django.contrib.auth.decorators import login_required
# Create your views here.
def petInfo(request):
    pet = Pet.objects.all()
    context = {
        "pet": pet
    }
    return render(request, 'Pet/petinfo.html',context)

# Create your views here.
@login_required
def insertPetinfo(request):
    form = InsertPet()

    if request.method == "POST":
        form = InsertPet(request.POST, request.FILES)

        if form.is_valid:
            form.save()
            return redirect('Pet')

    context = {
        'form': form
    }

    return render(request, 'House/inserthouse.html', context)
    # form = InsertPet()
    # landlord = Landlord.objects.get(user= request.user)
    # if Landlord:
    #     message = "Insert Pet Information"
    #     if request.method == 'POST':
    #         form = InsertPet(request.POST, request.FILES)
    #         message = "Oops,Try again"
    #
    #         if form.is_valid():
    #             pet = form.save(commit=False)
    #             # house.user =request.user
    #             pet.landlord = landlord
    #             pet.save()
    #             form = InsertPet()
    #             message = "Successfull !"
    #             return redirect('Pet')
    #
    #     context = {
    #         'form': form,
    #         'message': message,
    #         'landlord':True
    #
    #     }
    #     return render(request, 'House/inserthouse.html', context)
    #
    # else:
    #     return render(request, 'House/advertisement_info.html')
    #     redirect ("Advertisment")



