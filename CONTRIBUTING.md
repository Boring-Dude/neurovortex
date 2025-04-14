# Contributing to NeuroVortex

Thank you for considering contributing to **NeuroVortex**! We welcome contributions of all kinds, including bug fixes, feature requests, documentation improvements, and more. This document outlines the guidelines for contributing to the project.

---

## Table of Contents
1. Code of Conduct
2. How to Contribute
3. Setting Up the Development Environment
4. Submitting Changes
5. Style Guide
6. Testing
7. Reporting Issues
8. Feature Requests

---

## Code of Conduct
By participating in this project, you agree to abide by our [Code of Conduct](https://github.com/boring-dude/neurovortex/blob/main/CODE_OF_CONDUCT.md). Please treat everyone with respect and professionalism.

---

## How to Contribute
### 1. Fork the Repository
- Navigate to the [NeuroVortex repository](https://github.com/boring-dude/neurovortex).
- Click the **Fork** button to create your own copy of the repository.

### 2. Clone Your Fork
Clone your forked repository to your local machine:
```bash
git clone https://github.com/<your-username>/neurovortex.git
cd neurovortex
```

### 3. Create a Branch
Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

---

## Setting Up the Development Environment
1. **Install Python**: Ensure you have Python 3.8 or higher installed.
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Development Tools**:
   Install additional tools for linting and testing:
   ```bash
   pip install flake8 pytest pytest-cov
   ```

---

## Submitting Changes
### 1. Commit Your Changes
- Follow the Style Guide before committing.
- Write clear and concise commit messages:
  ```bash
  git commit -m "Add feature: GPU temperature monitoring"
  ```

### 2. Push Your Changes
Push your branch to your forked repository:
```bash
git push origin feature/your-feature-name
```

### 3. Open a Pull Request
- Go to the original repository: [NeuroVortex](https://github.com/boring-dude/neurovortex).
- Click **Pull Requests** > **New Pull Request**.
- Select your branch and submit the pull request.

---

## Style Guide
### Code Style
- Follow **PEP 8** for Python code.
- Use `flake8` to lint your code:
  ```bash
  flake8 neurovortex
  ```

### Docstrings
- Use **Google-style docstrings** for all functions and classes.
- Example:
  ```python
  def example_function(param1, param2):
      """
      Brief description of the function.

      Args:
          param1 (type): Description of param1.
          param2 (type): Description of param2.

      Returns:
          type: Description of the return value.
      """
  ```

---

## Testing
### Running Tests
- Write tests for any new features or bug fixes.
- Run tests using `pytest`:
  ```bash
  pytest
  ```

### Test Coverage
- Ensure your changes maintain or improve test coverage.
- Use `pytest-cov` to check coverage:
  ```bash
  pytest --cov=neurovortex --cov-report=term
  ```

---

## Reporting Issues
If you encounter a bug or have a question, please open an issue:
1. Go to the [Issues page](https://github.com/boring-dude/neurovortex/issues).
2. Click **New Issue**.
3. Provide a clear and detailed description of the issue.

### Include the Following:
- Steps to reproduce the issue.
- Expected behavior.
- Actual behavior.
- Environment details (e.g., OS, Python version).

---

## Feature Requests
We welcome feature requests! To suggest a new feature:
1. Open an issue on the [Issues page](https://github.com/boring-dude/neurovortex/issues).
2. Use the **Feature Request** template (if available).
3. Provide a detailed description of the feature and its use case.

---

## Thank You!
Thank you for contributing to NeuroVortex! Your contributions help make this project better 
