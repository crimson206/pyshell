from pyshell.core import shell_func, ShellError

# Example 1: File system operations
print("=== File System Operations ===")
try:
    # Create a test directory
    shell_func("mkdir -p test_data")
    print("✓ Created test directory")
    
    # Create a sample file
    shell_func("echo 'Hello, World!' > test_data/sample.txt")
    print("✓ Created sample file")
    
    # Count lines in the file
    line_count = shell_func("wc -l < test_data/sample.txt")
    print(f"✓ File has {line_count} lines")
    
    # Get file size
    file_size = shell_func("stat -c%s test_data/sample.txt")
    print(f"✓ File size: {file_size} bytes")
    
except ShellError as e:
    print(f"❌ File operation failed: {e}")

# Example 2: System information
print("\n=== System Information ===")
try:
    # Get current user
    user = shell_func("whoami")
    print(f"✓ Current user: {user}")
    
    # Get current directory
    pwd = shell_func("pwd")
    print(f"✓ Current directory: {pwd}")
    
    # Get system uptime
    uptime = shell_func("uptime -p")
    print(f"✓ System uptime: {uptime}")
    
except ShellError as e:
    print(f"❌ System info failed: {e}")

# Example 3: Data processing pipeline
print("\n=== Data Processing Pipeline ===")
try:
    # Create a data file with numbers
    shell_func("seq 1 10 > test_data/numbers.txt")
    print("✓ Created numbers file")
    
    # Filter even numbers
    even_numbers = shell_func("cat test_data/numbers.txt | grep '[02468]$'")
    print(f"✓ Even numbers: {even_numbers}")
    
    # Calculate sum of even numbers
    even_sum = shell_func("cat test_data/numbers.txt | grep '[02468]$' | paste -sd+ | bc")
    print(f"✓ Sum of even numbers: {even_sum}")
    
    # Clean up
    shell_func("rm -rf test_data")
    print("✓ Cleaned up test files")
    
except ShellError as e:
    print(f"❌ Data processing failed: {e}")
    print(f"Error details: {e.stderr}")

print("\n=== All examples completed! ===")