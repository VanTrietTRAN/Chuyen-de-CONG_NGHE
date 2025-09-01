from django.http import HttpRequest, HttpResponse
import asyncio
from django.views import View

from django.views.generic import TemplateView

def homepage(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Homepage (apps.main)")

class AboutView(TemplateView):
    template_name = "about.html"

class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")