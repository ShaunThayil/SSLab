
#This Funtion returns The Pointer To The Directory In Which Is At The End Of The Path    root/shaun <----Pointer To shaun
#Assume dir is the root folder
def findPath(path):
    
    path=path.split('/')
    if(path[0]!='root'):    # If Not Root There Is An Error In Path
        return False
    next=dir                #Set A Variable Pointing To The Root Directory
    if(len(path)==1):
        return next
    del path[0]    #No Need Of Root
    for i in path:
        next=next[0].get(i,None)
        if(next==None):
            return False
    return next

#To Check if a file is in a particular directory or not
#Input Parameters:- (pointer to directory,Filename)
#Return Value :-If Present(Index Of the file in the list)
#               Else:(-1)
def checkFile(directory,fname):
    if(fname in directory):
        return directory.index(fname)
    else:
        return -1

#To Check if a directory is in a particular directory or not
#IP Parameters:(pointer to directory,SubDirectory Name)
#Output: True/False
def checkDir(directory,dname):
    if(dname in directory[0]):
        return True
    
    else:
        return False

#To Create A File/Directory in a given directory
#Input flag(f/d)

def create(flag):
    path=input('Enter  Path as A1/A2/A3: ')
    directory=findPath(path)
    
    if(directory==False):
        print('Path Does Not Exist!!')
        return
    
    name=input('Enter Name: ')
   
    if(flag=='f'):
        if(checkFile(directory,name)>0):
            print('File Already Exists!!\n')
            return

        else:
            directory.append(name)
            print('File Created!!')
    
    elif(flag=='d'):
        if(checkDir(directory,name)==True):
            print('Directory Already Exists!!\n')
            return
    
        directory[0][name]=[{}]
        print('Directory Created!!')




def rename(flag):
    path=input('Enter Path:')
    directory=findPath(path)

    if(directory==False):
        print('Path Does Not Exist!!')
        return
    
    name=input('Enter  Name')
    if(flag=='f'):
        index=checkFile(directory,name)
        if(index<0):
            print('File Does Not Exist!!')
            return
        newname=input('Enter New Name:')
        if(checkFile(directory,newname)>0):
            print('New Name File Already Exists!!\n')

        directory[index]=newname
    
    elif(flag=='d'):
        if(checkDir(directory,name)==False):
            print('Directory Does Not Exist!!\n')
            return

        newname=input('Enter New Directory Name: ')
        if(checkDir(directory,newname)==True):
            print('New Directory Name Already Exists!!\n')
            return

        directory[0][newname]=directory[0][name]
        del directory[0][name]




    
    


def delete(flag):
    path=input('Enter Path: ')
    directory=findPath(path)
    if(directory==False):
        print('Path Does Not Exist!!')
        return
    
    name=input('Enter Name :')
    if(flag=='f'):
        
        index=checkFile(directory,name)
        if(index<0):
            print('File Does Not Exist!!\n')
            return
        
        del directory[index]
    
    elif(flag=='d'):
        if(checkDir(directory,name)==False):
            print('Directory Does Not Exist!!\n')
            return
        
        del directory[0][name]



def display():
    print(dir)


def move(flag,movetype):
    path1=input('Enter  Path :')
    directory1=findPath(path1)
    if(directory1==False):
        print('Incorrect Path!!')
        return
    name=input('Enter Name: ')
    if(flag=='f'):
        index=checkFile(directory1,name)
        if(index<0):
            print('File Does Not Exist!!\n')
            return
        
        path2=input('Enter Target Directory Path: ')
        directory2=findPath(path2)
        if(directory2==False):
            print('Directory Does Not Exist')
            return
        if(checkFile(directory2,name)>=0):
            print('File Already Exists!!\n')
            return
        
        directory2.append(name)
        if(movetype=='cut'):
            del directory1[index]
            print('File Moved!!!\n')
        else:
            print('File Copied!!\n')   
          
    
    elif(flag=='d'):
        path2=input('Enter Target Directory Path: ')
        directory2=findPath(path2)
        if(directory2==False):
            print('Directory Does Not Exist')
            return
        
        if(checkDir(directory2,name)==True):
            print('Directory Already Exists!!')
            return
        
        directory2[0][name]=directory2[0][name]
        if(movetype=='cut'):
            del directory1[0][name]
            print('Directory Moved!!!\n')
        else:
            print('Directory Copied!!\n')


    
   
  


    










dir=[{}]
while(True):
    print('\n\n\n1>Create File\n2>Create Directory\n3>Rename File\n4>Rename Directory\n5>Delete File\n6>Delete Directory\n7>Cut file\n8>Cut Directory\n9>Copy File\n10>Copy Directory\n11>Display\n12>Exit')
    op=int(input('Enter Option: '))
    if(op==1):
        create('f')
    elif(op==2):
        create('d')
    elif(op==3):
        rename('f')
    elif(op==4):
        rename('d')
    elif(op==5):
        delete('f')
    elif(op==6):
        delete('d')
    elif(op==7):
        move('f','cut')
    elif(op==8):
        move('d','cut')
    elif(op==9):
        move('f','copy')
    elif(op==10):
        move('d','copy')
    elif(op==11):
       display() 
    elif(op==12):
        break



