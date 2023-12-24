from .models import Avatar

def avatar_url(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user).first()
        if avatar:
            return {'avatar_url': avatar.imagen.url}
    return {'avatar_url': None}