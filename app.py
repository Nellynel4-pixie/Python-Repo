#Delete file | check existence

import os
if os.path.exists("try.txt"):
    os.remove("try.txt")
else:
    print("The file does not exist")




# Delete a file
#import os
#os.remove('try22.txt')

 
# Create a file
f = open("try2.txt", 'w')
#Write to file
f = open("try.txt", 'w')
f.write("Who is your favourite youtuber?")
f.close()

# Append to file
f = open("try.txt", 'w')
f.write("Who is your favourite youtuber?")
f.close()

# Reead file
f = open("try.txt", 'r')
print(f.readline())
rint(f.readline())

f.close()

if __name__ == "__main__":
    main()