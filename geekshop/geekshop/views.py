from django.shortcuts import render


def index(request):
    list_params = ['a1', 'a2', 'a3']
    context = {
        'list_params': list_params,
    }
    return render(request, 'index.html', context=context)

def contacts(request):
    return render(request, 'contact.html')
