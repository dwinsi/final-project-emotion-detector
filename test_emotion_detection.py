'''
     run unit tests to validate the application output.
'''
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector( unittest.TestCase):
    '''
        calls the required application function from the package and 
        tests it for the following statements and dominant emotions.
    '''
    def test_emotion_detector(self):
        '''
            calls the required application function from the package and 
            tests it for the following statements and dominant emotions.
        '''
        # Dominant Emotion: joy
        result1 = emotion_detector('I am glad this happened')
        self.assertEqual(result1['dominant_emotion'], 'joy')

        # Dominant Emotion: anger
        result2 = emotion_detector('I am really mad about this')
        self.assertEqual(result2['dominant_emotion'], 'anger')

        # Dominant Emotion: disgust
        result3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        # Dominant Emotion: sadness
        result4 = emotion_detector('I am so sad about this')
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        # Dominant Emotion: Fear
        result5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result5['dominant_emotion'], 'fear')


unittest.main()