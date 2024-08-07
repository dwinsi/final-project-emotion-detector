'''
    this module will predict Emotion of sentences using 
    Watson NLP library.
'''
# Import required modules
import json
import requests

def emotion_detector(text_to_analyze):
    '''
        run emotion detection using the 
        Watson NLP library Emotion Detection.
    '''

    # URL of the Emotion detector service in Watson NLP.
    baseurl =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'
    endpoint = 'NlpService/EmotionPredict'
    url = baseurl + endpoint

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the predict emotion API
    response = requests.post(url, json = myobj, headers = header)

    # parsing the JSON request from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        # retrieving Emotion predeictions
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        # retieving name of the dominant emotion
        dominant_emotions = {key for key in emotion if emotion[key] == max(emotion.values())}
        # adding dominant emotion to the dictionary 'emotion' to return it as response.
        for dominant_emotion in dominant_emotions:
            emotion['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotion = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    elif response.status_code == 500:
        emotion = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    return emotion
