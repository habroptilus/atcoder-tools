"""Code generators."""


class CodeGeneratorInterface:
    def __init__(self):
        return

    def run(self, src_dir, level, rnd, include_input_file=True):
        target_dir = src_dir / f"{level}/{rnd:03d}"
        if not target_dir.exists():
            target_dir.mkdir(parents=True)
        problems = self.get_problems(level, rnd)
        for prob in problems:
            self.gen_script(target_dir, prob)
        if include_input_file:
            input_filepath = target_dir / "input.txt"
            input_filepath.touch()
        return

    def gen_script(self, target_dir, prob):
        raise NotImplementedError

    def get_problems(self, level, rnd):
        temp = {"abc": list("abcd"), "agc": list("abcdef")}
        if level in temp.keys():
            return temp[level]
        elif level == "arc":
            if rnd >= 57:
                return "cdef".split()
            else:
                return "abcd".split()
        else:
            raise Exception("Invalid level.")


class PythonCodeGenerator(CodeGeneratorInterface):

    def gen_script(self, target_dir, prob):
        target_path = target_dir / f"code_{prob}.py"
        if not target_path.exists():
            target_path.touch()


class CppCodeGenerator(CodeGeneratorInterface):
    template = "#include <bits/stdc++.h>\ntypedef long long ll;"

    def gen_script(self, target_dir, prob):
        target_path = target_dir / f"code_{prob}.cpp"
        if not target_path.exists():
            target_path.write_text(self.template)
