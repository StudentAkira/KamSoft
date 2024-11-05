from django.shortcuts import render


# Create your views here.
def mails_data(request):
    return render(request, "mails/mails.html")
