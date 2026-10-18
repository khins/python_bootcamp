from pathlib import Path


OUTPUT_PATH = Path(__file__).resolve().parent / "writing_demo.txt"
year = 1981
with open(OUTPUT_PATH, "a", encoding="utf-8") as file_object:
    file_object.write(str(year)) 