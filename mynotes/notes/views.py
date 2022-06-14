from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from .models import Notes
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect



# Create your views here.
class NoteListView(generic.ListView):
    model = Notes
    template_name = 'note_list.html'
    context_object_name = 'notes'


class UserNotesListView(generic.ListView):
    model = Notes
    template_name = 'user_notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)


class NoteDetailView(generic.DetailView):
    model = Notes
    template_name = 'note.html'
    context_object_name = 'note'


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')

