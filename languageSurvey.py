from survey import AnonymousSurvey

# Define a question, and make a survey.
question = 'What language did you first learn to speak?'
mySurvey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
mySurvey.showQuestion()
print('Enter "q" at any time to quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    mySurvey.storeResponse(response)

# Show the survey results.
print('\nThank you to everyone who participated in the survey!')
mySurvey.showResults()