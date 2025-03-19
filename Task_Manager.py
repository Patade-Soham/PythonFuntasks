# Develop a Python program to manage a task list using lists and tuples,
# including adding, removing, updating, and sorting tasks
task=[]
cond= True
def adding():
    user_tasks=input('Enter the task to add : ').upper()
    task.append(user_tasks)
    print('Task added to the list')
def removing():
    user_tasks=input('Enter the task to remove : ').upper()
    task.remove(user_tasks)
    print('Task successfully removed from the list')
def updating():
    user_tasks=input('Enter the task to add : ').upper()
    position=int(input('Enter the number of position to edit : '))
    task[position-1]=user_tasks
    if position>len(task):
        print('Position does not exist...')
def sorting():
    task.sort()
def display():
    if len(task)==0:
        print('List is empty')
    else:    
        print(task)
def opperation():    
    while  cond==True:
       
        print('1. Add Task')
        print('2. Remove Task')
        print('3. Update Task')
        print('4. Sort Task')
        print('5. Display Task List')
        print('6. Exit...')
        choice=int(input('Enter your choice for the opertation : '))
        
        if choice==1:
            adding()
            display()
        elif choice==2:
            display()
            removing()
            display()
        elif choice==3:
            display()
            updating()
            display()
        elif choice==4:
            display()
            sorting()
            display()
        elif choice==5:
            display()
        elif choice==6:
            print('Thank you')
            break
        else:
            print('Invalid Choice!')
print('\n\n>>>>Welcome to Task Manager<<<<\n\n')       
opperation()
        
        
        
    
    
    
