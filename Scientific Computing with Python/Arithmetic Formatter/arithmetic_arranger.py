def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize the lines that will be used to store the formatted problems
    first_line = ""
    second_line = ""
    separator_line = ""
    answer_line = ""

    for problem in problems:
        # Split the problem string into its components (num1, operator, num2)
        components = problem.split()

        if len(components) != 3:
            return "Error: Invalid expression format."

        # Unpack the components into variables
        num1, operator, num2 = components

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if operator == "+":
            answer = int(num1) + int(num2)
        else:
            answer = int(num1) - int(num2)

        # Calculate the maximum length needed for formatting and format each line
        max_length = max(len(num1), len(num2)) + 2
        first_line += num1.rjust(max_length) + "    "
        second_line += operator + num2.rjust(max_length - 1) + "    "
        separator_line += "-" * max_length + "    "
        answer_line += str(answer).rjust(max_length) + "    "

    # Combine the formatted lines and remove any extra spaces at the end
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + separator_line.rstrip()
    
    if show_answers:
        arranged_problems += "\n" + answer_line.rstrip()

    return arranged_problems
