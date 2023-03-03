# ImplementingAlgorithms
assignment #7 for algorithms
The program reads a sequence of student logs from a file and calculates the maximum, most recent, and average student status based on their page IDs and submission scores. The output is a series of sorted student status reports, with each report containing the student's ID, lowest page ID, latest page ID, and average submission score.

The program consists of three main functions:

read_logs: Parses the input file and stores the logs for each student in a dictionary.

Algorithmic runtime: O(n), where n is the number of logs.
calculate_student_statuses: Calculates the student statuses based on their logs and returns a list of tuples containing the student ID, lowest page ID, latest page ID, and average submission score for each student.

Algorithmic runtime: O(n), where n is the number of students.
print_student_statuses: Prints the student statuses in the desired format.

Algorithmic runtime: O(n log n), where n is the number of students (due to sorting).