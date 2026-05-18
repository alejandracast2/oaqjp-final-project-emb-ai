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

    return response.text
    
    