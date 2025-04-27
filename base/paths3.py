from pathlib import Path


cwd = Path.cwd()

for p in cwd.iterdir():
    print(p)
print()

# D:\G-Doc\TOP Academy\Data Science\521\scripts\.git
# D:\G-Doc\TOP Academy\Data Science\521\scripts\.gitignore
# D:\G-Doc\TOP Academy\Data Science\521\scripts\base
# D:\G-Doc\TOP Academy\Data Science\521\scripts\funcs
# D:\G-Doc\TOP Academy\Data Science\521\scripts\git1.txt
# D:\G-Doc\TOP Academy\Data Science\521\scripts\git2.txt
# D:\G-Doc\TOP Academy\Data Science\521\scripts\git3.txt
# D:\G-Doc\TOP Academy\Data Science\521\scripts\git4.txt
# D:\G-Doc\TOP Academy\Data Science\521\scripts\libs
# D:\G-Doc\TOP Academy\Data Science\521\scripts\namespaces

for p in cwd.glob('*.txt'):
    print(p)
print()

# D:\G-Doc\TOP Academy\Data Science\521\scripts\git1.txt
# D:\G-Doc\TOP Academy\Data Science\521\scripts\git2.txt
# D:\G-Doc\TOP Academy\Data Science\521\scripts\git3.txt
# D:\G-Doc\TOP Academy\Data Science\521\scripts\git4.txt


