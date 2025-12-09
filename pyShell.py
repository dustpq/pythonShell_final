import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def start_shell():
    """Starts a simple interactive shell."""
    clear_screen()
    print("Welcome to the Simple Python Shell!")
    print("Type 'exit' to quit.")
    
    while True:
        try:
            command = input(">>> ")
            if command.lower() == 'exit':
                print("Exiting the shell. Goodbye!")
                break
            elif command.strip() == '':
                continue

            elif command.startswith('list'):
                list()

            elif command.startswith('cat'):
                parts = command.split(maxsplit=1)
                filename = parts[1] if len(parts) > 1 else None
                cat(filename)

            elif command.startswith('vim'):
                vim()

            else:
                try:
                    # Try to evaluate the command as an expression
                    result = eval(command)
                    if result is not None:
                        print(result)
                except SyntaxError:
                    # If it's not an expression, execute it as a statement
                    exec(command)
        except Exception as e:
            print(f"Error: {e}")

def list():
    """Lists current files in the directory."""
    files = os.listdir('.')
    for f in files:
        print(f)

def cat(filename=None):
    """Displays the content of a file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def vim(filename=None):
    """A simple text editor to create or edit files."""
    if filename is None:
        filename = input("Enter filename to create: ")
    print("Enter your text below. Type 'SAVE' on a new line to save and exit.")
    
    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)
    
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(lines))
        print(f"File '{filename}' saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_shell()