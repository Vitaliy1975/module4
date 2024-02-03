import sys
from pathlib import Path
from colorama import Fore

def main():
    path=sys.argv[1]
    directory=Path(path)
    try:
        if directory.exists() and directory.is_dir():
            for sub in directory.iterdir():
                if sub.is_dir():
                    print(f"{Fore.GREEN}{sub}{Fore.RESET}")
                elif sub.is_file():
                    print(f"{Fore.YELLOW}{sub}{Fore.RESET}")
        else:
            print(f"'{directory}' is not a directory or '{directory}' does not exist.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
