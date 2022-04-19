from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods


from htmx.models.todo import Todo
from htmx.models.course import Course, Module


class DesignView(TemplateView):
    template_name = "design.html"


def todos(request):
    todos = Todo.objects.all()
    courses = Course.objects.all()
    context = {"todos": todos, "courses": courses}

    return render(request, "todo/todos.html", context)


@require_http_methods(["GET", "POST"])
def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        todo.title = request.POST.get("title", "")
        todo.save()
        return render(request, "todo/partials/todo.html", {"todo": todo})

    return render(request, "todo/partials/edit.html", {"todo": todo})


@require_http_methods(["POST"])
def add_todo(request):
    todo = None
    title = request.POST.get("title", "")
    print(request.POST)
    course_id = request.POST.get("course", "")
    module_id = request.POST.get("modules", "")
    print(course_id)
    course = Course.objects.get(pk=course_id)
    print(course)
    module = Module.objects.get(pk=module_id)
    if title:
        todo = Todo.objects.create(title=title, course=course, module=module)
    return render(request, "todo/partials/todo.html", {"todo": todo})


@require_http_methods(["PUT"])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()
    return render(request, "todo/partials/todo.html", {"todo": todo})


@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponse()


@require_http_methods(["GET"])
def modules_todo(request):
    course = request.GET.get("course", "")
    modules = Module.objects.filter(course=course)
    context = {"modules": modules}
    return render(request, "todo/partials/modules.html", context)
