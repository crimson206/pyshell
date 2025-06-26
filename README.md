# PyShell

Execute shell scripts as Python functions with proper error handling.

## Installation

```bash
pip install pyshell
```

## Quick Start

```python
from pysh.core import shell_func, ShellError

# Execute a simple command
result = shell_func("echo 'Hello, World!'")
print(result)  # Hello, World!

# Handle errors gracefully
try:
    shell_func("cat nonexistent_file.txt")
except ShellError as e:
    print(f"Error: {e}")
    print(f"Return code: {e.returncode}")
    print(f"Stderr: {e.stderr}")
```

## Features

- **Simple API**: Execute shell commands as Python functions
- **Error Handling**: Automatic exception raising for non-zero exit codes
- **Type Safety**: Full type hints for better IDE support
- **Cross-platform**: Works on Unix-like systems (Linux, macOS)

## Examples

See the `examples/` directory for comprehensive examples:

- `success.py` - Working examples
- `fail.py` - Error handling examples

## API Reference

### `shell_func(script: str, **kwargs) -> str`

Execute a shell script and return the output.

**Parameters:**
- `script`: Shell script to execute
- `**kwargs`: Additional arguments passed to `subprocess.run`

**Returns:**
- `str`: Command output (stdout)

**Raises:**
- `ShellError`: When command fails with non-zero exit code

### `ShellError`

Exception raised when shell commands fail.

**Attributes:**
- `returncode`: Exit code of the failed command
- `stderr`: Standard error output
- `stdout`: Standard output

## License

MIT License 