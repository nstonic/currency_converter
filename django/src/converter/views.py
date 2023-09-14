from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from converter.services import Converter


@require_http_methods(["GET"])
def rate_view(request):
    from_ = request.GET.get('from')
    to = request.GET.get('to')
    value = request.GET.get('value')

    if not all([from_, to, value]):
        raise ValueError('Wrong request')

    data = {
        "result": Converter().convert(from_, to, value)
    }

    return Response(data, status=HTTP_200_OK)
