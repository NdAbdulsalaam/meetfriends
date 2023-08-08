from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    content = {
        'fruits': ['Apple', 'Banana', 'Mango', 'Orange']
    }
    return HttpResponse(template.render(content, request))

# no view for error_404 page is required
# def error_404(request):
#     template = loader.get_template('404.html')
#     return HttpResponse(template.render())

def mymembers(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    content = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(content, request))

def member_details(request, id):
    member_details = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    content = {
        'member_details': member_details,
    }
    return HttpResponse(template.render(content, request))

