from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username: %s password: %s' % (username, password))
        return HttpResponse('进行注册业务处理')


