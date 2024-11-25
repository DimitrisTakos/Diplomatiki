from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'tourismingreece/index.html', {})


def about_us(request):
    return render(request, 'tourismingreece/about-us.html', {})
