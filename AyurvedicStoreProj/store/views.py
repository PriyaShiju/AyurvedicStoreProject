from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import *
from django.core.exceptions import *
from django.views.decorators.http import *
from django.views.decorators.cache import *
from django.core.paginator import *
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse("Welcome to Ayurvedic Store in Australia")

def productdetail(request):
    return HttpResponse("Ayurvedic Product Details and Benefits")

@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def relatedproducts(request):
    items = ("Thailam","Choornam","Kozhambhu","Podi","Kulika")
    if request.method == 'GET':
        paginator = Paginator(items,2)
        pages = request.GET.get('page',1)
        try:
            items=paginator.page(pages)
            
        except PageNotAnInteger:
            items = paginator.page(1)
        
        #session management
        messages.info(request,"Successfully fetched")
        if not request.session.has_key('customer'):
            request.session['customer'] = 'Priya'
            print("Session value : " + request.session['customer'])
            
            
        #set and get cookies
        response = render(request, 'store/listproduct.html', {'items' : items})    
        if request.COOKIES.get("visits"):
            value = int(request.COOKIES.get('visits'))
            print("get cookie - " + str(value+1))
            response.set_cookie("visits", value+1)
        else:
            value = 1
            print("set cookie - " + str(value))
            response.set_cookie("visits", value)
        return response
    elif request.method == 'POST':
        return HttpResponseNotFound("Post is not allowed")
    
        #print("Request Headers : ",request.headers)
        #print("\n\nRequest : ", request)  # shows the Httprequest method as GET    
        #return HttpResponse("Related Products")
        
def logout(request):
    try:
        del request.session['customer']
    except:
        print("No session data found Error ")
    return HttpResponse("You have logged out")
        
def error_handler(request, exception=None):
    return HttpResponseNotFound("<h1>Page Not Found </h1> status = 404")

class ProductView(View):
    def get(self, request):
        items = ("Thailam","Choornam","Kozhambhu","Podi","Kulika")        
        paginator = Paginator(items,2)
        pages = request.GET.get('page',1)
        try:
            items=paginator.page(pages)
            
        except PageNotAnInteger:
            items = paginator.page(1)
            
        return render(request, 'store/listproduct.html', {'items' : items})    
        
class ProductViewAll(TemplateView):
    template_name = 'store/listproduct.html'
    
    # overwrite the method get_context_data
    def get_context_data(self, **kwargs):
        items = ("Thailam","Choornam","Kozhambhu","Podi","Kulika")        
        context ={'items':items}            
        return context    
    
class ListAllItems(ListView):
    template_name = 'store/listproduct.html'
    queryset = ("Thailam","Choornam","Kozhambhu","Podi","Kulika")        
    context_object_name ='items'
    paginate_by =2