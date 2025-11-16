# Bubble Sort implementation - I remember this being my first sorting algorithm!
def sort_names_bubble(name_list):
    n = len(name_list)  # storing length for readability
    for i in range(n):
        # TODO: maybe optimize this later with a flag for early termination
        for j in range(n - i - 1):  # bubble the largest to the end
            if name_list[j] > name_list[j + 1]:
                # classic swap - could use temp variable but this looks cleaner
                name_list[j], name_list[j + 1] = name_list[j + 1], name_list[j]

# Insertion sort for test scores
def sort_scores_insertion(score_array):
    for i in range(1, len(score_array)):
        current_val = score_array[i]  # the value we're trying to insert
        position = i - 1
        
        # shift elements to the right until we find the correct spot
        while position >= 0 and score_array[position] > current_val:
            score_array[position + 1] = score_array[position]
            position -= 1
        
        score_array[position + 1] = current_val  # insert the value

# Quick sort with recursion counter - let's see how many calls this makes!
def quick_sort_prices(price_arr, start, end, call_counter):
    if start < end:
        call_counter[0] += 1  # increment our counter
        pivot_index = partition_array(price_arr, start, end)
        
        # recursively sort left and right partitions
        quick_sort_prices(price_arr, start, pivot_index - 1, call_counter)  
        quick_sort_prices(price_arr, pivot_index + 1, end, call_counter)

def partition_array(arr, start_idx, end_idx):
    pivot_element = arr[end_idx]  # always use last element as pivot
    smaller_element_index = start_idx - 1  # index of smaller element
    
    for current_idx in range(start_idx, end_idx):
        if arr[current_idx] <= pivot_element:
            smaller_element_index += 1
            # swap elements
            arr[smaller_element_index], arr[current_idx] = arr[current_idx], arr[smaller_element_index]
    
    # place pivot in correct position
    arr[smaller_element_index + 1], arr[end_idx] = arr[end_idx], arr[smaller_element_index + 1]
    return smaller_element_index + 1

def show_menu():  # renamed to be more descriptive
    print("\n=== Sorting Algorithms Demo ===")  # changed title slightly
    print("1. Bubble Sort - Student Names")
    print("2. Insertion Sort - Test Scores") 
    print("3. Quick Sort - Book Prices")
    print("4. Exit")
    print("-" * 35)  # added a separator line

def main():
    # student data - mix of Bhutanese names from my class
    student_names = ["Sanjuck", "Drakpa", "Gyetshay", "Jamyang", "Sangay", "Sonam",
                    "Bishal", "Tshering", "wangchuk", "Choki", "Palden", "Thinley", 
                    "Tshagay", "Phuntsho", "Jigme"]

    # some test scores from recent exams
    test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 62]

    # book prices in Ngultrum - from the campus bookstore
    book_prices = [499, 299, 699, 199, 899, 329, 549, 219, 469, 389, 779, 469, 699, 539, 275]

    # keep original copies for display purposes
    backup_names = student_names[:]  # using slice notation instead of copy()
    backup_scores = test_scores[:]
    backup_prices = book_prices[:]

    program_running = True  # using a flag instead of while True
    while program_running:
        show_menu()
        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '1':
            print(f"\nOriginal student names: {backup_names}")
            sort_names_bubble(student_names)
            print(f"Names after bubble sort: {student_names}")
            
        elif user_choice == '2':
            print(f"\nOriginal test scores: {backup_scores}")
            sort_scores_insertion(test_scores)
            print(f"Scores after insertion sort: {test_scores}")
            
            # bonus: show top performers
            print("\n🏆 Top 5 Performers:")
            top_scores = sorted(test_scores, reverse=True)  # sort in descending order
            for rank in range(5):  # show top 5
                print(f"  {rank + 1}. {top_scores[rank]} points")
                
        elif user_choice == '3':
            print(f"\nOriginal book prices: {backup_prices}")
            recursion_tracker = [0]  # using list to track recursive calls
            quick_sort_prices(book_prices, 0, len(book_prices) - 1, recursion_tracker)
            print(f"Prices after quick sort: {book_prices}")
            print(f"📊 Total recursive calls made: {recursion_tracker[0]}")
            
        elif user_choice == '4':
            print("\nThanks for exploring sorting algorithms with me! 👋")
            program_running = False
            
        else:
            print("❌ Invalid choice. Please select 1-4.")

        # ask if user wants to continue (only if not exiting)
        if program_running:
            continue_choice = input("\nWould you like to try another sorting algorithm? (y/n): ")
            if continue_choice.lower() not in ['y', 'yes']:
                print("Thanks for using the sorting demo! Hope you learned something new 📚")
                program_running = False

# run the program
if __name__ == "__main__":
    main()