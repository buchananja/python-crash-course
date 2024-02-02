import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    '''A survey that will be avilible to all test functions.'''
    question = 'Which language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)
    return language_survey    

def test_store_single_response(language_survey):
    '''Test that a single response is stored properly.'''
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
    
def test_store_three_responses(language_survey):
    '''Test that a single response is stored properly.'''
    responses = ['English', 'Russian', 'Spansish']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert 'English' in language_survey.responses