import json
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToJson


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\myproject\pybo\javis-key.json'

DIALOGFLOW_PROJECT_ID = 'shinyoungtest-t9ld'
DIALOGFLOW_LANGUAGE_CODE = 'ko'

session_client = dialogflow.SessionsClient()

def chat(text, session_id='me'):
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text = text, language_code = DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    result = json.loads(MessageToJson(response))
    print(response)

    return response.query_result.fulfillment_text

chat('안녕','12345')