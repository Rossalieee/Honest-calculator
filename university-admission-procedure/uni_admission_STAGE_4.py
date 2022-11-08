students_limit = int(input())
all_applicants = []

with open('applicant_list.txt') as infile:
    for line in infile:
        all_applicants.append(line.strip().split(' '))


def floatify(num):
    try:
        return float(num)
    except ValueError:
        return num


all_applicants = [[floatify(x) for x in row] for row in all_applicants]

#  list of all applicants sorted by their first, second and third choice of faculty
appl_sorted_first = sorted(all_applicants, key=lambda x: (x[3], -x[2], x[0], x[1]))
appl_sorted_second = sorted(all_applicants, key=lambda x: (x[4], -x[2], x[0], x[1]))
appl_sorted_third = sorted(all_applicants, key=lambda x: (x[5], -x[2], x[0], x[1]))

faculties = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
faculties_dict = dict.fromkeys(faculties, [])
waiting_list = set([" ".join(x[0:2]) for x in all_applicants])


def admission_procedure(faculty, sortd_list, index):
    global faculties_dict
    global waiting_list
    accepted = []
    for x in sortd_list:
        if x[index] == faculty and " ".join(x[0:2]) in waiting_list:
            accepted.append(x[0:3])

    while len(accepted) > students_limit - len(faculties_dict[faculty]):
        accepted.pop()
    if len(accepted) > 0:
        accepted_names = set([" ".join(x[0:2]) for x in accepted])
        waiting_list -= accepted_names
        if len(faculties_dict[faculty]) > 0:
            accepted += faculties_dict[faculty]
            accepted = sorted(accepted, key=lambda x: (-x[2], x[0], x[1]))
        faculties_dict[faculty] = accepted


#  apll_sorted_first -> index=3, second -> index=4, third -> index=5
for faculty in faculties:
    admission_procedure(faculty, appl_sorted_first, 3)
for faculty in faculties:
    admission_procedure(faculty, appl_sorted_second, 4)
for faculty in faculties:
    admission_procedure(faculty, appl_sorted_third, 5)

for faculty in faculties:
    print(faculty)
    for x in faculties_dict[faculty]:
        print(' '.join(x[0:2]), end=' '), print(x[2])
    print('')
