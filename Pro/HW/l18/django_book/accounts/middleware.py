import logging

from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.utils.timezone import now

logger = logging.getLogger(__name__)


class AccessLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('django')

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated and request.path.startswith('/protected/'):
            self.logger.info(f"User {request.user.username} accessed {request.path}")

        return response


class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            if isinstance(e, Http404):
                return HttpResponseNotFound("Page not found")
            return HttpResponseServerError("Server error occurred")
        return response
