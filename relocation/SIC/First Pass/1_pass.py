import json
def check_length(pgm_name):
    
    diff=len(pgm_name)-6
    if(diff<0):
        l=[pgm_name]
        space=[" " for i in range(diff)]
        space.extend(pgm_name)
        new_str="".join(space)
        return new_str
    else:
        return pgm_name[:6]
    
        




def normalize(inp):
    res=inp.strip().split()
    if(len(res)==2):
        res.insert(0,'')
    elif(len(res)==1):
        res.insert(0,'')
        res.insert(2,'')
    
    return res
    

def add_label(label,symtab,locctr,lineNum):
    val=symtab.get(label,-1)
    if(val!=-1):
        print("Symbol Already Present In Symtab!!!\nLine",lineNum)
        exit(1)
    else:
        symtab[label]=locctr





def sic(source,destination):
    

    
     
    #Opening OPTAB 
    opfile=open("optab.txt")
    optab=json.load(opfile)
    opfile.close()
    
    inp=file.readline()
    if('#' in inp):
        inp=inp.split('#')[0]
    inp=normalize(inp)
     
    lineNum=0 
    locctr=0
    start_address=0
    pgm_name=""
    
    

    print("Before START: ",inp)
    if(inp[1]=="START"):
        locctr=start_address=int(inp[2])
        pgm_name=inp[0]
        lineNum=1
        print("Inside START!!")
        destination.write(hex(locctr)+" "+inp[1]+" "+inp[2]+"\n")
    else:
        file.seek(0)
    
    pgm_name=check_length(pgm_name)
    #Initializing Data Structures
    info_data={"start_address":str(start_address),"program_name":pgm_name}
    symtab={}
  
    
    for data in file.readlines():
        data=data.strip()
        code=data
        new_code="\n"
        if('#' in data):
            data=data.split('#')
            new_code='    #'+data[1]+"\n"
            code=data[0]
        
        code=normalize(code)
        lineNum+=1
        print(lineNum,"  ",code)
        label,opcode,operand=code
        
        if(label!=''):
            add_label(label,symtab,locctr,lineNum)
        
        
        if(opcode in optab.keys()):
            inc=3
        
        elif(opcode=='WORD'):
            inc=3
        
        elif(opcode=='RESB'):
            inc=int(operand)
        
        elif(opcode=='RESW'):
            inc=3*int(operand)
        
        elif(opcode=='BYTE'):
            inc=len(operand[2:-1])
            if(operand[0]=='X'):
                if(inc%2==0):
                    inc=int(inc*0.5)
                else:
                    inc=int(inc*0.5+1)
        elif(opcode=='END'):
            l=0
        else:
            print("Invalid OPCODE!!\nLine:",lineNum)
            exit(1)
         

        

        new_code=hex(locctr)+" "+opcode+" "+operand+new_code
        destination.write(new_code)
        locctr+=inc
    
    source.close()
    destination.close()


    #File To Save MetaData
    info=open("info.txt",'w')

    pgm_length=locctr-start_address
    info_data['length']=str(pgm_length)
    json.dump(info_data,info)
    info.close()
    
    #File To Save Symtab
    symtab_file=open("symtab.txt",'w')
    json.dump(symtab,symtab_file)
    symtab_file.close()
            


    











fname="sample_sic.txt"                                  #input("Enter Source File Name:")
file=open(fname)
fname="intermediate.txt"                                                  #input("Enter Destination File Name:")
target=open(fname,'w')

sic(file,target)