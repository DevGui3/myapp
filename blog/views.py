from django.http import HttpResponse


def post_views(request):
    return HttpResponse("hello world")


