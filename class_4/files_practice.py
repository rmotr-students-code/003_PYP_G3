
with MyOpen('test.txt') as f:
    print f.read()

try:
    f = open('test.txt', 'r')
    print(f.read())
except Exception as e:
    print("SOmething went wrong")
finally:
    print("Closing file")
    f.close()


with open('test.txt') as f:
    print f.read()