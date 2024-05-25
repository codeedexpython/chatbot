import os
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument
from django.conf import settings

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./mychatbot-p9ep-737d518430d2.json"

DIALOGFLOW_PROJECT_ID = 'mychatbot-p9ep'
DIALOGFLOW_LANGUAGE_CODE = 'en'

def detect_intent_texts(text, session_id):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except InvalidArgument as e:
        raise
