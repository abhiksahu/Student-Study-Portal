from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('aboutus', views.about_us, name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('notes',views.notes,name='notes'),
    path('delete_note/<int:pk>',views.delete_note,name='delete-note'),
    path('update_todo/<int:pk>',views.update_todo,name='update-todo'),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name='notes-detail'),
    path('homework',views.homework,name='homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update-homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name='delete-homework'),
    path('youtube',views.youtube,name='youtube'),
    path('todo',views.todo,name='todo'),
    path('delete_todo/<int:pk>',views.delete_todo,name='delete-todo'),
    path('books',views.books,name='books'),
    path('dictionary',views.dictionary,name='dictionary'),
    path('wiki',views.wiki,name='wiki'),
    path('conversion',views.conversion,name='conversion'),
    path('class1',views.class1,name='class1'),
    path('class2',views.class2,name='class2'),
    path('class3',views.class3,name='class3'),

]