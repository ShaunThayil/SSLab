def checkUser(uname):
    if(uname in user):
        return True
    else:
        return False

def checkFile(uname,fname):
    if(fname in user[uname]):
        return True
    else:
        return False


def createUser():
    uname=input('Enter Username')
     
    if(checkUser(uname)):
        print('User Already Exists!!\n')
    
    else:
        user[uname]=[]
        print('User Created!!\n')



def createFile(currUser):
    fname=input('Enter File Name')
    
    if(checkFile(currUser,fname)):
        print(fname,' Already Exists in ',currUser,' Directory')
        
    
    else:
        user[currUser].append(fname)

def renameUser():
    uname=input('Enter User Name: ')
    if(checkUser(uname)):
        newname=input('Enter New Name: ')
        if(checkUser(newname)):
            print('This username already exists!!')
        
        else:
            user[newname]=user[uname]
            del user[uname]
    
    else:
        print('User Does Not Exist!!\n')

def renameFile(currUser):
    fname=input('Enter File Name: ')
    if(checkFile(currUser,fname)):
        newName=input('Enter New File Name: ')
        if(not checkFile(currUser,newName)):
            user[currUser].remove(fname)
            user[currUser].append(newName)
            print('File Renamed!!\n')        
        else:
            print('File Name Already Exists!!\n')
    
    else:
        print('File Does Not Exist!!\n')

def deleteUser():
    uname=input('Enter UserName: ')
    if(checkUser(uname)):
        del user[uname]
        print('User Deleted!!\n')
    else:
        print('User Does Not Exist!!')

def deleteFile(currUser):
    fname=input('Enter File Name: ')
    if(checkFile(currUser,fname)):
        user[currUser].remove(fname)
        print('File Deleted!!\n')
    
    else:
        print('File Does Not Exist In This Users Directory')

def changeUser():
    
    uname=input('Enter User Name :')
    if(checkUser(uname)):
        return uname
    else:
        print('User Does Not Exist!!\n')

def display():
    
    for key,values in user.items():
        
        print('User ',key)
        print('Files:')
        for i in values:
            print(i,end=' ')
        print()











user=dict()
currUser='home'
while(True):
    print('Menu:\n')
    print('1>Create User 2>Create File 3>Rename User 4>Rename File 5>Delete User 6>Delete File 7>Change User 8>Display 9>Exit',sep='\n')
    op=int(input('Enter Option : '))

    if(op==1):
        createUser()

    
    elif(op==2):
        createFile(currUser)

    
    elif(op==3):
        renameUser()

    
    elif(op==4):
        renameFile(currUser)

    
    elif(op==5):
        deleteUser()

    
    elif(op==6):
        deleteFile(currUser)

    
    elif(op==7):
        currUser=changeUser()

    

    elif(op==8):
        display()

    elif(op==9):
        break