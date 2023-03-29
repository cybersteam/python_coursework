#file manipulation

class Filer():
    def open_file(self):
        #using the open function to open the text file create the file_object
        try:
            with open("tx1.txt") as file_object:
            #create a new object that passes the file_object to the read function
                contents = file_object.read()
                print(contents)
        except:
            print("no file was found")
        else:
            print("I found the file")


    def open_file2(self, file):
        '''
        #This is the same thing but using a new function "file" as the required argument
        # when calling the function later on you can then pass whatever file you want to it...
        # much more flexible code!!!
        '''
        try:
            with open(file) as file_object:
                contents = file_object.read()
                print(contents)
        except:
            print("no file was found")
        else:
            print("I found the file")

    def write_tofile(self, filename, texttowrite):
        try:
            with open(filename, "w") as file_object:
                file_object.write(texttowrite)
        except:
            print("file not found")
        else:
            print("the file was found and I wrote" + texttowrite)

    def add_tofile(self, filename, texttoadd):
        try:
            with open(filename, "a") as file_object:
                file_object.write(texttoadd)
        except:
            print("filenot found")
        else:
            print("the file was found and I added" + texttoadd + "to it")


myWriter = Filer()
myAdder = Filer()
#filer_go.open_file()
#filer_go.open_file2("tx2.txt")
#filer_go.open_file2("test.csv")
myWriter.write_tofile("tx1.txt","This is the new text")
myAdder.add_tofile("tx1.txt", "Some new added text")
