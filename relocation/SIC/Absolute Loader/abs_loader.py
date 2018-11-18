def findLength(data):
    return int(len(data)/2 + 1*(len(data)%2!=0))


def recordSplitter(data):
    data=data.strip().split('^')
    if(data[-1]==''):
        del data[-1]
    return data

def abs_loader(objcode):
    pgm_name,staddr,length=recordSplitter(objcode.readline())[1:]
    
    print('Program Name:-',pgm_name,' ','Start Address:- ',staddr,'Length:- ',length)
    
    prev_record=int(staddr,16)
    for data in objcode.readlines():
        if(data=='\n'):
            continue
        code=recordSplitter(data)
        
        if(code[0]=='E'):
            break
        
        recPointer,length=int(code[1],16),int(code[2],16)
        code=code[3:]
        diffRecord='|'
        if(recPointer!=prev_record):
            diffRecord=(recPointer-prev_record)
            for _ in range(2):
                print('|')
            print("After ",diffRecord,' Memory Locations')
            for _ in range(2):
                print('|')

        for line in code:
            
            print(hex(recPointer),"   --    ",line)
            recPointer+=findLength(line)
        prev_record=recPointer

    print("Execution Starts At ",code[1])
    objcode.close()




    
























objcode=open("objcode.txt")

abs_loader(objcode)