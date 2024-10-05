"""
A Flask application for emotion detection based on input text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.get('/emotionDetector')
def sent_emotion_detector():
    """
    Analyzes the text for emotions and returns the results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    return f"""
    For the given statement, the system response is 'anger': {response['anger']},
     'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} 
     and 'sadness': {response['sadness']}.The dominant emotion 
     is <strong>{response['dominant_emotion']}</strong>."""
@app.get('/')
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    