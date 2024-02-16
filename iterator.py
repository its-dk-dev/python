list = [1, 2, 3, 4]
i = iter(list)

print(i)
print(i.__next__)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())

fd = open("demo.txt", "r")
print(fd is iter(fd))

print(fd.__next__(), end=" ") 
print(fd.__next__(), end=" ")
print(fd.__next__(), end=" ")
print(fd.__next__(), end=" ")

while True:
    try:
        has_next = fd.__next__()
        if has_next:
            print(has_next)
    except:
        break

fd.close()