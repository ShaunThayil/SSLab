import json
optab=json.load(open("optab.txt"))
symtab=json.load(open("symtab.txt"))
info=json.load(open("info.txt"))


def breakcommand(data):
    res=data.split()
    if(len(res)==2):
        res.insert(2,"")
    
    return res 

def normalize(data,maxlen,inpSymbol):
    res=""
    data=str(data)
    if(inpSymbol=='0'):     #For Hex Normalization
        data=data[2:]

    if(len(data)==maxlen):
        res=data
    else:
        
        diff=maxlen-len(data)
        for i in range(diff):
            res+=inpSymbol
        res+=data
    return res

def headMaker(source,objectcode):
 
    data=source.readline().split('#')
    
    
    code=data[0].strip()
    print(code)
    length=info["length"]
    line=['H']
    location,opcode,operand=breakcommand(code)
    
    if(opcode=='START'):
        pgmname=info['program_name']
        
        
    else:
        source.seek(0)
    line.append(normalize(pgmname,6,' '))
    line.append(normalize(location,6,'0'))
    line.append(normalize(int(length),6,'0'))
    line.append("\n")
    
    objectcode.write("^".join(line))
        
    
def createText(location):
    return ['T',normalize(location,6,'0')]

def validInst(opcode,operand):
    
    instcode=optab[opcode]
    l=operand.split(',')
    X=0
    if(len(l)==2):
        operand=l[0]
        X=1
    
    
    
    o=symtab.get(operand,None)
    
    if(operand!="" and o==None):
            print("Invalid Operand")
            exit(1)
        
    if(operand==""):
         symcode='0000'
    else:
        symcode=normalize(hex(symtab[operand]),4,'0')
    
    


    
    
    if(X==1):
        symlist=list(symcode)
        a=int(symlist[0])
        symlist[0]=hex(8|a)
        symcode=''.join(symlist)
    
    inst=instcode+symcode
    return inst
      


    
    



line=['T']

def sic_2pass(source):
    #Loading Data
    objectcode=open("objcode.txt",'w')
    
    headMaker(source,objectcode)
    textrec=0
    
    for data in source.readlines():         #textrec is used to store the length of the present record
        res=0
        code=data.split('#')
        if(code[0]==''):
            continue
        
        else:
            location,opcode,operand=breakcommand(code[0].strip())
       
        print(location," ",opcode,' ',operand)
        command=''
        if(opcode=='END'):
            break
        
        if(opcode in optab.keys()):
            command=validInst(opcode,operand)
            inc=3
            
        elif(opcode=='WORD'):
                command=normalize(hex(int(operand)),6,'0')
                inc=3
        
        elif(opcode=='BYTE'):
            val=operand[2:-1]
            if(operand[0]=='C'):
                inc=len(val)
                for i in val:
                    command+=hex(ord(i))[2:]
                    
            elif(operand[0]=='X'):
                command+=val
                if(len(val)%2==0):
                    inc=int(len(val)/2)
                else:
                    inc=int(len(val)/2+1)
        
        elif(opcode=='RESW' or opcode=='RESB'):
            res=1
        
        else:
            print("Invalid Instruction")
            exit(1)
        

        
        recsize=textrec+inc 
        if(recsize>30 or res==1):
            textrec=0        #reset record size variable 
            line.append('\n')
            line.insert(2,normalize(hex(recsize),2,'0'))
            objectcode.write("^".join(line))
            if(res==1):
                continue
        
        if(textrec==0):      #Create New  Record  
            line=createText(location)

        textrec=recsize
        line.append(command)
        
        
    objectcode.write("E^"+normalize(operand,6,' '))
    objectcode.close()


                    

        
if(__name__=="__main__"):
    source=open("intermediate.txt")
    sic_2pass(source)
