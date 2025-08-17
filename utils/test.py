from logging import exception
# 用来验证一些语法的地方

def test():
    try:
        a = 1
    except exception(Exception):
        a = None
        print("error")

    try:
        print("a", a)
    except exception(Exception):
        print("error")

if __name__ == "__main__":
    test()
    print("Hello World")