score1 = float (input ('What is you score for Test 1: '))
per_1 = float (input ('What is percentage for Test 1: '))
score2 = float (input ('What is your score for Test 2: '))
per_2 = float (input ('What is percentage for Test 2: '))
score3 = float (input ('What is you score for Test 3: '))
per_3 = float (input ('What is percentage for Test 3: '))
exam_score = float (input ('What is your score for Exam: '))

final_mark = score1*per_1/100 + score2*per_2/100 + score3*per_3/100 + exam_score*0.5

print ('Your final mark is ', (final_mark))
