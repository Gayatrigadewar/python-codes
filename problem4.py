my_list = []

n = int(input())

for _ in range(n):
    command = input().strip().split()
    cmd = command[0]

    if cmd == "insert":
        i = int (command[1])
        e = int (command[2])
        my_list.insert(i, e)
    elif cmd == "print":
        print(my_list)
    elif cmd == "remove":
        e = int(command[1])
        my_list.remove(e)
    elif cmd == "append":
        e = int(command[1])
        my_list.append(e)
    elif cmd == "sort":
        my_list.sort()
    elif cmd == "pop":
        mylist.pop()
    elif cmd == "reverse":
        my_list.reverse() 


