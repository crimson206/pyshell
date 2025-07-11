# PyShell

Execute shell scripts as Python functions with proper error handling.

> **Note**: This is different from the existing `pyshell` package on PyPI. This library focuses on simplicity and explicit error handling.

## Installation

```bash
pip install git+https://github.com/crimson206/pyshell.git
```

## Quick Start

```python
from pyshell import shell, ShellError

# Execute a simple command
result = shell("echo 'Hello, World!'")
print(result)  # Hello, World!

# Handle errors gracefully
try:
    shell("cat nonexistent_file.txt")
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

### `shell(script: str, env: dict = None, **kwargs) -> str`

Execute a shell script and return the output.

**Parameters:**
- `script`: Shell script to execute
- `env`: Additional environment variables to merge with existing ones
- `**kwargs`: Additional arguments passed to `subprocess.run`

**Returns:**
- `str`: Command output (stdout)

**Raises:**
- `ShellError`: When command fails with non-zero exit code

### `ShellError`

Exception raised when shell commands fail. This exception is automatically raised by the `shell()` function and should only be used for catching errors, not for creating them manually.

**Attributes:**
- `returncode`: Exit code of the failed command
- `stderr`: Standard error output
- `stdout`: Standard output

**Note:** This exception is designed for internal use by the `shell()` function. Users should only catch this exception, not instantiate it directly.

## License

MIT License 