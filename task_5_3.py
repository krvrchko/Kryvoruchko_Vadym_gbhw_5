def gen_tutors_list(tutors, klasses):
  i = 0
  while i < len(tutors) and i < len(klasses):
    yield tutors[i], klasses[i]
    i += 1
  while i < len(tutors):
    yield tutors[i], None
    i += 1
  while i < len(klasses):
    yield None, klasses[i]
    i += 1  

tutors1 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]

klasses1 = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutors2 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]

klasses2 = [
    '9А', '7В', '9Б', '9В', '8Б'
]

tut_klas_list = gen_tutors_list(tutors1, klasses1)
tut_klas_list2 = gen_tutors_list(tutors2, klasses2)

for i in tut_klas_list:
  print(i)

print(type(tut_klas_list))

print('--------------------------------------------')

for i in tut_klas_list2:
  print(i)

print(type(tut_klas_list2))

