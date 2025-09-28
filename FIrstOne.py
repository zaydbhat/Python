def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count


# Main execution
if __name__ == "__main__":
    # Get test scores from user
    print("Enter test scores one by one (type 'done' when finished):")
    test_scores = []

    while True:
        user_input = input("Enter a test score: ")
        if user_input.lower() == 'done':
            break
        try:
            score = float(user_input)
            test_scores.append(score)
            print(f"Added score: {score}")
        except ValueError:
            print("Please enter a valid number or 'done' to finish")

    # Calculate and display average
    if test_scores:
        average_score = calculate_average(test_scores)
        print(f"\nAll scores: {test_scores}")
        print(f"The average test score is: {average_score:.2f}")
    else:
        print("No scores were entered.")