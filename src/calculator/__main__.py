from .operations import Calculator
from .repl import run_repl

def main() -> None:
    run_repl(Calculator())

if __name__ == "__main__":
    main()
