import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def start_shell():
    """Starts a simple interactive shell."""
    clear_screen()
    os.chdir("shellHome")
    print("Welcome to the pyShell!")
    print("Type 'help' for a list of commands.")
    print("Type 'exit' to quit.")
    
    while True:
        try:
            command = input(">>> ")
            if command.lower() == 'exit':
                print("Exiting the shell. Goodbye!")
                break
            elif command.strip() == '':
                continue
            
            elif command.startswith('help'):
                help()

            elif command.startswith('list'):
                list()

            elif command.startswith('cat'):
                parts = command.split(maxsplit=1)
                filename = parts[1] if len(parts) > 1 else None
                if filename is None:
                    print("Usage: cat <filename>")
                else:
                    cat(filename)

            elif command.startswith('vim'):
                parts = command.split(maxsplit=1)
                filename = parts[1] if len(parts) > 1 else None
                vim(filename)

            elif command.startswith('mkdir'):
                parts = command.split(maxsplit=1)
                if len(parts) < 2:
                    print("Usage: mkdir <dirname>")
                else:
                    mkdir(parts[1])

            elif command.startswith('rmdir'):
                parts = command.split(maxsplit=1)
                if len(parts) < 2:
                    print("Usage: rmdir <dirname>")
                else:
                    rmdir(parts[1])

            elif command.startswith('rm'):
                parts = command.split(maxsplit=1)
                if len(parts) < 2:
                    print("Usage: rm <filename>")
                else:
                    rm(parts[1])

            elif command.startswith('touch'):
                parts = command.split(maxsplit=1)
                if len(parts) < 2:
                    print("Usage: touch <filename>")
                else:
                    touch(parts[1])

            elif command.startswith('cd'):
                parts = command.split(maxsplit=1)
                if len(parts) < 2:
                    print("Usage: cd <dirname>")
                else:
                    cd(parts[1])

            elif command == 'cwd':
                print(cwd())

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
        

def help():
    """Displays help information."""
    help_text = """
    Available pyShell Commands:
    - list              : Lists files in the current directory.
    - cat <filename>    : Displays the content of the specified file.
    - vim <filename>    : Opens a simple text editor to create or edit a file.
    - mkdir <dirname>   : Creates a new directory.
    - rmdir <dirname>   : Removes a directory.
    - rm <filename>     : Removes a file.
    - touch <filename>  : Creates an empty file.
    - cd <dirname>      : Changes the current directory.
    - help              : Displays this help message.
    - exit              : Exits the shell.
    You can also enter any valid Python expression or statement.
    """
    print(help_text)

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
    print("Enter your text below. Type ':SAVE' on a new line to save and exit.")
    
    lines = []
    while True:
        line = input()
        if line == ':SAVE':
            break
        lines.append(line)
    
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(lines))
        print(f"File '{filename}' saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

def mkdir(dirname):
    """Creates a new directory."""
    try:
        os.makedirs(dirname, exist_ok=True)
    except Exception as e:
        print(f"Error: {e}")

def rmdir(dirname):
    """Removes a directory."""
    try:
        os.rmdir(dirname)
    except Exception as e:
        print(f"Error: {e}")

def rm(filename):
    """Removes a file."""
    try:
        os.remove(filename)
    except Exception as e:
        print(f"Error: {e}")

def touch(filename):
    """Creates an empty file."""
    try:
        with open(filename, 'a'):
            os.utime(filename, None)
    except Exception as e:
        print(f"Error: {e}")

def cd(dirname):
    """Changes the current directory."""
    try:
        os.chdir(dirname)
    except Exception as e:
        print(f"Error: {e}")

def cwd():
    """Returns the current working directory."""
    return os.getcwd()

if __name__ == "__main__":
    start_shell()