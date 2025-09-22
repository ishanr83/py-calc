from calculator.operations import Calculator
from calculator import __main__ as m

def test_main_calls_run_repl_with_calculator(monkeypatch):
    called = {"ok": False, "arg": None}
    def fake_run_repl(arg):
        called["ok"] = True
        called["arg"] = arg
    monkeypatch.setattr(m, "run_repl", fake_run_repl)

    m.main()  # should invoke our fake

    assert called["ok"] is True
    assert isinstance(called["arg"], Calculator)
