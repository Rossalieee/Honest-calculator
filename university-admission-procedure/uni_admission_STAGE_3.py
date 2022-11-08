appl_num_total = int(input())
appl_num_limit = int(input())

all_applicants = []
acceptance_msg = "Successful applicants:"


def floatify(num):
    try:
        return float(num)
    except ValueError:
        return num
    
    
for i in range(appl_num_total):
    all_applicants.append(input().split())

all_applicants = [[floatify(x) for x in row] for row in all_applicants]

applicants_sorted = sorted(all_applicants, key=lambda x: (-x[2], x[0], x[1]))

accepted_appl = applicants_sorted[0:appl_num_limit]

print(acceptance_msg)

for applicants in accepted_appl:
    print(" ".join(applicants[0: 2]))
