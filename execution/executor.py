import subprocess
import tempfile
import os

def run_code(code, language="python"):
    try:
        if language == "python":
            with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
                f.write(code.encode())
                file_path = f.name

            result = subprocess.run(
                ["python", file_path],
                capture_output=True,
                text=True,
                timeout=5
            )

        elif language == "java":
            file_path = "Main.java"

            with open(file_path, "w") as f:
                f.write(code)

            compile_result = subprocess.run(
                ["javac", file_path],
                capture_output=True,
                text=True
            )

            if compile_result.returncode != 0:
                return False, compile_result.stderr

            result = subprocess.run(
                ["java", "Main"],
                capture_output=True,
                text=True,
                timeout=5
            )

        else:
            return False, "Unsupported language"

        if result.returncode == 0:
            return True, result.stdout

        return False, result.stderr

    except Exception as e:
        return False, str(e)
