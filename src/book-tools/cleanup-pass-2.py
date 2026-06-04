import re
from pathlib import Path

in_path = Path("ch01-introduction.md")
out_path = Path("ch01-introduction-polished.md")

text = in_path.read_text(encoding="utf-8")

# --- Polishing Pass ---

def remove_page_numbers(text: str) -> str:
    # Remove isolated numbers between paragraphs (likely page numbers)
    text = re.sub(r"\n\s*\d{1,3}\s*\n", "\n", text)
    return text

def fix_spaced_words(text: str) -> str:
    # Fix residual letter-spacing like "t h i s", "r e v i v a l"
    def join_spaced_letters(m):
        return m.group(0).replace(" ", "")
    text = re.sub(r"(?:\b[A-Za-z]\b\s*){2,}[A-Za-z]\b", join_spaced_letters, text)
    return text

def fix_quotes_and_apostrophes(text: str) -> str:
    text = text.replace("“", '"').replace("”", '"').replace("’", "'")
    return text

def add_blockquotes(text: str) -> str:
    # Convert lines starting with quotes to Markdown blockquotes
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.match(r'^\s*".+?"', line):
            lines[i] = "> " + line.strip()
    return "\n".join(lines)

def fix_headings(text: str) -> str:
    # Ensure consistent heading spacing
    text = re.sub(r"^#([A-Za-z])", r"# \1", text, flags=re.MULTILINE)
    text = re.sub(r"^##([A-Za-z])", r"## \1", text, flags=re.MULTILINE)
    # Ensure one blank line before and after headings
    text = re.sub(r"([^\n])\n(#)", r"\1\n\n\2", text)
    text = re.sub(r"(# .+)\n([^#\n])", r"\1\n\n\2", text)
    return text

def normalize_paragraphs(text: str) -> str:
    # Collapse multiple blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Ensure sentences don't merge
    text = re.sub(r"([a-z])([A-Z])", r"\1. \2", text)
    return text

def final_trim(text: str) -> str:
    text = text.strip() + "\n"
    return text

# Sequentially apply polishing transformations
text = remove_page_numbers(text)
text = fix_spaced_words(text)
text = fix_quotes_and_apostrophes(text)
text = add_blockquotes(text)
text = fix_headings(text)
text = normalize_paragraphs(text)
text = final_trim(text)

out_path.write_text(text, encoding="utf-8")
print(f"Polished Markdown saved to: {out_path}")
