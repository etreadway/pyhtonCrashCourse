import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''Tests for the class AnonymousSurvey'''

    def setUp(self):
        '''
        Create a survey and a set of responses for use in all test methods.
        '''
        question = 'What language did you first learn to speak?'
        self.mySurvey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'mandarin']

    def testStoreSingleResponse(self):
        '''Test that a single response in stored prpoerly'''
        self.mySurvey.storeResponse(self.responses[0])
        self.assertIn(self.responses[0], self.mySurvey.responses)


    def testStoreThreeResponses(self):
        '''Test that three individual responses are stored properly'''

        for response in self.responses:
            self.mySurvey.storeResponse(response)

        for response in self.responses:
            self.assertIn(response, self.mySurvey.responses)

unittest.main()