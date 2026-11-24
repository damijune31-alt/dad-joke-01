import os
import sys
from pathlib import Path

# One dad joke: the plants were too needy, so the parting is literal.
JOKE = "I told my plants to stop being so needy, and now we're really growing apart."

if not 1 <= len(JOKE) <= 200:
    sys.exit(f"joke must be 1-200 characters, got {len(JOKE)}")
if "\n" in JOKE:
    sys.exit("joke must be a single line")
print(f"wrote {len(JOKE)} characters to entry.txt")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(JOKE, encoding="utf-8")

if entry_path.read_text(encoding="utf-8") != JOKE:
    sys.exit("entry.txt does not match the joke")
