from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import generic
from .models import Notes, Category
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


class UserNotesListView(LoginRequiredMixin, generic.ListView):
    model = Notes
    template_name = 'user_notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)


class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Notes
    fields = ['title', 'note', 'category']
    success_url = "/notes/"
    template_name = 'note_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Notes
    template_name = 'note.html'
    context_object_name = 'note'

    def test_func(self):
        notes = self.get_object()
        return self.request.user == notes.author

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Notes
    fields = ['title', 'note', 'category']
    success_url = "/notes/"
    template_name = 'note_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        notes = self.get_object()
        return self.request.user == notes.author


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Notes
    success_url = "/notes/user_notes/"
    template_name = 'note_delete.html'
    context_object_name = 'note'

    def test_func(self):
        note = self.get_object()
        return self.request.user == note.author



class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = ['name']
    template_name = 'create_category.html'
    context_object_name = 'create_category'
    success_url = "/notes/"


# registration function
@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    return redirect('user_notes')

        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')


def search(request):
    query = request.GET.get('query')
    search_results = Notes.objects.filter(Q(title__icontains=query))
    return render(request, 'search.html', {'notes': search_results, 'query': query})


