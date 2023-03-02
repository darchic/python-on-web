#todos=open('todos.txt','a')
#print("Первая строка",file=todos)
#print("Вторая строка",file=todos)
#todos.close()

tasks = open('todos.txt')
for str in tasks:
    print(str, end='')
tasks.close()

with open("todos.txt") as tasks:
    for srt in tasks:
        print(str, end=" ")
print("Тут файл уже закрыт")

