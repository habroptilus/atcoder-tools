from pathlib import Path
dir_path = Path("python/ABC")


for p in dir_path.glob("*/abc*.py"):
    rnd = str(p.parent)[-3:]
    prob = str(p)[-4].lower()
    to_path = Path(f"src/abc/{rnd}/python/code_{prob}.py")
    to_path.parent.mkdir(exist_ok=True, parents=True)
    data = p.read_text()
    to_path.write_text(data)
