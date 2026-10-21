# 🛡️ Python Exception Handling

This directory demonstrates error handling techniques in Python to write resilient, fault-tolerant code and prevent program crashes.

---

## 📄 File Inventory

* **`exception handling`**:
  * Practical demonstrations of handling common runtime errors:
    * `ValueError`: Handling invalid user input conversions (e.g., non-integer strings passed to `int()`).
    * `FileNotFoundError`: Gracefully catching missing file references.
    * `PermissionError` & `FileExistsError`: Handling file system permission errors and existing file conflicts.
    * `try-except-else`: Executing success blocks when no exceptions are thrown.
    * `raise`: Triggering explicit exceptions defensively (e.g., rejecting negative age values).
* **`fina;.py`**:
  * Demonstration of the `finally` block ensuring execution of cleanup routines regardless of whether an exception was raised or handled.

---

## 💡 Code Patterns Illustrated

```python
# Validating user input safely
try:
    age = int(input("Enter Age: "))
except ValueError:
    print("Please enter a valid integer")
else:
    print(f"Valid Age: {age}")
```

```python
# Guaranteeing resource cleanup
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed.")
```
