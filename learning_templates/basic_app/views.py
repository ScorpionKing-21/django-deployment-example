from django.shortcuts import render

def index(request):
    contex_dict = {'text':'Hello World', 'number':100}
    return render(request, 'basic_app/index.html', context=contex_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/rele_url_templ.html')

def base(request):
    return render(request, 'basic_app/base.html')
