from calculator.operations import Calculator
from calculator.repl import run_repl

def make_io(lines):
    """lines: iterable of inputs; returns (input_fn, output_fn, outputs_list)."""
    it = iter(lines)
    outputs = []
    def input_fn(prompt):
        try:
            return next(it)
        except StopIteration:
            # Simulate Ctrl+D (EOF)
            raise EOFError
    def output_fn(s):
        outputs.append(s)
    return input_fn, output_fn, outputs

def test_repl_happy_path_add_mul():
    input_fn, output_fn, out = make_io(["add 2 3", "mul 3 4", "exit"])
    run_repl(Calculator(), input_fn, output_fn)
    assert "Calculator REPL." in out[0]
    assert "5.0" in out       # result of add
    assert "12.0" in out      # result of mul
    assert out[-1] == "Bye!"  # graceful exit

def test_repl_validation_unknown_zero():
    # Covers: empty line, unknown command, non-numeric, division by zero, quit
    input_fn, output_fn, out = make_io(["", "foo", "add two 2", "div 5 0", "q"])
    run_repl(Calculator(), input_fn, output_fn)
    assert any("Unknown command" in x for x in out)
    assert any("Error:" in x and "numeric" in x for x in out)
    assert any("Error:" in x and "Division by zero" in x for x in out)
    assert out[-1] == "Bye!"

def test_repl_eof_path():
    # No inputs at all -> EOF on first prompt
    input_fn, output_fn, out = make_io([])
    run_repl(Calculator(), input_fn, output_fn)
    assert out[-1] == "Bye!"

def test_repl_keyboard_interrupt_path():
    # Simulate Ctrl+C on first prompt
    def input_fn(_prompt):
        raise KeyboardInterrupt
    outs = []
    run_repl(Calculator(), input_fn, outs.append)
    assert outs[-1] == "Bye!"
