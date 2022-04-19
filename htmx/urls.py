from django.urls import path

from htmx.views import courses, modules

from htmx.views import DesignView
from htmx.views import todos, add_todo, update_todo, delete_todo, edit_todo

urlpatterns = [
    path("courses/", courses, name="courses"),
    path("courses/modules", modules, name="modules"),
    path("todos/design/", DesignView.as_view()),
    path("todos/", todos, name="todos"),
    path("todos/add-todo/", add_todo, name="add_todo"),
    path("todos/update/<int:pk>", update_todo, name="update_todo"),
    path("todos/delete/<int:pk>", delete_todo, name="delete_todo"),
    path("todos/edit/<int:pk>", edit_todo, name="edit_todo"),
]
