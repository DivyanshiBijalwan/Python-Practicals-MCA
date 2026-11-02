from pathlib import Path
text = input("Enter text: ")
Path("sample.txt").write_text(text, encoding="utf-8")
print("Text written successfully.")
