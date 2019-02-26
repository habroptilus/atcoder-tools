import subprocess
from pathlib import Path
from shutil import rmtree


class ExecutorInterface:
    temp_dir = Path("temp")

    def __init__(self):
        pass

    def run(self, source_path, inputs):
        """複数ののサンプルのinputに対して実行し、結果を文字列のリストとして出力する.

        :param source_path:
        :param input: str
        """
        outputs = []
        input_path = self.temp_dir / "input.txt"
        for input_str in inputs:
            input_path.write_text(input_str)
            outputs.append(self.execute(source_path, input_path))
        rmtree(self.temp_dir)
        return outputs

    def execute(self, source_path, input_path):
        """一つのサンプルに対して実行し、結果を文字列として出力する.各言語でオーバーライドする.

        :param source_path:
        :param input_str: str
        """
        raise NotImplementedError


class PythonExecutor(ExecutorInterface):
    def execute(self, source_path, input_path):
        output_path = self.temp_dir / "output.txt"
        cmd = f"python {source_path} < {input_path} > {output_path}"
        subprocess.call(cmd.split())
        output = output_path.read_text()
        return output


class CppExecutor(ExecutorInterface):
    def execute(self, source_path, input_path):
        output_path = self.temp_dir / "output.txt"
        temp_exe_path = self.temp_dir / "exe.out"
        compile_cmd = f"g++ {source_path} --std=c++14 -o {temp_exe_path}"
        execute_cmd = f"g++ {temp_exe_path} < {input_path} > {output_path}"
        subprocess.call(compile_cmd.split())
        subprocess.call(execute_cmd.split())
        output = output_path.read_text()
        return output
