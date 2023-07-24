#This program wiil go input and out put files 
# File:  passw0rdjayden.py
# Project:Assignment10: Input and Output Files
# Author:  Jayden Alexander 
# History: Version 3.10


'''
the password uses the following criterias


The password should be at least 12 characters strong. 
 The password should contain EXACTLY TWO upper case letters.
 The password should have EXACTLY TWO digits.
 The password should contain EXACTLY ONE special character like $ or ! or %. 
 The password should not contain any spaces.
 The password should contain all remaining lower case letters

and sould read the given input file passwdin.txt

'''


def main():
    #opens read file
    inFile = open("passwdin.txt", "r")
    oFile = open("jaydenpasswdout.txt","w")
    
    #if msg return false print reason it is false 
    for pss in inFile:
        
        valid, msg = check_password_jayden(pss)

        if valid ==True:
            print(msg)
            oFile.write(msg + "\n")
            
        else:
            pss_strip= pss.strip()
            error = f"{pss_strip} - password not accepted because of following conditions.\n"
            error+=(msg)
            print(error)
            oFile.write(error +"\n")
    inFile.close()
    oFile.close()
    
def check_password_jayden( pss ):
    #count for each criteria
    l_case_count=0
    up_case_count= 0
    digit_count = 0
    spl_char_count = 0
    space_count=0
    size = len(pss)
    pss_strip = pss.strip("\n")
    #for loop that goes through each character
    for char in pss_strip:
    
        if char.isupper():
            up_case_count+=1
            
            
        elif char.isdigit():
            digit_count+=1
            
            
        elif char.isspace():
            space_count+=1
            
        elif char.islower():
            l_case_count+=1
            
        else:
            spl_char_count +=1
            
        #print(char)
    
    
    #print(up_case_count)
    #print(digit_count)
    #print(spl_char_count)
    #print(space_count)
    
   
        
    #if count is not equal to desired amount than retun why pass word was not accepted    
    if size >= 12 and up_case_count ==2 and digit_count ==2 and space_count == 0 and spl_char_count == 1:
        msg = f"{pss_strip} - password is accepted \n"
        return True,msg
    else:
        msg = ""
        if size <12:
            msg += "Password has to have at least 12 characters. \n"
        if up_case_count !=2:
            msg += "password should contain at EXACTLY 2 uppercase letters. \n"
        if digit_count != 2:
            msg += "password should contain at EXACTLY 2 digits. \n"
        if space_count != 0:
            msg+= "password should not contain any spaces. \n"
        if spl_char_count != 1:
            msg+= "The password should contain only one special character. \n"
        return False, msg
            
  


 
   
 

  
 
main()
    
