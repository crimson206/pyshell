from pyshell import shell, ShellError

# Example 1: File system operations
print("=== File System Operations ===")
try:
    # Create a test directory
    shell("mkdir -p test_data")
    print("✓ Created test directory")
    
    # Create a sample file
    shell("echo 'Hello, World!' > test_data/sample.txt")
    print("✓ Created sample file")
    
    # Count lines in the file
    line_count = shell("wc -l < test_data/sample.txt")
    print(f"✓ File has {line_count} lines")
    
    # Get file size
    file_size = shell("stat -c%s test_data/sample.txt")
    print(f"✓ File size: {file_size} bytes")
    
except ShellError as e:
    print(f"❌ File operation failed: {e}")

# Example 2: System information
print("\n=== System Information ===")
try:
    # Get current user
    user = shell("whoami")
    print(f"✓ Current user: {user}")
    
    # Get current directory
    pwd = shell("pwd")
    print(f"✓ Current directory: {pwd}")
    
    # Get system uptime
    uptime = shell("uptime -p")
    print(f"✓ System uptime: {uptime}")
    
except ShellError as e:
    print(f"❌ System info failed: {e}")

# Example 3: Data processing pipeline
print("\n=== Data Processing Pipeline ===")
try:
    # Create a data file with numbers
    shell("seq 1 10 > test_data/numbers.txt")
    print("✓ Created numbers file")
    
    # Filter even numbers
    even_numbers = shell("cat test_data/numbers.txt | grep '[02468]$'")
    print(f"✓ Even numbers: {even_numbers}")
    
    # Calculate sum of even numbers
    even_sum = shell("cat test_data/numbers.txt | grep '[02468]$' | paste -sd+ | bc")
    print(f"✓ Sum of even numbers: {even_sum}")
    
    # Clean up
    shell("rm -rf test_data")
    print("✓ Cleaned up test files")
    
except ShellError as e:
    print(f"❌ Data processing failed: {e}")
    print(f"Error details: {e.stderr}")

print("\n=== All examples completed! ===")