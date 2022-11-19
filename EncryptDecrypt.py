from cryptography.fernet import Fernet
#import os
#os.chdir("E:\PythonForNetworking\Cryptography")

Options = (input("Would you like to [encrypt] or [decrypt]? "))
Options="Pizza"
Options = Options.lower()
while not (Options == str("encrypt")) and not (Options == (str("decrypt"))):
    print("Invalid Option")
    Options = (input("Would you like to [encrypt] or [decrypt]? "))
    Options = Options.lower()
    
if Options.lower() == str("encrypt"):
    #get input from user
    message = input("Enter a message to be encrypted: ")
    userFileName = input("What would you like to name this file: ")
    userFileName = (userFileName + ".txt")

    #make the key and save it to a file. taunt user with witty file name.
    key = Fernet.generate_key()
    with open("iDidntCopyIt.txt", "wb") as userKey:
        userKey.write(key)
        userKey.close()
    print(f"Your key is: \n{key} \nCopy this key as it will be used for decryption. \nNote: it has also been saved to a file \"iDidntCopyIt.txt\"")

    #Make the file
    with open(userFileName, "w") as userFN:
        userFN.write(message)
        userFN.close()


    #Encrypt the file 
    f = Fernet(key)

    with open(userFileName, "rb") as userFN:
        ruserFN = userFN.read()

    encrypted = f.encrypt(ruserFN)

    with open("encrypted" + userFileName, "wb") as encUserFile:
        encUserFile.write(encrypted)

######################################################################### 
elif Options.lower() == str("decrypt"):

    #Decrypting file
    decryptKey = input("Paste in your key here: ")
    encryptedFilename = input("I know youd be back.... \nPlease provide the full name of the file: ")
    #print(decryptKey + " " + encryptedFilename)


    ff = Fernet(decryptKey)
    #encrypted = decryptKey.encrypt(a)

    with open(encryptedFilename, "rb") as encryptedFile:
        a = encryptedFile.read()
        #print(a)

    decryptedOutput = ff.decrypt(a)
    print(decryptedOutput)

    with open ("decrypted" + encryptedFilename, "wb") as decryptedFile:
        decryptedFile.write(decryptedOutput)

else:
    exit
