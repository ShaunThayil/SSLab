def checkDir(fname):
    if(fname in root):
        return root.index(fname)
    else:
        return -1


def createFile():
    fname=input('Enter File Name: ')
    index=checkDir(fname)

    if(index>=0):
        print('File Already Exists!!!\n')
    else:
        root.append(fname)
        print('File Created!!\n')
    
def renameFile():
    fname=input('Enter File Name: ')
    
    index=checkDir(fname)

    if(index>=0):
        newName=input('Enter New File Name:')
        if(checkDir(newName)<0):
            root[index]=newName
            print('File Renamed!!\n')
        else:
            print('New Name File Already Exists!!\n')
    else:
        print('File Does Not Exist!!\n')
    
        
def  deleteFile():
    fname=input('Enter File Name : ')
    index=checkDir(fname)
    if(index<0):
        print('File Does Not Exist!!\n')
       
    
    else:
        root.remove(fname)
        print('File Deleted!!\n')
 

def displayFiles():
    if(len(root)==0):
        print('Directory Empty!!\n')
        return
    for i in root:
        print(i)
    
    print()










root=[]
while(True):
    print('1>Create File 2>Rename File 3>Delete File 4>Display  5>Exit')
    op=int(input('Enter Option: '))
    if(op==1):
        createFile()

    
    elif(op==2):
        renameFile()

    

    elif(op==3):
        deleteFile()

    
    elif(op==4):
        displayFiles()

    
    elif(op==5):
        break