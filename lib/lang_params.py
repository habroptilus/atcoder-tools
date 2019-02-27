from .tools import PythonExecutor, PythonCodeGenerator, CppCodeGenerator, CppExecutor

params = {
    "python": {
        "id": 3023,
        "extension": "py",
        "executor": PythonExecutor(),
        "generator": PythonCodeGenerator()
    },
    "cpp": {
        "id": 3003,
        "extension": "cpp",
        "executor": CppExecutor(),
        "generator": CppCodeGenerator()
    },
}
