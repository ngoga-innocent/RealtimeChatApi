
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewChat.settings")  # Replace with your project name
django.setup()
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from chat.routing import wsPattern
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewChat.settings')

asgi_app = get_asgi_application()
application=ProtocolTypeRouter({
    "http":asgi_app,
    "websocket":URLRouter(wsPattern),
})
