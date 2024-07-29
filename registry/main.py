from registry.arithmetic import ARITHMETIC

if __name__ == "__main__":
    print(ARITHMETIC)
    print(repr(ARITHMETIC))

    add_obj = ARITHMETIC.get("Add")()
    print(add_obj(1, 2))

    sub_obj = ARITHMETIC.get("Subtract")()
    print(sub_obj(1, 2))

