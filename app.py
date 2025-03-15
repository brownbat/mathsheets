from flask import Flask, render_template, request
import random, os

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page with the worksheet generation form.

    Displays all available operation types and problem count options.
    """
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """
    Generate a math worksheet based on form parameters.

    Accepts POST data with:
    - operation_type: The specific math operation category
    - num_problems: Number of problems to generate (10-50)

    Returns a rendered worksheet template with the generated problems.
    """
    operation_type = request.form.get('operation_type', 'addition_1digit')
    num_problems = int(request.form.get('num_problems', 20))

    # Get the base operation from the operation type
    operation = operation_type.split('_')[0]

    # Get problems based on the specific operation type
    problems = generate_problems_by_type(operation_type, num_problems)

    return render_template('worksheet.html', problems=problems, operation=operation)

def generate_problems_by_type(operation_type, num_problems):
    """
    Generate a list of math problems based on the specified operation type.

    Args:
        operation_type (str): The type of math operation (e.g., 'addition_1digit')
        num_problems (int): Number of problems to generate

    Returns:
        list: List of problem dictionaries, each with 'a', 'b', and 'op' keys

    Note:
        Prevents duplicate problems on the same page (20 problems per page)
    """
    problems = []

    # Keep track of problems on current page to avoid exact duplicates
    page_size = 20
    current_page_problems = set()

    for i in range(num_problems):
        # Start a new page tracking set every 20 problems
        if i % page_size == 0:
            current_page_problems = set()

        # Try to generate a unique problem (max 10 attempts)
        for attempt in range(10):
            # Generate problem based on operation type
            problem_data = generate_single_problem(operation_type)
            a, b = problem_data['a'], problem_data['b']
            op = problem_data['op']

            problem_key = (a, b, op)

            # Check if this exact problem is unique on this page
            if problem_key not in current_page_problems:
                # Add the problem to tracking
                current_page_problems.add(problem_key)
                problems.append(problem_data)
                break

    return problems

def generate_single_problem(operation_type):
    """
    Generates a single math problem based on the specified operation type.

    Args:
        operation_type (str): The specific category of math problem to generate
            (e.g., 'addition_1digit', 'subtraction_with_regrouping')

    Returns:
        dict: A problem dictionary with keys:
            - 'a': The first number in the problem (usually larger)
            - 'b': The second number in the problem
            - 'op': The operation symbol ('+', '-', '×', '÷')

    Note:
        Each operation type has specific constraints to ensure appropriate
        difficulty and educational value.
    """
    # Addition problems
    if operation_type == 'addition_1digit':
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        return {'a': a, 'b': b, 'op': '+'}

    elif operation_type == 'addition_2_1digit':
        a = random.randint(10, 99)
        b = random.randint(1, 9)
        return {'a': a, 'b': b, 'op': '+'}

    elif operation_type == 'addition_no_carrying':
        # Generate 2-digit numbers where a + b doesn't result in carrying
        a_tens = random.randint(1, 9)
        a_ones = random.randint(0, 9)
        b_tens = random.randint(1, 9)
        b_ones = random.randint(0, 9 - a_ones)  # Ensure ones digits don't sum to more than 9
        a = a_tens * 10 + a_ones
        b = b_tens * 10 + b_ones
        return {'a': a, 'b': b, 'op': '+'}

    elif operation_type == 'addition_with_carrying':
        # Generate 2-digit numbers where a + b results in carrying
        a_tens = random.randint(1, 9)
        a_ones = random.randint(1, 9)
        b_tens = random.randint(1, 9)
        b_ones = random.randint(10 - a_ones, 9)  # Ensure ones digits sum to more than 9
        a = a_tens * 10 + a_ones
        b = b_tens * 10 + b_ones
        return {'a': a, 'b': b, 'op': '+'}

    elif operation_type == 'addition_mixed':
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        return {'a': a, 'b': b, 'op': '+'}

    # Subtraction problems
    elif operation_type == 'subtraction_within_20':
        a = random.randint(1, 20)
        b = random.randint(1, a)
        return {'a': a, 'b': b, 'op': '-'}

    elif operation_type == 'subtraction_from_10s':
        a = random.randint(1, 9) * 10  # 10, 20, 30, etc.
        b = random.randint(1, 9)
        return {'a': a, 'b': b, 'op': '-'}

    elif operation_type == 'subtraction_no_regrouping':
        # Generate 2-digit numbers where a - b doesn't require regrouping
        a_tens = random.randint(1, 9)
        a_ones = random.randint(0, 9)
        b_tens = random.randint(1, a_tens)
        b_ones = random.randint(0, a_ones)  # Ensure b's ones digit is <= a's ones digit
        a = a_tens * 10 + a_ones
        b = b_tens * 10 + b_ones
        return {'a': a, 'b': b, 'op': '-'}

    elif operation_type == 'subtraction_with_regrouping':
        # Generate 2-digit numbers where a - b requires regrouping
        a_tens = random.randint(2, 9)  # At least 2 tens for regrouping
        a_ones = random.randint(0, 8)
        b_tens = random.randint(1, a_tens - 1)  # Ensure b's tens digit is < a's tens digit
        b_ones = random.randint(a_ones + 1, 9)  # Ensure b's ones digit is > a's ones digit
        a = a_tens * 10 + a_ones
        b = b_tens * 10 + b_ones
        return {'a': a, 'b': b, 'op': '-'}

    elif operation_type == 'subtraction_mixed':
        a = random.randint(10, 99)
        b = random.randint(1, a)
        return {'a': a, 'b': b, 'op': '-'}

    # Multiplication problems
    elif operation_type == 'multiplication_2_5_10':
        a = random.randint(1, 12)
        b = random.choice([2, 5, 10])
        return {'a': a, 'b': b, 'op': '×'}

    elif operation_type == 'multiplication_3_4_6':
        a = random.randint(1, 12)
        b = random.choice([3, 4, 6])
        return {'a': a, 'b': b, 'op': '×'}

    elif operation_type == 'multiplication_7_8_9':
        a = random.randint(1, 12)
        b = random.choice([7, 8, 9])
        return {'a': a, 'b': b, 'op': '×'}

    elif operation_type == 'multiplication_mixed':
        a = random.randint(1, 12)
        b = random.randint(1, 9)
        return {'a': a, 'b': b, 'op': '×'}

    elif operation_type == 'multiplication_2digit_1digit':
        a = random.randint(10, 99)
        b = random.randint(2, 9)
        return {'a': a, 'b': b, 'op': '×'}

    # Division problems
    elif operation_type == 'division_facts_10':
        quotient = random.randint(1, 10)
        b = random.randint(1, 9)
        a = b * quotient
        return {'a': a, 'b': b, 'op': '÷'}

    elif operation_type == 'division_facts_20':
        quotient = random.randint(1, 20)
        b = random.randint(1, 9)
        a = b * quotient
        return {'a': a, 'b': b, 'op': '÷'}

    elif operation_type == 'division_no_remainder':
        # Generate mostly 2-digit numbers divided by 1 digit with no remainder
        quotient = random.randint(1, 30)  # Back to original range, but kept the better name
        b = random.randint(2, 9)
        a = b * quotient
        return {'a': a, 'b': b, 'op': '÷'}

    elif operation_type == 'division_with_remainder':
        # Generate mostly 2-digit numbers divided by 1 digit with remainder
        quotient = random.randint(1, 20)  # Back to original range, but kept the better name
        b = random.randint(2, 9)
        remainder = random.randint(1, b - 1)
        a = b * quotient + remainder
        return {'a': a, 'b': b, 'op': '÷'}

    elif operation_type == 'division_by_2digit':
        # Generate reasonably sized numbers divided by 2-digit numbers
        b = random.randint(10, 20)  # Smaller 2-digit divisor (10-20 instead of 10-30)
        quotient = random.randint(2, 10)  # Smaller quotient (2-10 instead of 2-20)

        # 30% chance of having a remainder (reduced from 50%)
        if random.random() < 0.3:
            remainder = random.randint(1, b - 1)
            a = b * quotient + remainder
        else:
            a = b * quotient

        return {'a': a, 'b': b, 'op': '÷'}

    # Fallback to basic addition if operation type not recognized
    else:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        return {'a': a, 'b': b, 'op': '+'}

# Keep the original function for compatibility
def generate_problems(operation, num_problems, max_digits):
    problems = []
    max_num = 10 ** max_digits - 1

    # Keep track of problems on current page to avoid exact duplicates
    page_size = 20
    current_page_problems = set()

    for i in range(num_problems):
        # Start a new page tracking set every 20 problems
        if i % page_size == 0:
            current_page_problems = set()

        # Try to generate a unique problem (max 10 attempts)
        for attempt in range(10):
            if operation == 'addition':
                a = random.randint(1, max_num)
                b = random.randint(1, max_num)
                problem_key = (a, b, '+')

            elif operation == 'subtraction':
                a = random.randint(1, max_num)
                b = random.randint(1, max_num)
                # Ensure a >= b for elementary level
                if a < b:
                    a, b = b, a
                problem_key = (a, b, '-')

            elif operation == 'multiplication':
                a = random.randint(1, max_num)
                b = random.randint(1, max_num)
                problem_key = (a, b, '×')

            elif operation == 'division':
                # Create division problems with clean answers
                answer = random.randint(1, max_num // 10 or 1)
                b = random.randint(1, 12)
                a = b * answer
                problem_key = (a, b, '÷')

            # Check if this exact problem is unique on this page
            if problem_key not in current_page_problems:
                # Add the problem to tracking
                current_page_problems.add(problem_key)
                problems.append({'a': a, 'b': b, 'op': problem_key[2]})
                break

        # If we couldn't generate a unique problem after max attempts, use the last one anyway

    return problems

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
