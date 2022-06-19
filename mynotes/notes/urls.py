from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.NoteListView.as_view(), name="notes"),
    path('<int:pk>', views.NoteDetailView.as_view(), name="note"),
    path('register/', views.register, name="register"),
    path('user_notes/', views.UserNotesListView.as_view(), name="user_notes"),
    path('tinymce/', include("tinymce.urls")),
    path('new_note/', views.NoteCreateView.as_view(), name="new_note"),
    path('new_category/', views.CategoryCreateView. as_view(), name="new_category"),
    path('note/<int:pk>/update', views.NoteUpdateView.as_view(), name="note_update"),
    path('note/<int:pk>/delete', views.NoteDeleteView.as_view(), name='note_delete'),

]
