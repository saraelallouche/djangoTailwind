from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from htmx.models.course import Course, Module


def courses(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "courses/university.html", context)


@require_http_methods(["GET"])
def modules(request):
    course = request.GET.get("course", "")
    modules = Module.objects.filter(course=course)
    context = {"modules": modules}
    return render(request, "courses/partials/modules.html", context)
