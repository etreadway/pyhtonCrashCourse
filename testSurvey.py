import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''Tests for the class AnonymousSurvey'''

    def testStoreSingleResponse(self):
        '''Test that a single response in stored prpoerly'''
        question = 'What language did you first learn to speak?'
        mySurvey = AnonymousSurvey(question)
        mySurvey.storeResponse('English')

        self.assertIn('English', mySurvey.responses)

    def testStoreThreeResponses(self):
        '''Test that three individual responses are stored properly'''
        question = 'What language did you first learn to speak?'
        mySurvey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            mySurvey.storeResponse(response)

        for response in responses:
            self.assertIn(response, mySurvey.responses)

unittest.main()