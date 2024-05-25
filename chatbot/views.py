from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import uuid
from .dialogflow_client import detect_intent_texts

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')
        
        if request.user.is_authenticated:
            session_id = str(request.user.id)
        else:
            session_id = str(uuid.uuid4())

        bot_response = detect_intent_texts(user_message, session_id)
        return JsonResponse({'response': bot_response})
    return JsonResponse({'error': 'Invalid request'}, status=400)
