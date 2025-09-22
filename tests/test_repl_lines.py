from calculator import repl
from calculator.operations import Calculator

def test_cover_prompt_and_quit_line():
    # Cover PROMPT line explicitly
    assert repl.PROMPT == "> "

    # Cover the normal quit path ("q") so the final "Bye!" is printed
    outs = []
    def input_fn(_):
        return "q"
    repl.run_repl(Calculator(), input_fn, outs.append)

    # Banner then "Bye!" — we only assert the last to be robust
    assert outs[-1] == "Bye!"
