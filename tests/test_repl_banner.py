from calculator.operations import Calculator
from calculator.repl import run_repl

def test_banner_and_quit_path():
    # Feed just 'q' so we print the banner once, then quit gracefully.
    inputs = iter(["q"])
    outputs = []
    def input_fn(_):
        return next(inputs)
    def output_fn(s):
        outputs.append(s)

    run_repl(Calculator(), input_fn, output_fn)

    assert outputs[0].startswith("Calculator REPL.")
    assert outputs[-1] == "Bye!"
