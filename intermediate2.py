usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_input=input("Username: ")
match=False
for name in usernames:
    if name==user_input:
        match=True
        break
    else:
        match=False
if match==True:
    print("Access granted")
else:
    print("Access denied")