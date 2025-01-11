# InputData.py
def write_data_to_file(filename, data):
    """Writes a list of integers to a file."""
    try:
        with open(filename, 'w') as file:
            for value in data:
                file.write(f"{value}\n")
        print(f"Data successfully written to {filename}.")
    except Exception as e:
        print(f"Error writing data to file: {e}")

def get_input_data():
    """Prompts the user for input data and returns it as a list of integers."""
    print("Please enter data values (one per line). Type 'done' when finished.")
    input_data = []
    while True:
        user_input = input("Enter a value: ")
        if user_input.lower() == 'done':
            break
        try:
            value = int(user_input)
            input_data.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer or 'done' to finish.")
    return input_data
