

import importlib

test_mod = importlib.import_module("test_mod",".")
#test_mod = __import__("test_mod")

test_mod.sayhi()