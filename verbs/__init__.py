"""Python boilerplate,
in this file I setup PYTHONPATH so modules can be found more easily.
"""

import os
import sys

# csfp - "current_script_folder_path"
csfp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if csfp not in sys.path:
    sys.path.insert(0, csfp)
