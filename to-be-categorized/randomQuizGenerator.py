#! /usr/bin/env python3
# randomQuizGenerator.py - Create quizzes with questions in random order, along with
# an answer key.

import random

# Quiz Data: key = state, value = capital
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Repeat loop 35 times to create 35 quizzes.
for quizNum in range(35):
    # Create a quiz file with name = "capitalsquiz" + NUMBER + ".txt"
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    # Create an answer file with name = "capitalsquiz_answers" + NUMBER + ".txt"
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Quiz Header: Name, Date, and Period
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    # Form Number is written via %s formatting
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle order of states.
    # Get the states, which are the keys in DICT 'capitals'.
    states = list(capitals.keys())
    # Shuffle the states List
    random.shuffle(states)

# Loop through all 50 states. Make a Q for each State.
for questionNum in range(50):

    # Store the capital > state > questionNum in correctAnswer
        # e.g. [capitals[capitals.keys[#]]]
    correctAnswer = capitals[states[questionNum]]
    # To get the wrongAnswers, duplicate States...
    wrongAnswers = list(capitals.values())
    # ... and delete the correct answer
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    # From wrongAnswers,
    wrongAnswers = random.sample(wrongAnswers, 3)
    # So we have 4 options: the right answer, and 3 random wrong answers.
    answerOptions = wrongAnswers + [correctAnswer]
    # Shuffle the options, so the correct answer isn't always D.
    random.shuffle(answerOptions)

    # Write Qs and As into the quiz file.
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
    for i in range(4):
        quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
    quizFile.write('\n')

# Write the answer key to a file.
    # Here, the first %s is the question number.
    # The second %s is matching A, B, C, or D to the correctAnswer
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
        answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()
