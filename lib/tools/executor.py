"""Executors."""
import subprocess
from pathlib import Path


class ExecutorInterface:

    def __init__(self):
        pass

    def run(self, source_path, inputs):
        """複数ののサンプルのinputに対して実行し、結果を文字列のリストとして出力する.

        :param source_path:
        :param input: str
        """
        outputs = []
        for data in inputs:
            outputs.append(self.execute(source_path, data))
        return outputs

    def execute(self, source_path, input_path):
        """一つのサンプルに対して実行し、結果を文字列として出力する.各言語でオーバーライドする.

        :param source_path:
        :param input_str: str
        """
        raise NotImplementedError


class PythonExecutor(ExecutorInterface):
    def execute(self, source_path, data):
        cmd = f"python {source_path}"
        p = subprocess.Popen(
            cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output = p.communicate(data.encode())[0]
        return output.decode()


class CppExecutor(ExecutorInterface):

    def run(self, source_path, inputs):
        """複数のサンプルのinputに対して実行し、結果を文字列のリストとして出力する.

        :param source_path:
        :param input: str
        """
        # compile
        temp_exe_path = Path("exe.out")
        compile_cmd = f"g++ {source_path} --std=c++14 -o {temp_exe_path}"
        subprocess.call(compile_cmd.split())
        outputs = []
        # execute
        for data in inputs:
            outputs.append(self.execute(source_path, data))
        # remove execution file
        temp_exe_path.unlink()
        return outputs

    def execute(self, temp_exe_path, data):
        execute_cmd = f"g++ {temp_exe_path}"
        p = subprocess.Popen(execute_cmd.split(),
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output = p.communicate(data.encode())[0]
        return output.decode()
