from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Anasayfa Merhaba Dünya")
def authors(request):
    return HttpResponse("Yazarların Listesi Geldi Buraya heralde kodlar gelecek")
def books(request):
    return HttpResponse("Kitapların Listesi Geldi Buraya heralde kodlar gelecek")
def authordetails(request,authorId):
    return HttpResponse("Yazarların Detay Listesi Geldi Buraya heralde kodlar gelecek" + authorId)