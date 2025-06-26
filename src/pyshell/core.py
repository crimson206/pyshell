import subprocess

class ShellError(Exception):
    def __init__(self, message, returncode, stderr, stdout=""):
        super().__init__(message)
        self.returncode = returncode
        self.stderr = stderr
        self.stdout = stdout

def shell(script: str, **kwargs) -> str:
    """Execute shell script as a Python function.
    
    Args:
        script: Shell script to execute
        **kwargs: Additional arguments passed to subprocess.run
        
    Returns:
        str: Command output (stdout)
        
    Raises:
        ShellError: When command fails with non-zero exit code
    """
    result = subprocess.run(
        f"set -e\n{script}",
        shell=True,
        capture_output=True,
        text=True,
        **kwargs
    )
    
    if result.returncode != 0:
        raise ShellError(
            f"Shell command failed: {script[:50]}...",
            result.returncode,
            result.stderr,
            result.stdout
        )
    
    return result.stdout.strip()

