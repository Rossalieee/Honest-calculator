# University Admission Procedure Project
This project is about creating program that decides which university candidates will be accepted based on given requirements. It is a great opportunity to practice loops and various mathematical operations, learn how to handle files and different types of collections such as lists (including nested lists) and dictionaries.

**Learned skills:** list comprehension, exceptions handling, lambda function, sorting lists, opening and creating files, operations on dictionary

## Project Stages
### Stage 1:
**About:** At this stage program take three imputs from the user (exam scores), calculates mean exam score and outputs it.

### Stage 2:
**About:**  Now program reads the numbers and output the mean score, as in the previous stage. Then if the mean score of the applicant is equal to or greater than 60.0, the program notifies the applicant of their acceptance to the university. Otherwise, informs them about their rejection.

### Stage 3:
**About:** A this stage the program ranks the potential students and determines who's going to get admitted based on the GPA (Grade Point Average).

**Objectives:**
* Read the first input, an N integer representing the total number of applicants.
* Read the second input, an M integer representing the number of applicants that should be accepted to the university.
* Read N lines from the input. Each line contains the first name, the last name, and the applicant's GPA. These values are separated by one whitespace character. A GPA is a floating-point number with two decimals.
* Output the `Successful applicants:` message.
* Output M lines for applicants with the top-ranking GPAs. Each line should contain the first and the last name of the applicant separated by a whitespace character. Successful applicants' names should be printed in descending order depending on the GPA — first, the applicant with the best GPA, then the second-best, and so on.
* If two applicants have the same GPA, rank them in alphabetical order using their full names

### Stage 4:
**About:** Now the program reads a file containing aplicants list. The list contains applicants names, GPU and their first, second and third department choice (Mathematics, Physics, Biotech, Chemistry, or the Engineering). The algorithm sorts the applicants according to their GPA and take into account their priorities: if the applicant doesn't score high enough to get accepted to the department of first priority, they'll participate in the rankings for the second priority, and so on.

### Stage 5:
**About:** At this stage instead of the GPU the program accepts applicants based on the finals, depending on the Department. For example, for a Physics department candidate, it would check the physics final exam.

**Objectives:**
* Read an N integer. This integer represents the maximum number of students for each department.
* Read the file. File structure: each line contains four columns with scores for particular exams: physics, chemistry, math, computer science (in this order). For example, `John Ritchie 89 45 83 75 Physics Engineering Mathematics`.
* Take into account the following exam results for the departments: physics for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science for the Engineering, and chemistry (again) for the Biotech department.
* Perform three stages of admission based on the applicants' priorities. Applicants should be ranked by their exam score and, in case they have the same score, their full name in alphabetic order. There should be no more than N accepted applicants for each department. One student can only be accepted to one department.
* Output the exam result for each student:

```
department_name
applicant1 exam1
applicant2 exam2
applicant3 exam3
```

### Stage 6:
**About:** Now some of the departments need more than one exam result for each applicant.

**Objectives:**
* Read an N integer from the input. This integer represents the maximum number of students for each department.
* Read the file
* Consider the following exam results for departments: physics and math for the Physics department, chemistry for the Chemistry department, math for the Mathematics department, computer science and math for the Engineering Department, chemistry and physics for the Biotech department.
* As in the previous stage, the exams are listed in the following order for each applicant: physics, chemistry, math, computer science.
* For the departments that need several exams, calculate the **mean score** and use it to rank the applicants. Otherwise, use the result for a single exam.
* Keep the rest of the steps the same as in the previous stage (once again, there should be no more than N accepted applicants for each department; use the same principles for sorting).
* Instead of printing the results (you may do it if you want), output the admission lists to files. Create a file for each department, name it %department_name%.txt, for example, physics.txt. Write the names of the students accepted to the department and their mean finals score to the corresponding file (one student per line).

### Stage 7:
**About:** Now the applicants can try to pass a special university admission exam. If the candidate's score on this exam is better than their mean score for the finals required by a Department, the university is ready to discard the results of the finals.
