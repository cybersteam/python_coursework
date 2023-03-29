import re

def read_lines():
    #we're going to be counting something so we need a number to start with
    count = 0
    try:
        with open("tx1.txt") as the_file:
            #we need an object that holds the lines that are read each count
            lines = the_file.readlines()
            #everytime we read a new line we put it into a variable called "line"
            for line in lines:
                #increment the count variable
                count += 1
                # prints the count and the line
                print("Line " + str(count) + ": " + line)

    except OSerror as Booboo:
        print("we had a booboo")
        print(Booboo)

def read_and_search():
        try:
            with open("tx1.txt") as the_file:
                lines = the_file.readlines()
                for line in lines:
                    # rstrip() takes out empty spaces, line breaks etc.
                    # without it here we would need Lucy to be the only thing on the line
                    if line.rstrip() == "Lucy":
                        print("---> we found Lucy!")
        except OSerror as Booboo:
            print(line)

def reading_lines_with_find():
    try:
        with open ("tx1.txt") as the_file:
            lines = the_file.readlines()
            for line in lines:
                # here it looks for Lucy in the lines and if it doesnt find it then it returns -1 !!!
                hit = line.find("Lucy")
                if hit != -1:
                    print("we found Lucy in the line of text!\n")
                else:
                    print(line)
    except OSerror as Booboo:
        print("we had a booboo")
        print(Booboo)

#here we create a regex function to use for finding a pattern in strings
def regex_magic(pattern, string):
    object_match = re.search(pattern, string)
    return object_match

def reading_lines_with_regex():
    try:
        with open("tx1.txt") as the_file:
            lines = the_file.readlines()
            print("\n")
            for line in lines:
                pattern = "Lucy"
                #pattern = "^Lucy"   -----> search for it at the beginning of a line
                #pattern = "Lucy$" - -----> search for it at the end of a line
                if str(regex_magic(pattern, line)) == "None":
                    print(line)
                else:
                    print("--> we found the text" + pattern + ", in the line")
    except OSerror as booboo:
        print("it was a boobbpoio")
        print(Booboo)




#read_lines()
#read_and_search()
#reading_lines_with_find()
reading_lines_with_regex()
