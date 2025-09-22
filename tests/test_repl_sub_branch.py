from calculator.operations import Calculator
from calculator.repl import run_repl

def test_repl_sub_branch():
    # Drive the REPL to execute the "sub" branch, then quit.
    inputs = iter(["sub 5 3", "q"])
    outs = []
    def input_fn(_):
        return next(inputs)
    run_repl(Calculator(), input_fn, outs.append)

    assert "2.0" in outs
    assert outs[-1] == "Bye!"
