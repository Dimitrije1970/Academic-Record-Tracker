class Node:
    def __init__(self, subject_code, grade):
        self.subject_code = subject_code
        self.grade = grade
        self.next = None


class LinkedList:
    def __init__(self, length):
        self.length = length
        self.head = None

    def addSort(self, subject_list, grade):
        new_node = Node(subject_list, grade)

        temp = self.head
        if temp is None:
            self.head = new_node
            new_node.next = self.head
            self.length += 1
            return
        if new_node.subject_code < temp.subject_code and temp.next == temp:
            self.head = new_node
            new_node.next = temp
            temp.next = self.head
            self.length += 1
            return
        if new_node.subject_code < temp.subject_code and temp.next != temp:
            tail = self.head
            while True:
                if tail.next == self.head:
                    break
                tail = tail.next

            new_node.next = temp
            self.head = new_node
            tail.next = new_node
            self.length += 1
            return

        while temp.next.subject_code < new_node.subject_code:
            temp = temp.next

            if temp.next == self.head:
                break

        new_node.next = temp.next
        temp.next = new_node

        self.length += 1

    def removeSubject(self, subject_to_remove):
        temp = self.head

        if temp is None:
            return
        if temp.subject_code == subject_to_remove and temp.next == temp:
            self.head = None
            return

        node = None
        if temp.subject_code == subject_to_remove:
            while temp.next is not self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = temp.next

        while (temp.next != self.head and temp.next.subject_code != subject_to_remove):
            temp = temp.next

        if temp.next.subject_code == subject_to_remove:
            node = temp.next
            temp.next = node.next

        self.length -= 1

    def printList(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(f"[{temp.subject_code},{temp.grade}]", end="->")
                temp = temp.next
                if temp == self.head:
                    break
        print('\n')

    def isSubjectIn(self, subject_code):
        temp = self.head
        if self.head is not None:
            while True:
                if temp.subject_code == subject_code:
                    return True
                temp = temp.next
                if temp == self.head:
                    break

        return False


class Student:
    def __init__(self, index_num, linked_list):
        self.index_num = index_num
        self.linked_list = linked_list


print('1. Dodaj novog studenta.')
print('2. Dodaj polozeni predmet za studenta.')
print('3. Prikazi predmet sa odredjenom ocenom.')
print('4. Ponisti polozeni predmet za studenta.')
print('5. Ponisti sve polozene predmete za studenta.')
print('6. Dohvati broj polozenih predmeta za studenta.')
print('7. Ispisi polozene predmete za studenta.')
print('8. Unija polozenih ispita 2 zadata studenta.')
print('0. Prekini program.')

choice = 0
max_students = 100

try:
    max_students = int(input('Unesi maksimalan broj studenata:'))
    choice = int(input('Unesi redni broj opcije:'))
except ValueError:
    print('Doslo je do greske prilikom unosa')
student_list = list()

while True:
    if choice == 0:
        break
    elif choice == 1:
        index_num = int(input('Unesi broj indeksa:'))
        indexes = [student.index_num for student in student_list]
        if index_num not in indexes and len(indexes) < max_students:
            subject_list = LinkedList(0)
            student_list.append(Student(index_num, subject_list))
        else:
            print('Vec postoji student sa ovim brojem indeksa ili je ispunjen maksimalan broj studenata.')
    elif choice == 2:
        index_num = int(input('Unesi broj indeksa studenta za kog se unosi predmet: '))
        indexes = [student.index_num for student in student_list]
        if index_num in indexes:
            subject_code = input('Unesi sifru predmeta:')
            grade = int(input('Unesi ocenu:'))

            if grade < 5 or grade > 10:
                print('Lose uneta ocena.')
            elif grade == 5:
                print('Student je pao premdet.')
            else:
                current_student = student_list[indexes.index(index_num)]
                temp_list = current_student.linked_list

                if not temp_list.isSubjectIn(subject_code):
                    temp_list.addSort(subject_code, grade)
                    # temp_list.printList()
                else:
                    print("Vec je unet premdet sa tom sifrom.")

        else:
            print('Nema studenta sa tim brojem indeksa.')
    elif choice == 3:
        grade_search = int(input('Koja ocena se prikazuje:'))
        for student in student_list:
            temp_student = student.index_num
            temp_node = student.linked_list.head

            if temp_node is None:
                continue

            while True:
                if temp_node.grade == grade_search:
                    print(f"{temp_student}/{temp_node.subject_code}/{temp_node.grade}")

                temp_node = temp_node.next
                if temp_node == student.linked_list.head:
                    break
    elif choice == 4:
        index_num = int(input('Unesi broj indeksa studenta za kog se ponistava predmet:'))
        indexes = [student.index_num for student in student_list]
        if index_num in indexes:
            subject_to_remove = input('Unesi predmet koji se ponistava:')

            current_student = student_list[indexes.index(index_num)]
            temp_list = current_student.linked_list

            if not temp_list.isSubjectIn(subject_to_remove):
                print('Nema predmeta sa ovom sifrom.')
            else:
                temp_list.removeSubject(subject_to_remove)
                # temp_list.printList()

        else:
            print('Ne postoji takav student.')
    elif choice == 5:
        index_num = int(input('Unesi broj indeksa studenta za kog se ponistavaju svi predmeti:'))
        indexes = [student.index_num for student in student_list]
        if index_num in indexes:
            current_student = student_list[indexes.index(index_num)]
            current_student.linked_list = LinkedList(0)
            # current_student.linked_list.printList()
        else:
            print('Ne postoji takav student.')
    elif choice == 6:
        index_num = int(input('Unesi broj indeksa studenta za kog se dohvata broj polozenih predmeta:'))
        indexes = [student.index_num for student in student_list]
        if index_num in indexes:
            current_student = student_list[indexes.index(index_num)]
            print(current_student.linked_list.length)
        else:
            print('Ne postoji takav student.')
    elif choice == 7:
        index_num = int(input('Unesi broj indeksa studenta za kog se ispisuju svi polozeni predmeti:'))
        indexes = [student.index_num for student in student_list]
        if index_num in indexes:
            current_student = student_list[indexes.index(index_num)]
            current_student.linked_list.printList()
        else:
            print('Ne postoji takav student.')
    elif choice == 8:
        index_num_1 = int(input('Unesi broj indeksa prvog studenta za ispisivanje unije:'))
        index_num_2 = int(input('Unesi broj indeksa drugog studenta za ispisivanje unije:'))
        indexes = [student.index_num for student in student_list]
        if index_num_1 in indexes and index_num_2 in indexes:
            first_set = set()
            second_set = set()

            first_head = student_list[indexes.index(index_num_1)].linked_list.head
            for i in range(student_list[indexes.index(index_num_1)].linked_list.length):
                first_set.add(first_head.subject_code)
                first_head = first_head.next


            second_head = student_list[indexes.index(index_num_2)].linked_list.head
            for i in range(student_list[indexes.index(index_num_2)].linked_list.length):
                second_set.add(second_head.subject_code)
                second_head = second_head.next


            print(f'Unija polozenih predmeta za indekse {index_num_1} i {index_num_2} je: ' , *set.union(first_set, second_set))

        else:
            print('Ne postoji takav student.')

    try:
        choice = int(input('Unesi redni broj opcije:'))
    except ValueError:
        print('Doslo je do greske prilikom unosa')
