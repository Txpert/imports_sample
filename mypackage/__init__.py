import importlib
from .module2 import func1
from .module1 import func2

__all__ = ['funktion_a', 'funktion_b']

# module_names = ['module1', 'module2']
# for module_name in module_names:
#     module = importlib.import_module(f'.{module_name}', package='mypackage')
#     globals().update({attr: getattr(module, attr) for attr in dir(module) if not attr.startswith('_')})

# Alternativ, wenn nur bestimmte Funktionen importiert werden sollen
# globals().update({name: module.funktion_a for module in modules if hasattr(module, 'funktion_a')})
