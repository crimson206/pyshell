from pysh.core import shell_func, ShellError

# Example 4: Error handling demonstrations
print("\n=== Error Handling Examples ===")

# Example 4a: Command not found
print("4a. Command not found:")
try:
    shell_func("nonexistent_command")
except ShellError as e:
    print(f"❌ Expected error: {e}")
    print(f"   Return code: {e.returncode}")
    print(f"   Stderr: {e.stderr[:100]}...")

# Example 4b: File not found
print("\n4b. File not found:")
try:
    shell_func("cat nonexistent_file.txt")
except ShellError as e:
    print(f"❌ Expected error: {e}")
    print(f"   Return code: {e.returncode}")

# Example 4c: Permission denied
print("\n4c. Permission denied:")
try:
    shell_func("touch /root/test_file")
except ShellError as e:
    print(f"❌ Expected error: {e}")
    print(f"   Return code: {e.returncode}")

# Example 4d: Invalid syntax
print("\n4d. Invalid syntax:")
try:
    shell_func("echo 'unclosed quote")
except ShellError as e:
    print(f"❌ Expected error: {e}")
    print(f"   Return code: {e.returncode}")

print("\n=== All examples completed! ===")