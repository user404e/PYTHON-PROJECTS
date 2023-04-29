print("TO DO LSIT - \n")

inp = ""

while True:
    
    file = open("to_do_list.csv","r")

    data = file.readlines()
    
    file.close()

    if data == []:
        print("\nList Is Empty ...")
    else:
        i=1
        print("")
        for work in data:
            print(i," " + work,end="")
            i += 1
        
    inp = input("\n_ : ")
        
    if inp[:inp.find(" ")].upper() == "REMOVE":
        
        if inp.upper() == "REMOVE ALL":
            
            data.clear()
            file = open("to_do_list.csv","w")
            file.writelines(data)
        
        else:
            
            work_num = int(inp[inp.find(" ")+1:])   
            data.pop(work_num-1)
                
            file = open("to_do_list.csv","w")
            file.writelines(data)
        
    elif inp.upper() == "CLEAR" or inp.upper() == "CLEAR ALL":
        
        data.clear()
        file = open("to_do_list.csv","w")
        file.writelines(data)
            
    elif inp[:inp.find(" ")].upper() == "ADD":
            
        work_name = inp[inp.find(" ")+1:]
        
        data.append(work_name + "\n")
        
        file = open("to_do_list.csv","w")
        
        file.writelines(data)
        
    elif inp.upper() != "END" or inp.upper() != "EXIT" or inp.upper() != "QUIT":
        
        break
        
    else:
            
        print("\nINVALID INPUT - ")
        
    file.close()
