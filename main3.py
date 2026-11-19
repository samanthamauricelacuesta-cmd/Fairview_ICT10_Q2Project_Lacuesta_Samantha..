from pyscript import document, display

grade7 = {'Pupinia Poppins', 'Poppy Larpin', 'Papoy Pans', 'Papi Candy'}
grade8 = {'Glass Peyn', 'Jen Nestine', 'Gen Zee', 'Kat Cato'}
grade9 = {'Anne Cleaves', 'Jane Yourearly', 'Seymour Last', 'Henry Theeight'}
grade10 = {'Vivienne Westwood', 'Maree Coleman', 'Zuvee Mamah', 'Peter Pavitir'}

# Combine all grades into a base set
all_students = grade7.union(grade8, grade9, grade10)

def verify_candidate(e):
    # Get and format input values cleanly
    first_name = document.getElementById("first_name").value.strip().capitalize()
    last_name = document.getElementById("last_name").value.strip().capitalize()
    full_name = f"{first_name} {last_name}"

    # 2. Process data logically: Add candidate if fields aren't empty
    if first_name and last_name:
        all_students.add(full_name)

    # Compute variables before rendering them in output strings
    total_members = len(all_students)
    student_list = ", ".join(sorted(all_students))

    #  Display results safely
    display(f"""
        List of Students:
        {student_list}
        Total Number of Students:{total_members}
    """, target="result", append=False)