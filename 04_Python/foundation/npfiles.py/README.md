# 🔢 NumPy Fundamentals & Numerical Operations

This directory contains practice exercises and Jupyter notebooks focused on numerical computing using **NumPy** (`numpy`), the foundational library for scientific and vector computing in Python.

---

## 📄 File Inventory

* **`files.ipynb`**:
  * Interactive Jupyter notebook demonstrating:
    * Vectorized operations comparing Python list comprehensions against NumPy array math.
    * Initializing 1D and multidimensional NumPy arrays (`np.array`).
    * Scalar arithmetic on arrays without manual loops.
    * Boolean filtering and logical masking (e.g., `mark > 45`).
    * Array transformations, scaling, and statistical aggregations.

---

## 💡 Key Benefits of NumPy

* **Performance**: NumPy arrays (`ndarray`) are contiguous memory blocks implemented in C, enabling high execution speeds compared to standard Python lists.
* **Vectorization**: Clean, expressive syntax performing element-wise arithmetic without explicit `for` loops.
* **Broadcasting**: Arithmetic operations across arrays of different compatible shapes.

---

## 🏃 How to Run

```bash
pip install numpy jupyter
jupyter notebook files.ipynb
```
