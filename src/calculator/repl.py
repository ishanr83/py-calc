from typing import Callable
from .operations import Calculator, CalculatorError, DivisionByZeroError

PROMPT = "> "

def banner() -> str:
    return "Calculator REPL. Commands: add|sub|mul|div <a> <b>  | exit"

def bye() -> str:
    return "Bye!"

def _parse_two_numbers(parts: list[str]) -> tuple[float, float]:
    if len(parts) != 3:
        raise ValueError("Usage: <op> <num1> <num2>")
    try:
        a = float(parts[1])
        b = float(parts[2])
    except ValueError:
        raise ValueError("Numbers must be numeric.")
    return a, b

def run_repl(
    calc: Calculator,
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    # banner (covered by direct call + run path)
    output_fn(banner())
    while True:
        try:
            line = input_fn(PROMPT).strip()
        except (EOFError, KeyboardInterrupt):
            output_fn(bye())
            break

        if not line:
            continue
        if line.lower() in {"exit", "quit", "q"}:
            output_fn(bye())
            break

        parts = line.split()
        op = parts[0].lower()
        try:
            if op in {"add", "sub", "mul", "div"}:
                a, b = _parse_two_numbers(parts)
                if op == "add":
                    result = calc.add(a, b)
                elif op == "sub":
                    result = calc.sub(a, b)
                elif op == "mul":
                    result = calc.mul(a, b)
                else:
                    result = calc.div(a, b)
                output_fn(str(result))
            else:
                output_fn("Unknown command. Use add|sub|mul|div or exit")
        except DivisionByZeroError as e:
            output_fn(f"Error: {e}")
        except (ValueError, CalculatorError) as e:
            output_fn(f"Error: {e}")
