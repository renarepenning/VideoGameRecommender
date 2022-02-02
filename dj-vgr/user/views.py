from django.shortcuts import render
from django.http import HttpResponse

# request handler!

def say_hello(request):
    return HttpResponse('Hello World')



# to use templates --> don't use these much
'''def say_hello_template(request):
    return render(request, 'hello.html', {'key': 'value to pass'})'''