import subprocess
import sys


def test_cli_with_flag():
    result = subprocess.run(
        [sys.executable, "-m", "prime_calculator", "-n", "50"],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "30" in result.stdout


def test_cli_without_flag():
    result = subprocess.run(
        [sys.executable, "-m", "prime_calculator"],
        input="50\n",
        capture_output=True,
        text=True,
        check=True,
    )

    assert "30" in result.stdout
