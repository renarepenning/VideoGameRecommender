from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .models import myUser, Game, Mood
# request handler!

# create view ==> add to urls.py here, then in parent class.
def user_home(request):
    #return HttpResponse('Welcome to our capstone website \n user page')
    context = {
        'num_users': myUser.objects.all().count(),
        'num_games': Game.objects.all().count(),
    }


    return render(request, 'index.html', context=context)

def get_name(request, name):
    person = myUser.objects.get(pk=name)
    return HttpResponse(f"User {name}, added on {person.add_date}")



def game_by_name(request, gname):
    game = Game.objects.get(pk=gname)
    return HttpResponse(f"game: {gname}, last updated on {game.last_update}, type {game.genre}.")

# to use templates --> don't use these much
'''def say_hello_template(request):
    return render(request, 'hello.html', {'key': 'value to pass'})'''

# https://www.youtube.com/watch?v=dW1o-o1Z5G0
def saveitem(request):
    if request.method == "POST":
        if request.POST.get('mymood'):
            savevalue=Mood()
            savevalue.mymood=request.POST.get('mymood')
            savevalue.save()
            messages.success(request,"the selected mood",savevalue.mymood," was saved in db")
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')