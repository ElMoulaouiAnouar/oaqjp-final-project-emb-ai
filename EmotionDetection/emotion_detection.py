import requests
import json

def emotion_detector(text_to_analyse):
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }

    response = requests.post('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
                             headers=header, json=data)
    
    if response.status_code == 400 :
      return {
            'anger': None,'disgust': None,
            'fear': None,'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }   
    elif response.status_code == 200 : 
        format_data = json.loads(response.text)

        emotion_predictions = format_data['emotionPredictions'][0]['emotion']
        anger_score = emotion_predictions['anger']
        disgust_score = emotion_predictions['disgust']
        fear_score = emotion_predictions['fear']
        joy_score = emotion_predictions['joy']
        sadness_score = emotion_predictions['sadness']
        
        dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
    
        result = {
                'anger': anger_score,'disgust': disgust_score,
                'fear': fear_score,'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        return result
    
  








