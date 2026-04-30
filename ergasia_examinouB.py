club_info_robotics = ("Λέσχη Ρομποτικής", "κ. Ιωάννου", "Δευτέρα")
club_info_theater = ("Λέσχη Θεάτρου", "κ. Παπαδοπούλου", "Τετάρτη")
club_info_music = ("Λέσχη Μουσικής", "κ. Νικολάου", "Παρασκευή")
club_info_sports = ("Λέσχη Αθλητισμού", "κ. Δημητρίου", "Πέμπτη")

students_robotics = {"Νίκος", "Μαρία", "Γιώργος"}
students_theater = {"Ελένη", "Κώστας", "Μαρία"}
students_music = {"Άννα", "Δημήτρης"}
students_sports = {"Γιάννης", "Σοφία", "Νίκος"}

all_clubs = [
    [club_info_robotics, students_robotics],
    [club_info_theater, students_theater],
    [club_info_music, students_music],
    [club_info_sports, students_sports]
]

# --- ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ ---
while True:
    print("\n" + "="*30)
    print("      ΜΕΝΟΥ ΕΠΙΛΟΓΩΝ")
    print("="*30)
    print("1. Εμφάνιση όλων των λεσχών")
    print("2. Εμφάνιση των στοιχείων μιας λέσχης")
    print("3. Εμφάνιση των μαθητών μιας λέσχης")
    print("4. Αναζήτηση μαθητή σε όλες τις λέσχες")
    print("5. Προσθήκη μαθητή σε συγκεκριμένη λέσχη")
    print("6. Διαγραφή μαθητή από συγκεκριμένη λέσχη")
    print("7. Εμφάνιση όλων των μοναδικών μαθητών")
    print("8. Εμφάνιση κοινών μαθητών μεταξύ δύο λεσχών")
    print("9. Εμφάνιση μαθητών που ανήκουν μόνο σε μία λέσχη")
    print("10. Έξοδος")
    
    choice = input("\nΕπιλέξτε λειτουργία (1-10): ")

    match choice:
    case "1":
            print("\n--- ΛΙΣΤΑ ΟΛΩΝ ΤΩΝ ΛΕΣΧΩΝ ---")
            for club in all_clubs:
                # club[0] είναι το tuple με τις πληροφορίες, club[0][0] είναι το όνομα
                print(f"- {club[0][0]}")

        case "2":
            print("\n--- ΣΤΟΙΧΕΙΑ ΛΕΣΧΗΣ ---")
            print("1. Ρομποτική, 2. Θέατρο, 3. Μουσική, 4. Αθλητισμός")
            idx = input("Επιλέξτε αριθμό λέσχης: ")
            if idx.isdigit() and 1 <= int(idx) <= 4:
                club_index = int(idx) - 1
                info = all_clubs[club_index][0] # Παίρνουμε το tuple
                print(f"Όνομα: {info[0]}")
                print(f"Υπεύθυνος: {info[1]}")
                print(f"Ημέρα: {info[2]}")
            else:
                print("Λάθος επιλογή!")

        case "3":
            print("\n--- ΜΑΘΗΤΕΣ ΛΕΣΧΗΣ ---")
            idx = input("Επιλέξτε αριθμό λέσχης (1-4): ")
            if idx.isdigit() and 1 <= int(idx) <= 4:
                students = all_clubs[int(idx)-1][1] # Παίρνουμε το set με τους μαθητές
                print(f"Μαθητές: {', '.join(students) if students else 'Δεν υπάρχουν μαθητές'}")
            else:
                print("Λάθος επιλογή!") 
        case "4":
            print("\n--- ΑΝΑΖΗΤΗΣΗ ΜΑΘΗΤΗ ---")
            search_name = input("Δώστε το όνομα του μαθητή: ")
            found = False
            for club in all_clubs:
                if search_name in club[1]: # club[1] είναι το set των μαθητών
                    print(f"Ο/Η {search_name} συμμετέχει στη: {club[0][0]}")
                    found = True
            if not found:
                print("Ο μαθητής δεν βρέθηκε σε καμία λέσχη.")

        case "5":
            print("\n--- ΠΡΟΣΘΗΚΗ ΜΑΘΗΤΗ ---")
            print("1. Ρομποτική, 2. Θέατρο, 3. Μουσική, 4. Αθλητισμός")
            idx = input("Σε ποια λέσχη (1-4); ")
            if idx.isdigit() and 1 <= int(idx) <= 4:
                new_student = input("Όνομα μαθητή για προσθήκη: ")
                all_clubs[int(idx)-1][1].add(new_student)
                print(f"Ο/Η {new_student} προστέθηκε επιτυχώς!")
            else:
                print("Λάθος επιλογή!")

        case "6":
            print("\n--- ΔΙΑΓΡΑΦΗ ΜΑΘΗΤΗ ---")
            print("1. Ρομποτική, 2. Θέατρο, 3. Μουσική, 4. Αθλητισμός")
            idx = input("Από ποια λέσχη (1-4); ")
            if idx.isdigit() and 1 <= int(idx) <= 4:
                del_student = input("Όνομα μαθητή για διαγραφή: ")
                if del_student in all_clubs[int(idx)-1][1]:
                    all_clubs[int(idx)-1][1].remove(del_student)
                    print(f"Ο/Η {del_student} διαγράφηκε.")
                else:
                    print("Ο μαθητής δεν υπάρχει σε αυτή τη λέσχη.")
            else:
                print("Λάθος επιλογή!")
        case "7":
            print("\n--- ΟΛΟΙ ΟΙ ΜΟΝΑΔΙΚΟΙ ΜΑΘΗΤΕΣ ΤΟΥ ΣΧΟΛΕΙΟΥ ---")
            # Δημιουργούμε ένα κενό σύνολο και προσθέτουμε όλα τα μέλη (Union)
            all_unique_students = set()
            for club in all_clubs:
                all_unique_students = all_unique_students | club[1]
            
            print(f"Συνολικό πλήθος μαθητών: {len(all_unique_students)}")
            print(f"Ονόματα: {', '.join(all_unique_students)}")

        case "8":
            print("\n--- ΚΟΙΝΟΙ ΜΑΘΗΤΕΣ ΜΕΤΑΞΥ ΔΥΟ ΛΕΣΧΩΝ ---")
            print("1. Ρομποτική, 2. Θέατρο, 3. Μουσική, 4. Αθλητισμός")
            c1 = int(input("Επιλέξτε την πρώτη λέσχη (1-4): ")) - 1
            c2 = int(input("Επιλέξτε τη δεύτερη λέσχη (1-4): ")) - 1
            
            # Χρήση τομής (&) για την εύρεση κοινών στοιχείων
            common = all_clubs[c1][1] & all_clubs[c2][1]
            
            if common:
                print(f"Κοινοί μαθητές: {', '.join(common)}")
            else:
                print("Δεν υπάρχουν κοινοί μαθητές μεταξύ αυτών των λεσχών.")

        case "9":
            print("\n--- ΜΑΘΗΤΕΣ ΠΟΥ ΑΝΗΚΟΥΝ ΜΟΝΟ ΣΕ ΜΙΑ ΛΕΣΧΗ ---")
            idx = int(input("Επιλέξτε λέσχη (1-4): ")) - 1
            target_club = all_clubs[idx][1]
            
            # Εύρεση όλων των άλλων μαθητών
            other_students = set()
            for i in range(len(all_clubs)):
                if i != idx:
                    other_students = other_students | all_clubs[i][1]
            
            # Χρήση διαφοράς (-) για να βρούμε τους αποκλειστικούς
            exclusive = target_club - other_students
            
            if exclusive:
                print(f"Μαθητές μόνο στη {all_clubs[idx][0][0]}: {', '.join(exclusive)}")
            else:
                print("Όλοι οι μαθητές αυτής της λέσχης συμμετέχουν και κάπου αλλού.")
        case "10":
            print("Έξοδος από την εφαρμογή...")
            break
        case _:
            print("Η λειτουργία αυτή θα υλοποιηθεί στο επόμενο στάδιο.")
