
from rest_framework.response import Response
from django.conf import settings
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from ping.defaults import *
from ping.checks import checks
from ping.decorators import http_basic_auth


@csrf_exempt
@http_basic_auth
def status(request):
    """
    Returns a simple HttpResponse
    """

    response = "<h1>%s</h1>" % getattr(settings, 'PING_DEFAULT_RESPONSE', PING_DEFAULT_RESPONSE)
    mimetype = getattr(settings, 'PING_DEFAULT_MIMETYPE', PING_DEFAULT_MIMETYPE)

    response_dict = None
    if request.GET.get('checks') == 'true':
        response_dict = checks(request)
        response += "<dl>"
        for key, value in sorted(response_dict.items()):
            response += "<dt>%s</dt>" % str(key)
            response += "<dd>%s</dd>" % str(value)
        response += "</dl>"

    response = json.dumps(response_dict, sort_keys=True)

    return Response(response)
