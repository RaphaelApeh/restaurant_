from django.contrib.auth import get_user_model

User = get_user_model()

def authenticate(request,username,password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
    if user.check_password(password):
        return user
    else:
        return None