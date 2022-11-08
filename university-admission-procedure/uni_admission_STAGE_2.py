from statistics import mean

exams_mean = mean((int(input()), int(input()), int(input())))
print(exams_mean)

if exams_mean >= 60:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")
