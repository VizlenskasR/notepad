from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.NoteListView.as_view(), name="notes"),
    path('<int:pk>', views.NoteDetailView.as_view(), name="note"),
    path('register/', views.register, name='register'),
    path('user_notes/', views.UserNotesListView.as_view(), name='user_notes'),
    path('tinymce/', include('tinymce.urls')),

]
