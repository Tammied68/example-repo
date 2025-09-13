#Write a program that allows a user to register students for an exam venue.
#First, ask the user how many students are registering.
def collect_student_ids():
    try:
        num_students = int(input("Enter the number of students registering: "))
        student_ids = [] #Creates an empty list for the IDs and stores them here

        #Loop to retrieve the multiple IDs from each registrant
        for i in range(num_students): 
            student_id = input(f"Enter student ID for registrant {i + 1}: ")
            student_ids.append(student_id) #Adds one entry to the list during each loop cycle

        print("\nAll registered student IDs: ")
        for sid in student_ids: #Allows me to call sid to use the IDs in the list for other tasks
            print(f"{sid}.....................................")

        return student_ids #Return the list so it csn be used elsewhere
        
    except ValueError:
        print("❌ Please enter a valid number for the number of students." )

def save_ids_to_file(student_ids):
    try:
        with open("reg_form.txt", "w", encoding="utf-8") as file:
            for sid in student_ids:
                file.write(f"{sid}..............................\n")
        print("✅ Student IDs saved to reg_form.txt")
    except Exception as e:
        print(f"⚠️ Could not write to file: {e}")
       
# Call the function
student_ids = collect_student_ids()
save_ids_to_file(student_ids)
#I hope my reg_form.txt has text!!

