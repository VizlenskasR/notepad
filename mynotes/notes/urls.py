from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.UserNotesListView.as_view(), name="user_notes"),
    path('<int:pk>', views.NoteDetailView.as_view(), name="note"),
    path('register/', views.register, name="register"),
    path('tinymce/', include("tinymce.urls")),
    path('new_note/', views.NoteCreateView.as_view(), name="new_note"),
    path('new_category/', views.CategoryCreateView. as_view(), name="new_category"),
    path('note/<int:pk>/update', views.NoteUpdateView.as_view(), name="note_update"),
    path('note/<int:pk>/delete', views.NoteDeleteView.as_view(), name='note_delete'),
    path('search/', views.search, name='search'),

]
