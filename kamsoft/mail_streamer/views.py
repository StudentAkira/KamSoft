from django.shortcuts import render

# Create your views here.
def test_view(request):
    a = 1
    return {"message" : "test"}
