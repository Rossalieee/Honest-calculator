students_limit = int(input())
all_applicants = []

with open('applicants_5.txt') as infile:
    for line in infile:
        all_applicants.append(line.strip().split(' '))


def floatify(num):
    try:
        return float(num)
    except ValueError:
        return num


all_applicants = [[floatify(x) for x in row] for row in all_applicants]

faculties = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
faculties_exam_index = {'Biotech': 3, 'Chemistry': 3, 'Engineering': 5, 'Mathematics': 4, 'Physics': 2}
faculties_dict = dict.fromkeys(faculties, [])
waiting_list = set([" ".join(x[0:2]) for x in all_applicants])


#  exam_index: physics -> 2, chemistry -> 3, math -> 4, computer science -> 5
#  fac_index: 6 -> first choice, 7 -> second, 8 -> third
def admission_procedure(faculty, exam_index, fac_index):
    global faculties_dict
    global waiting_list
    appl_sorted = sorted(all_applicants, key=lambda x: (-x[exam_index], x[0], x[1]))
    accepted = []
    for x in appl_sorted:
        if x[fac_index] == faculty and " ".join(x[0:2]) in waiting_list:
            accepted.append(x[0:6])

    while len(accepted) > students_limit - len(faculties_dict[faculty]):
        accepted.pop()
    if len(accepted) > 0:
        accepted_names = set([" ".join(x[0:2]) for x in accepted])
        waiting_list -= accepted_names
        if len(faculties_dict[faculty]) > 0:
            accepted += faculties_dict[faculty]
            accepted = sorted(accepted, key=lambda x: (-x[exam_index], x[0], x[1]))
        faculties_dict[faculty] = accepted


def print_accepted(fac, ex_indx):
    print(fac)
    for x in faculties_dict[fac]:
        print(' '.join(x[0:2]), end=' '), print(x[ex_indx])


for key, value in faculties_exam_index.items():
    admission_procedure(key, value, 6)
for key, value in faculties_exam_index.items():
    admission_procedure(key, value, 7)
for key, value in faculties_exam_index.items():
    admission_procedure(key, value, 8)

for key, value in faculties_exam_index.items():
    print_accepted(key, value)
    print('')
