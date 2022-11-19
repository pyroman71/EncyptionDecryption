# EncyptionDecryption
encryption and decryption for assignment Publish a python module on github

Required: 
Python 3.4+
 Module: cryptography
 pip install cryptography
 
 
 Run EncryptDecrypt.py
 
 You will be prompted with "Would you like to [encrypt] or [decrypt]? "
 Select "encrypt" to proceed with encrypting a file or decrypt to begin decrypting a previously encrypted file
 
 ################################ ENCRYPT #######################################
 
Prompt: "Enter a message to be encrypted: "
- Enter a message here to be encrypted

Prompt: "What would you like to name this file: "
- This will provide the name of the file (note: it will append .txt to the end to make files readable in text editors)

Prompt:   "Your key is:
          {key} 
          Copy this key as it will be used for decryption. 
          Note: it has also been saved to a file "iDidntCopyIt.txt"
          
- You will receive your encryption key in the {key} location, as well as a file "iDidntCopyIt.txt" storing your key if you opt not to copy it.  This file will be saved to the directory which you run the script from.



 ################################ DECRYPT #######################################
 Prompt:  "Paste in your key here: "
 - Provide the key received during the encryption process
 - *NOTE* the key has also been saved to a file called "iDidntCopyIt.txt" in the directory which the script was run from

 Prompt:    "I know youd be back.... 
            Please provide the full name of the file: "
 
 - Provide the name of the encrypted file to be decrypted
 - **NOTE** the file must be from the same session where the key was generated.

