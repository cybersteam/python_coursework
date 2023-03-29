import os

#print = "Don't do this!"
name = "stefan Mischook"
#print(name + "YO!" * 16 ) 
#print(name)
# creating a file



#aFile = open(os.path.expanduser("~/Desktop/file.txt"), "a")
try:
    aFile = open("/Users/stefanmischook/Desktop/file.txt", "w")
    for x in range(0, 15):
        aFile.write('\nHello Friends!')
    
    aFile.flush()
    aFile.close

except:
    print("Call the nerd police! Something happened!")    
print("It is done.")
