from django.shortcuts import render

# Create your views here.

def quote_list(request):
    quotes = Quote.objects.all()  # fetch all quotes from DB
    return render(request, "quotes/quote_list.html", {"quotes": quotes})