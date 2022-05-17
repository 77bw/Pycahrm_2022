import test_mod


if hasattr(test_mod,"sayhi"):
    f = getattr(test_mod,"sayhi")
    f()


    setattr(test_mod,"name",22)
    print(test_mod.name)