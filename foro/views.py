from django.shortcuts import render
from user_agents import parse

def index(request):
    # Inicializamos la variable de tipo de dispositivo
    device_type = 'Desconocido'
    
    # Obtener el 'user_agent' desde las cabeceras HTTP
    user_agent = request.META.get('HTTP_USER_AGENT', '')

    # Si el 'user_agent' está presente, analizamos el tipo de dispositivo
    if user_agent:
        user_agent_parsed = parse(user_agent)
        
        # Determinamos el tipo de dispositivo
        if user_agent_parsed.is_mobile:
            device_type = 'Móvil'
        elif user_agent_parsed.is_tablet:
            device_type = 'Tablet'
        else:
            device_type = 'Escritorio'
    
    # Pasamos el tipo de dispositivo al template
    return render(request, 'foro/index.html', {'device_type': device_type})