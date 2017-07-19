(name,password,phrase,isTrue)=(input(),input(),"",0) ### Username password etc
openFile=open("Users.txt","r")
File=openFile.read()
for letter in File: ### getting user code
    if isTrue==1:
        if phrase==password:
            isTrue=2
    elif phrase==name:
        isTrue=1
    if isTrue==2 and letter == "\n":
        userCode=phrase
        isTrue=3
        break
    elif letter==" "or letter=="\n":
        phrase=""
    else:
        phrase+=letter
if isTrue==3:
    fileName=input() #### opening file
    openFile=open(userCode+"_"+fileName+".txt","r")
    file=openFile.read()
    print(file)
    openFile.close
    with open("logs.txt", "a") as file: ### loging that file was opend
      file.writelines(userCode+"_"+fileName+"\n")
    input()
else:
    input("Invalid name of password")
