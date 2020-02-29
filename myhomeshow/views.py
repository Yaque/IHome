from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render

list_data = [{"name":"good", "password":"python"}, {'name':'learning','password':'django'}]


# 首页
def index(request):
    return render(request, 'index.html')


def index_data(request):
    name = request.POST.get('name', None)
    password = request.POST.get('password', None)

    one_data = {'name':name, 'password':password}
    list_data.append(one_data)
    return render(request, 'index0.html', {'form':list_data})

