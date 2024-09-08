from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'EsQua',
        'price': '5000',
        'stock': '10',
        'description':'Minuman Segerrrrrrrrrrrr'
    }

    return render(request, "main.html", context)