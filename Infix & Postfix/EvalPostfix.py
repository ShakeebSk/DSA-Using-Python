def evaluate_postfix(expression):
    stack = []  # Initialize an empty stack

    for char in expression:
        if char.isdigit():
            # If the character is a digit, push it onto the stack
            stack.append(int(char))
        else:
            # If it's an operator, pop the top two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Evaluate the expression based on the operator
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            else:
                raise ValueError(f"Invalid operator: {char}")

            # Push the result back onto the stack
            stack.append(result)

    # The final result should be the only element left in the stack
    return stack[0]

# Example usage:
postfix_expression = "2 3 1 * + 9 -"
result = evaluate_postfix(postfix_expression)
print(f"Postfix expression: {postfix_expression}")
print(f"Result: {result}")
