from Crypto.Cipher import AES,PKCS1_OAEP,Blowfish,DES,ARC4
from Crypto.Random import get_random_bytes
import os,random
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad,unpad






def aes():
    

    choices=int(input("1-Encryt the Text\n2-Encrypt the File Content\nYour Choice: "))
    if choices==1:
        text_for_aes=input("Enter the Text: ")
        our_key=get_random_bytes(32)

        attr_a=AES.new(our_key,AES.MODE_CBC)
        attr_b=attr_a.encrypt(pad(text_for_aes.encode(),AES.block_size))
        print("Encrypted Text-------->"+str(attr_b))

        


        attr_c=AES.new(our_key,AES.MODE_CBC,attr_a.iv)
        attr_d=unpad(attr_c.decrypt(attr_b),AES.block_size)
        #print("*"*30)
        print("\nDecrypted Text---------->"+str(attr_d.decode()))
        print("\n"*2)

    elif choices==2:
        file_name=input("Enter the File Path: ")
        if os.path.exists(file_name):
            f=open(file_name,"rb")
            for real_text in f.readlines():
                
                our_aes_key=get_random_bytes(32)

                attr_1=AES.new(our_aes_key,AES.MODE_CBC)
                attr_2=attr_1.encrypt(pad(real_text.decode().encode(),AES.block_size))
                print("Encrypted Text-------->"+str(attr_2))

                


                attr_3=AES.new(our_aes_key,AES.MODE_CBC,attr_1.iv)
                final=unpad(attr_3.decrypt(attr_2),AES.block_size)
                
                print("\nDecrypted Text---------->"+str(final.decode()))
                print("\n"*2)
    else:
        print("Wrong Number!!!")
        SystemExit
def otp():
    
    def create_key(lenght)->str:
        key=""
        for i in range(lenght):
            key+=chr(random.randint(0,1)+48)
        return key

    def encrypt(text,key_parameter):
        encryption=""
        for i in range(len(text)):
            encryption+=chr(ord(text[i])^ord(key_parameter[i]))
        return encryption

    while True:

        text_for_otp=input("\nEnter the Text: ")
        
        our_otp_key=create_key(len(text_for_otp))
        final=encrypt(text_for_otp,our_otp_key)
        print("\nReal Text------------>"+"\t"+text_for_otp+"\t"*2+"|"*2+"\t"+"\nEncrypted Text----------->"+"\t"+str(final))
def rc4():
    

    text_for_rc4=bytes(input("Enter the Text: ").encode())

    our_rc4_key=get_random_bytes(32)

    attr=ARC4.new(our_rc4_key)

    encrypted=attr.encrypt(text_for_rc4)
    print("\nEncrypted Text--------->"+str(encrypted))
def rsa():
    


    text_for_rsa=bytes(input("Enter the text:").encode())
    
    our_rsa_key=RSA.generate(2048)
    attr=PKCS1_OAEP.new(our_rsa_key.public_key())#public key şifrelemek için
    encrypted=attr.encrypt(text_for_rsa)
    print("\nEncrypted text--------------->"+str(encrypted))

    our_private_key=our_rsa_key.export_key()
    with open("our_private.pem","wb") as f:
        f.write(our_private_key)

    our_key=RSA.import_key(open("our_private.pem").read())
    cipher=PKCS1_OAEP.new(our_key)
    real_text=cipher.decrypt(encrypted);print("\nReal Text------->"+str(real_text.decode()))
def blowfish():
    
    key=get_random_bytes(16)
    iv=get_random_bytes(8)

    text_for_blowfish=bytes(input("Enter the Text:").encode())
    

    attr=Blowfish.new(key,Blowfish.MODE_CBC,iv)
    text=pad(text_for_blowfish,Blowfish.block_size)
    sonuc=attr.encrypt(text)



    nesne_2=Blowfish.new(key,Blowfish.MODE_CBC,iv)
    cozulmus=nesne_2.decrypt(sonuc)
    sonuc_2=unpad(cozulmus,Blowfish.block_size)
    print("\nEncrypted text--------->"+str(sonuc)+"\t\n"+"\nDecrypted text-------->"+"\t"+str(sonuc_2.decode()))
def des():
    


    text_for_des=bytes(input("Enter the Text: ").encode())
    key=get_random_bytes(8)

    attr_1=DES.new(key,DES.MODE_ECB)
    attr_2=pad(text_for_des,DES.block_size)
    chiper=attr_1.encrypt(attr_2);print("\nEncrypted text------------->"+str(chiper.hex()))

    new_des=DES.new(key,DES.MODE_ECB)
    answer=unpad(new_des.decrypt(chiper),DES.block_size)
    print("\nDecrypted text------------->"+str(answer.decode()))

encryption_types=int(input("1-aes\n2-otp\n3-rc4\n4-rsa\n5-blowfish\n6-des\nYour Choice: "))
if encryption_types==1:
    aes()
elif encryption_types==2:
    otp()
elif encryption_types==3:
    rc4()
elif encryption_types==4:
    rsa()
elif encryption_types==5:
    blowfish()
elif encryption_types==6:
    des()
else:
    print("Wrong Number!")
    SystemExit
