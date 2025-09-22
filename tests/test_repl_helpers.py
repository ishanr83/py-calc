from calculator import repl
from calculator.operations import Calculator

def test_banner_bye_and_prompt_are_used_and_correct():
    # Directly cover helpers + constant
    assert repl.banner().startswith("Calculator REPL.")
    assert repl.bye() == "Bye!"
    assert repl.PROMPT == "> "

    # Also cover normal quit path quickly (banner -> q -> bye)
    outs = []
    def input_fn(_):
        return "q"
    repl.run_repl(Calculator(), input_fn, outs.append)
    assert outs[0].startswith("Calculator REPL.")
    assert outs[-1] == "Bye!"
