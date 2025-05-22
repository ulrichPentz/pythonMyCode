from django.shortcuts import render, redirect
from .models import Demographics  # Assuming &quot;Receipe&quot; is the correct model name
from django.http import HttpResponse


def demographics(request):
    if request.method == 'POST':
        data = request.POST

        demographics_name = data.get('demographics_name')
        demographics_surname = data.get('demographics_surname')
        demographics_image = request.FILES.get('demographics_image')
        demographics_address = data.get('demographics_address')
        demographics_age = data.get('demographics_age')

        Demographics.objects.create(
            demographics_image = demographics_image,
            demographics_name = demographics_name,
            demographics_surname = demographics_surname,
            demographics_address = demographics_address,
            demographics_age = demographics_age,
        )
        return redirect('/')

    queryset = Demographics.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            demographics_name__icontains=request.GET.get('search'))

    context = {'demographics': queryset}
    return render(request, 'demographics.html', context)


def delete_demographics(request, id):
    queryset = Demographics.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update_demographics(request, id):
    queryset = Demographics.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        demographics_name = data.get('demographics_name')
        demographics_surname = data.get('demographics_surname')
        demographics_image = request.FILES.get('demographics_image')
        demographics_address = data.get('demographics_address')
        demographics_age = data.get('demographics_age')

        queryset.demographics_name = demographics_name
        queryset.demographics_surname = demographics_surname
        queryset.demographics_image = demographics_image
        queryset.demographics_address = demographics_address
        queryset.demographics_age = demographics_age
        

        if demographics_image:
            queryset.demographics_image = demographics_image

        queryset.save()
        return redirect('/')

    context = {'demographics': queryset}
    return render(request, 'update_demographics.html', context)