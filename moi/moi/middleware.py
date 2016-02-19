from django.shortcuts import render

class AuthRequiredMiddleware(object):
    def process_request(self, request):
        if '/admin' not in request.path and request.user.is_anonymous():
            return render(request, 'moi/splash.html')
        return None
