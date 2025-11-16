def find_student_by_id(student_list, target_id):
    # Keep track of how many times we check
    comparison_count = 0 
    
    # Going through each student one by one
    for index in range(len(student_list)):
        comparison_count += 1
        if student_list[index] == target_id:
            # Found it! Return position (1-based) and how many checks we did
            return index + 1, comparison_count
    
    # Didn't find the student ID anywhere
    return -1, comparison_count


def search_score_binary(score_list, target_score):
    left_boundary = 0
    right_boundary = len(score_list) - 1
    checks = 0
    
    while left_boundary <= right_boundary:
        # Calculate middle point - this is the key to binary search
        middle = (left_boundary + right_boundary) // 2
        checks += 1
        
        if score_list[middle] == target_score:
            return middle + 1, checks  # Found it!
        elif score_list[middle] < target_score:
            # Target is in the right half
            left_boundary = middle + 1  
        else:
            # Target is in the left half
            right_boundary = middle - 1 
    
    return -1, checks  # Not found


def display_menu():
    print("\n=== Searching Algorithms Menu ===")
    print("Select a search operation (1-3):")
    print("1. Linear Search - Find Student ID")  
    print("2. Binary Search - Find Score")
    print("3. Exit program")


def main():
    # Sample student IDs - notice they're not sorted
    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012, 1013,
                   1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022]
    
    # These scores are already sorted - important for binary search!
    sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88, 90, 92, 95, 98]

    program_running = True
    while program_running:
        display_menu()
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            # Linear search option
            print("Searching in the list:", student_ids)
            try:
                search_id = int(input("Enter Student ID to search: "))
                pos, comparisons = find_student_by_id(student_ids, search_id)
                
                if pos != -1:
                    print(f"Result: Student ID {search_id} found at position {pos}")
                else:
                    print("Result: Student ID not found")
                print(f"Comparisons made: {comparisons}")
                
            except ValueError:
                print("Please enter a valid number.")

        elif user_choice == "2":
            # Binary search option
            print("Sorted scores:", sorted_scores)
            try:
                search_score = int(input("Enter score to search: "))
                pos, comparisons = search_score_binary(sorted_scores, search_score)
                
                if pos != -1:
                    print(f"Result: Score {search_score} found at position {pos}")
                else:
                    print("Result: Score not found")
                print(f"Comparisons made: {comparisons}")
                
            except ValueError:
                print("Please enter a valid number.")
                
        elif user_choice == "3":
            print("Goodbye!")
            program_running = False  
            
        else:
            print("Invalid choice. Please try again.")


# This is where the program starts
if __name__ == "__main__":
    main()