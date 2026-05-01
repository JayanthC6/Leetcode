# LeetCode Solutions

A collection of LeetCode solutions in Python and SQL.

## 📁 Repository Structure

```
Leetcode/
├── Python/          # Python solutions to LeetCode problems
└── SQL/             # SQL solutions to LeetCode problems
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** for running Python solutions
- **Git** for cloning the repository
- A code editor like **VS Code**, **PyCharm**, or any terminal-based editor

### Clone the Repository

#### Using HTTPS

```bash
git clone https://github.com/JayanthC6/Leetcode.git
cd Leetcode
```

#### Using SSH

```bash
git clone git@github.com:JayanthC6/Leetcode.git
cd Leetcode
```

## 💻 Using with VS Code

### Step 1: Install VS Code

Download and install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/)

### Step 2: Clone and Open the Repository

**Option A: Using VS Code Command Palette**
1. Open VS Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type "Git: Clone" and press Enter
4. Paste the repository URL: `https://github.com/JayanthC6/Leetcode.git`
5. Choose a folder to clone into

**Option B: Using Terminal**
```bash
# Clone the repository
git clone https://github.com/JayanthC6/Leetcode.git

# Open in VS Code
code Leetcode
```

### Step 3: Install Recommended Extensions

For the best experience, install these VS Code extensions:

1. **Python** (`ms-python.python`) - Python language support
2. **Pylance** (`ms-python.vscode-pylance`) - Python IntelliSense
3. **SQLTools** (`mtxr.sqltools`) - SQL editing and execution

### Step 4: Run Python Solutions

1. Open any Python file (e.g., `Python/Two_sum.py`)
2. Click the play button ▶️ in the top right, or
3. Right-click and select "Run Python File in Terminal"

## 🖥️ Using with Terminal

### Navigate to the Repository

```bash
cd Leetcode
```

### Run a Python Solution

```bash
python Python/Two_sum.py
```

Or interactively test solutions:

```bash
# Open Python interactive mode
python

# Import and test a solution
>>> from Python.Two_sum import Solution
>>> s = Solution()
>>> s.twoSum([2, 7, 11, 15], 9)
[0, 1]
```

## 🔧 Using with Other Editors

### PyCharm

1. Open PyCharm
2. File → Open → Select the cloned `Leetcode` folder
3. Navigate to any Python file and click the green play button

### Vim/Neovim

```bash
cd Leetcode
vim Python/Two_sum.py
```

### Sublime Text

```bash
cd Leetcode
subl .
```

## 🤖 Using with AI Coding Assistants

### GitHub Copilot (VS Code)

1. Install the GitHub Copilot extension in VS Code
2. Sign in with your GitHub account
3. Open any solution file - Copilot will provide suggestions as you type

### Other AI Tools

This repository works with any AI-powered code editor that supports:
- Python language server
- Git integration

## 📝 Adding Your Own Solutions

1. Create a new Python file in the `Python/` directory
2. Follow the existing naming convention (e.g., `Problem_name.py`)
3. Implement your solution as a class with the appropriate method:

```python
class Solution:
    def yourMethod(self, params):
        # Your solution here
        pass
```

## 🔄 Keeping Up to Date

```bash
# Pull the latest changes
git pull origin main
```

## 📜 License

This repository is for educational purposes and personal use.

---

Feel free to contribute by submitting a pull request!
