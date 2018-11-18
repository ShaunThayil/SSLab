def findLength(data):
    return int(len(data)/2 + 1*(len(data)%2!=0))


def recordSplitter(data):
    data=data.strip().split('^')
    if(data[-1]==''):
        del data[-1]
    return data



def hex_to_bin(binary):
    b=bin(int(binary,16))[2:-2]
    
    return b

def abs_loader(objcode):
    pgm_name,staddr,length=recordSplitter(objcode.readline())[1:]
    staddr=input('Enter Starting Address:-')
    staddr=int(staddr,16)
    print('Program Name:-',pgm_name,' ','Start Address:- ',hex(staddr)[2:],'Length:- ',length)
    prev_record=staddr
    for data in objcode.readlines():
        if(data=='\n'):
            continue
        code=recordSplitter(data)
        
        if(code[0]=='E'):
            break
        
        #print(code[3])
        recPointer,length,binary=int(code[1],16)+staddr,int(code[2],16),hex_to_bin(code[3])
        code=code[4:]
        diffRecord='|'
        if(recPointer!=prev_record):
            diffRecord=(recPointer-prev_record)
            for _ in range(2):
                print('|')
            print("After ",diffRecord,' Memory Locations')
            for _ in range(2):
                print('|')
        
        count=0
        #print(len(code),code)
        for line in code:
            if(binary[count]=='1'):
                change=hex(int(line[3:],16)+staddr)[2:]
                #print(change)
                line=line[:3]+change

            print(hex(recPointer),"   --    ",line)
            recPointer+=findLength(line)
            count+=1
        prev_record=recPointer

    print("Execution Starts At ",code[1])
    objcode.close()




    
























objcode=open("objcode_relocation.txt")

abs_loader(objcode)