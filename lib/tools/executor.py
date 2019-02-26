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
        input_path = Path("input_temp.txt")
        for input_str in inputs:
            input_path.write_text(input_str)
            outputs.append(self.execute(source_path, input_path))
        input_path.unlink()
        return outputs

    def execute(self, source_path, input_path):
        """一つのサンプルに対して実行し、結果を文字列として出力する.各言語でオーバーライドする.

        :param source_path:
        :param input_str: str
        """
        raise NotImplementedError


class PythonExecutor(ExecutorInterface):
    def execute(self, source_path, input_path):
        output_path = Path("output_temp.txt")
        cmd = f"python {source_path} < {input_path} > {output_path}"
        subprocess.call(cmd.split())
        output = output_path.read_text()
        output_path.unlink()
        return output
