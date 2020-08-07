from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Position, Contestant, User

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

#get positions and the candidates under them
def display(request):
    position = Position.objects.all()
    context = {'positions':position}
    return render(request, 'vote.html', context)

#voting for the conadidate of our choice
def vote(request):
    position = Position.objects.all()
    try:
        selected_candidate = position.contestant_set.get(request.POST['POST'])
    except(KeyError, Candidate.DoesNotExist):
        #redisplay the voting form
        return render(request, 'vote.html',{
            'postions':position,
            'error_message': 'your voting is not complete' 
        })        
    else:
        selected_candidate.no_of_votes += 1
        selected_candidate.save()
        return render(request, 'vote.html',{
            'postions':position,
            'error_message': 'your voting is not complete' 
        })   