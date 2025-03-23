print("hellow python")
name=input("enter new text")
charac=len(name)
a = name.replace(" ","")
print (charac)

words = []
for i in range (5):
    word = input (f"enter word {i + 1}:")
    words.append(word)
    print("length of words entered:")
    for word in words:
    
        print (f" The word '{word}' has {len(word)} characters")
    