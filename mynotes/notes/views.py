from django.shortcuts import render
from django.views import generic
from .models import Notes

# Create your views here.
class NoteListView(generic.ListView):
    model = Notes
    template_name = 'note_list.html'
    context_object_name = 'notes'


class NoteDetailView(generic.DetailView):
    model = Notes
    template_name = 'note.html'
    context_object_name = 'note'

