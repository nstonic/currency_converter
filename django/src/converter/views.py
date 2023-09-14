from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from requests import HTTPError
from rest_framework import status

from converter.services import Converter


@require_http_methods(["GET"])
def rate_view(request):
    from_ = request.GET.get('from')
    to = request.GET.get('to')
    value = request.GET.get('value')

    if not value.isdigit():
        return JsonResponse({'error': 'Wrong value'}, status=status.HTTP_400_BAD_REQUEST)

    return rate_path_view(request, from_, to, int(value))


@require_http_methods(["GET"])
def rate_path_view(request, from_: str, to: str, value: int):
    try:
        data = {
            "result": Converter().convert(from_, to, value)
        }
    except ValueError as ex:
        return JsonResponse({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    except HTTPError as ex:
        return JsonResponse({'error': str(ex)}, status=status.HTTP_424_FAILED_DEPENDENCY)

    return JsonResponse(data, status=status.HTTP_200_OK)
