from django.http import JsonResponse
from functools import wraps

# 自定义装饰器时，使用 @wraps 可以让装饰后的函数看起来更像原函数，方便调试和使用，比如：


def login_required_json(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"success": False, "msg": "未登录"}, status=401)
        return func(request, *args, **kwargs)

    return wrapper
