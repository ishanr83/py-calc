import sys
import subprocess
import os

def test_module_entrypoint_quits_cleanly():
    # Run "python -m calculator" and feed 'q\n' to exit the REPL immediately.
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"  # ensure module is found on Windows/CI
    proc = subprocess.run(
        [sys.executable, "-m", "calculator"],
        input="q\n",
        text=True,
        capture_output=True,
        env=env,
    )
    assert proc.returncode == 0
    assert "Calculator REPL" in proc.stdout
    assert "Bye!" in proc.stdout
