#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    h4_attr = dir(hidden_4)
    for attr in h4_attr:
        if attr[0:2] != "__":
            print(attr)
