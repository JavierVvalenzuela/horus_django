from django.shortcuts import render
from user_agents import parse

def index(request):
    # Obtener el user agent desde las cabeceras HTTP
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    is_mobile = False

    # Detectar si es un dispositivo móvil
    if user_agent:
        user_agent_parsed = parse(user_agent)
        if user_agent_parsed.is_mobile:
            is_mobile = True

    return render(request, 'foro/index.html', {'is_mobile': is_mobile})