from django.http import HttpRequest, HttpResponse


def help_home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Help home (apps.help)")


