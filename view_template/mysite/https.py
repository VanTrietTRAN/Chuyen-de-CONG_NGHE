from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.http import Http404
from django.shortcuts import render
from polls.models import Poll
from django.core.exceptions import PermissionDenied
from django.test import SimpleTestCase, override_settings
from django.urls import path

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

def my_view(request):
    return HttpResponse(status=201)
    
def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, "polls/detail.html", {"poll": p})

def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)

def permission_denied_view(request):
    raise PermissionDenied

urlpatterns = [
    path("403/", permission_denied_view),
]

handler403 = response_error_handler
# ROOT_URLCONF must specify the module that contains handler403 = ...
@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):
    def test_handler_renders_template_response(self):
        response = self.client.get("/403/")
        # Make assertions on the response here. For example:
        self.assertContains(response, "Error handler content", status_code=403)

async def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)