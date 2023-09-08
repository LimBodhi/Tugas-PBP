from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Barang 1',
        'amount': 100,
        'price': 10000,
        'description': "Ini barang 1"
    }

    return render(request, "main.html", context)