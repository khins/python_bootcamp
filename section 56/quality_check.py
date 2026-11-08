"""Run focused syntax and API tests; does not install dependencies or deploy."""
from pathlib import Path
import ast
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    folder = ROOT / "section 55"
    for path in folder.glob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", str(folder),
                    "-p", "test_*.py", "-v"], cwd=ROOT, check=True)
    print("Syntax and API checks passed")

if __name__ == "__main__":
    main()
