import sys
# takes an argument (subject) and prints the average score excluding that subject, to two decimals.

def grade(exclude):
    grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79,
    'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}

    '''
    # Print dictionary, get tuple values and place them in subject/grade
        for subject,grade in grades.items():
            print(f"{subject}: {grade}")
    '''
    filtered_grades = {}


    for subject, grade in grades.items():
        if subject != exclude:
            filtered_grades[subject] = grade

    # values = data , Prints entire dictionary of datas
    # print(filtered_grades.values())
    # Print all subjects (keys) from the filtered_grades dictionary
    # print(filtered_grades.keys())

    total = sum(filtered_grades.values())
    subject_count = len(filtered_grades)

    average = total / subject_count

    print(f"Average: {average: .2f}")



if __name__ == "__main__":
    exclude = sys.argv[1]
    exclude = exclude.capitalize()
    grade(exclude)