from pathlib import Path
from sys import path


cwd = Path.cwd()

# >>> cwd
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/521/scripts')

script_dir = Path(path[0])

# >>> script_dir
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/521/scripts/base')

# file_path = Path(r'd:\G-Doc\TOP Academy\Data Science\521\scripts\base\literals.py')
file_path = script_dir / 'literals.py'

# >>> file_path
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/521/scripts/base/literals.py')


# >>> script_dir.parent
# WindowsPath('D:/G-Doc/TOP Academy/Data Science/521/scripts')
# >>>
# >>> script_dir.parent == cwd
# True


# >>> script_dir.exists()
# True
# >>>
# >>> script_dir.is_dir()
# True
# >>>
# >>> script_dir.is_file()
# False
# >>>
# >>> file_path.exists()
# True
# >>>
# >>> file_path.is_dir()
# False
# >>>
# >>> file_path.is_file()
# True
# >>>
# >>> (script_dir / 'out.txt').exists()
# False
# >>>
# >>> (script_dir / 'out.txt').is_dir()
# False
# >>>
# >>> (script_dir / 'out.txt').is_file()
# False

