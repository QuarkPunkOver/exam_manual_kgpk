from django.shortcuts import redirect

class ForcePasswordResetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.FirstAuth:
            if request.path != '/password-reset/':  # Убедитесь, что это путь к форме сброса
                return redirect('/password-reset/')  # Замените на правильный путь
        return self.get_response(request)
#Глобальный редирект первосозданных акков на сброс пароля