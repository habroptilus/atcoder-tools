"""Code generators."""


class CodeGeneratorInterface:
    def __init__(self):
        return

    def run(self, src_dir, level, rnd, include_input_file=True):
        target_dir = src_dir / f"{level}/{rnd:03d}"
        problems = self.get_problems(level, rnd)
        for prob in problems:
            self.gen_script(target_dir, prob)
        if include_input_file:
            input_filepath = target_dir / "samples/input.txt"
            input_filepath.parent.mkdir(parents=True, exist_ok=True)
            input_filepath.touch()
        return

    def gen_script(self, target_dir, prob):
        raise NotImplementedError

    def get_problems(self, level, rnd):
        temp = {"abc": list("abcd"), "arc": list(
            "abcd"), "agc": list("abcdef")}
        if level in temp.keys():
            return temp[level]
        else:
            raise Exception("Invalid level.")


class PythonCodeGenerator(CodeGeneratorInterface):

    def gen_script(self, target_dir, prob):
        target_path = target_dir / f"python/code_{prob}.py"
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.touch(exist_ok=False)


class CppCodeGenerator(CodeGeneratorInterface):
    template = "#include <bits/stdc++.h>\ntypedef long long ll;"

    def gen_script(self, target_dir, prob):
        target_path = target_dir / f"cpp/code_{prob}.cpp"
        target_path.parent.mkdir(parents=True, exist_ok=True)
        if not target_path.exists():
            target_path.write_text(self.template)
        else:
            raise Exception(f"{target_path} already exists.")
