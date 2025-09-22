from calculator.operations import Calculator, CalculatorError
from calculator.repl import run_repl

def _io_from(seq):
    it = iter(seq)
    outs = []
    def input_fn(_):
        return next(it)
    def output_fn(s):
        outs.append(s)
    return input_fn, output_fn, outs

def test_usage_error_when_arg_count_wrong():
    # Triggers the "Usage: <op> <num1> <num2>" ValueError in _parse_two_numbers
    input_fn, output_fn, outs = _io_from(["add 1", "q"])
    run_repl(Calculator(), input_fn, output_fn)
    assert any("Usage:" in s and "<op> <num1> <num2>" in s for s in outs)
    assert outs[-1] == "Bye!"

def test_calculatorerror_path_is_covered():
    # Hit the generic CalculatorError branch (not just ValueError)
    class BoomCalc(Calculator):
        def add(self, a, b):  # override to raise CalculatorError
            raise CalculatorError("boom")
    input_fn, output_fn, outs = _io_from(["add 1 2", "q"])
    run_repl(BoomCalc(), input_fn, output_fn)
    assert any("Error: boom" in s for s in outs)
    assert outs[-1] == "Bye!"
