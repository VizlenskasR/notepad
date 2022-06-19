from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from .models import Notes, Category
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect



# Create your views here.
# classes related to notes
# class NoteListView(LoginRequiredMixin, generic.ListView):
#     model = Notes
#     template_name = 'note_list.html'
#     context_object_name = 'notes'


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
    success_url = "/notes/user_notes/"
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

#classes related to categories
# class CaregoryListView(LoginRequiredMixin, generic.ListView):
#     model = Category
#     template_name = 'category_list.html'
#     context_object_name = 'categories'
#     success_url = "/notes/"
#
# class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
#     model = Category
#     template_name = 'category.html'
#     context_object_name = 'category'

    # def test_func(self):
    #     notes = self.get_object()
    #     return self.request.user == notes.author



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
                    return redirect('user_notes')

        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')

