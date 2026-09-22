import subprocess
import sys


def test_terminale_con_flag():
    result = subprocess.run(
        [sys.executable, "-m", "calcola_primi", "-n", "50"],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "30" in result.stdout


def test_terminale_senza_flag():
    result = subprocess.run(
        [sys.executable, "-m", "calcola_primi"],
        input="50\n",
        capture_output=True,
        text=True,
        check=True,
    )

    assert "30" in result.stdout
