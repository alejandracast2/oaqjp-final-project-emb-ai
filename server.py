from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    '''Route for emotion detection.'''

    # Get the text to analyze from the query parameters
    text_to_analyze = request.args.get('text')

    # Analyze the emotion of the given text
    emotion_result = emotion_detector(text_to_analyze)

    # Return the result as a JSON response
    return f"For the given statement, the system response is 'anger': {emotion_result['anger']}, 'disgust': {emotion_result['disgust']}, 'fear': {emotion_result['fear']}, 'joy': {emotion_result['joy']} and 'sadness': {emotion_result['sadness']}. The dominant emotion is {emotion_result['dominant_emotion']}"

@app.route("/")
def render_index_page():
    '''Render the main index page.'''

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    