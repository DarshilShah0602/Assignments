s = "hello"

try:
    s[0] = 'H'
except TypeError:
    print("Strings are immutable in Python")
