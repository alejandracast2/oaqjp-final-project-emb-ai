import json

import requests


def emotion_detector(text_to_analyze):
    '''Analyze emotion of a given text.'''

    # Define the URL for the emotion analysis API
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Create the payload with the text to be analyzed
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Set the headers with the required model ID
    header = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    # Make a POST request to the API
    response = requests.post(
        url,
        json=myobj,
        headers=header
    )

    datos = {}
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        datos = formatted_response['emotionPredictions'][0]["emotion"]
        max_datos = max(datos, key=datos.get)
        datos["dominant_emotion"] = max_datos

    elif response.status_code == 400:
        datos["anger"] = None
        datos["disgust"] = None
        datos["fear"] = None
        datos["joy"] = None
        datos["sadness"] = None
        datos["dominant_emotion"] = None

    else:
        datos["anger"] = None
        datos["disgust"] = None
        datos["fear"] = None
        datos["joy"] = None
        datos["sadness"] = None
        datos["dominant_emotion"] = None
    
    return datos
    