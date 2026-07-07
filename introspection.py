#Option 2: Use Python introspection

#If you can import the module, run:

import inspect
from persistence import save_read

print(inspect.getsource(save_read))