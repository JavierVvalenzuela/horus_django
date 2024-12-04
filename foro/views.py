from django.shortcuts import render

def index(request):
    # Lógica para detectar si el usuario está en un dispositivo móvil
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    is_mobile = False
    
    mobile_keywords = ['iphone', 'ipad', 'android', 'windows phone', 'blackberry', 'mobile', 'opera mini']
    
    for keyword in mobile_keywords:
        if keyword in user_agent:
            is_mobile = True
            break

    return render(request, 'foro/index.html', {'is_mobile': is_mobile})