from survey import AnonymousSurvey

# Define a question and make a survey
question = 'Which language did you first learn to speak?'
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print('Enter "q" at any time to quit.')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    language_survey.store_response(response)
    
# Show the survey results
print('\nThank you for your responses.')
language_survey.show_results()