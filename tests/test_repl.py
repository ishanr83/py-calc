from calculator.operations import Calculator
from calculator.repl import run_repl

def make_io(lines):
    # lines: list of inputs to feed; returns (input_fn, outputs_list)
    it = iter(lines)
    outputs = []
    def input_fn(prompt):
        try:
            return next(it)
        except StopIteration:
            # Simulate Ctrl+D
            raise EOFError
    def output_fn(s):
        outputs.append(s)
    return input_fn, output_fn, outputs

def test_repl_happy_path_add_mul():
    input_fn, output_fn, out = make_io(["add 2 3", "mul 3 4", "exit"])
    run_repl(Calculator(), input_fn, output_fn)
    assert "Calculator REPL." in out[0]
    assert "5.0" in out  # result of add
    assert "12.0" in out # result of mul
    assert "Bye!" == out[-1]

def test_repl_input_validation_and_unknown():
    input_fn, output_fn, out = make_io(["", "foo", "add two 2", "div 5 0", "q"])
    run_repl(Calculator(), input_fn, output_fn)
    # unknown command:
    assert any("Unknown command" in x for x in out)
    # non-numeric:
    assert any("Error:" in x and "numeric" in x for x in out)
    # div by zero:
    assert any("Error:" in x and "Division by zero" in x for x in out)
    assert "Bye!" == out[-1]
