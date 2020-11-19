class AnonymousSurvey():
    '''Collect anonymous answers tp a survey question.'''

    def __init__(self, question):
        '''Store a question, and prepare to store responses.'''
        self.question = question
        self.responses = []

    def showQuestion(self):
        '''Show the survey question.'''
        print(self.question)

    def storeResponse(self, newResponse):
        '''Store a single response to the survey.'''
        self.responses.append(newResponse)

    def showResults(self):
        '''Show all the responses that have been given.'''
        print('Survey results:')
        for response in self.responses:
            print('- ' + response)