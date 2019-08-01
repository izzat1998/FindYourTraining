from social_django.middleware import SocialAuthExceptionMiddleware


class MyMiddleWare(SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        print("hello")
        # return super().get_redirect_uri(request, exception)
        # strategy = getattr(request, 'social_strategy', None)
        # return strategy.setting('LOGIN_ERROR_URL')
