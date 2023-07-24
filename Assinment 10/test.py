
def main():
    
    inFile = open("super.txt","r")

    oFile = open("userid.txt","w")
    

    line= inFile.readline()

    while line!="":
        name_list = line.split()
        print(name_list)
        
        first_name = name_list[0]
        last_name=name_list[1]
        user_id= first_name[0]+last_name
        
        print(user_id)

        oFile.write(user_id)
        line =inFile.readline()
        

    inFile.close()
    oFile.close()    
    

    

  
    
main()
