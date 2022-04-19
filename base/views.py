from django.shortcuts import render
from django.db.models import Q
from .models import Property, Type, Message

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def about(request):
    return render(request, 'base/about.html')


def contact(request):
    return render(request, 'base/contact.html')


def blog(request):
    return render(request, 'base/blog.html')


def listing(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    properties = Property.objects.filter(
        Q(type__name__icontains=q) |
        Q(name__icontains=q) |
        Q(host__username__icontains=q) |
        Q(description__icontains=q) |
        Q(price__icontains=q)
    )
    types = Type.objects.all()
    property_count = properties.count()
    property_messages = Message.objects.filter(
        Q(property__type__name__icontains=q)
        )

    context = {'properties': properties, 'types': types,
               'property_count': property_count, 'property_messages': property_messages}
    return render(request, 'base/listing.html', context)

def property(request, pk):
    property = Property.objects.get(id=pk)

    context = {'property': property}

    return render(request, 'base/property.html', context)    


def agent(request):
    return render(request, 'base/agent.html')


def blog_single(request):
    return render(request, 'base/blog_single.html')


def agent_single(request):
    return render(request, 'base/agent_single.html')
