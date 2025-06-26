import subprocess

class ShellError(Exception):
    def __init__(self, message, returncode, stderr, stdout=""):
        super().__init__(message)
        self.returncode = returncode
        self.stderr = stderr
        self.stdout = stdout

def shell(script: str, env: dict = None, **kwargs) -> str:
    """Execute shell script as a Python function.
    
    Args:
        script: Shell script to execute
        env: Additional environment variables to merge with existing ones
        **kwargs: Additional arguments passed to subprocess.run
        
    Returns:
        str: Command output (stdout)
        
    Raises:
        ShellError: When command fails with non-zero exit code
    """
    # Merge environment variables if provided
    if env is not None:
        import os
        merged_env = os.environ.copy()
        merged_env.update(env)
        kwargs['env'] = merged_env
    
    result = subprocess.run(
        f"set -e\n{script}",
        shell=True,
        capture_output=True,
        text=True,
        **kwargs
    )
    
    if result.returncode != 0:
        # Create a more informative error message
        script_preview = script[:100] + "..." if len(script) > 100 else script
        stderr_preview = result.stderr.strip()[:200] + "..." if len(result.stderr) > 200 else result.stderr.strip()
        
        error_msg = f"Shell command failed (exit code {result.returncode}): {script_preview}"
        if stderr_preview:
            error_msg += f"\nError: {stderr_preview}"
            
        raise ShellError(
            error_msg,
            result.returncode,
            result.stderr,
            result.stdout
        )
    
    return result.stdout.strip()

