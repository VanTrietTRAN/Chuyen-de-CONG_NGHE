from typing import Optional

from django.http import HttpRequest, HttpResponse


def report(request: HttpRequest, id: Optional[int] = None) -> HttpResponse:
    if id is None:
        return HttpResponse("Credit reports list")
    return HttpResponse(f"Credit report {id}")


def charge(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Charge processed")


