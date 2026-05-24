"""
Text Analyzer Tool
Analyzes input text and provides frequency, counts, and stats.
"""
def freq_char(a):
    a=a.replace(" ","").lower()
    freq={}
    for i in a:
        if i.islower():
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
    return freq
choice=1
print("==========Text Analyzer==========\n\n")
while choice!=0:
    mode=int(input("Enter 1 to Enter Text 2 to Insert File\n"))
    if mode==1:
        a=input("Enter Text:")
    else:
        fn=input("Enter FileName:")
        try:
            with open(fn,"r") as f:
                a=f.read()
        except:
            print("File not found")
            continue
    char_freq=freq_char(a)
    words=a.split()
    if char_freq=={}:
        print("\n\nEmpty/Invalid\n")
    else:
        with open("output.txt","w") as f:
            f.write("\n\n---Analysis---\n")
            #f.write(f"Input Text: {a}")
            max_list=sorted(char_freq.items(),key=lambda x:x[1],reverse=True)
            min_c=sorted(char_freq.items(),key=lambda x:x[1])
            f.write(f"The Three Frequent Letters are:")
            for ch,co in max_list[:3]:
                f.write(f"{ch}-{co}\n")
            ch,co=min_c[0]
            f.write(f"\nLeast Frequent: {ch}-{co}\n")
            f.write(f"Total Words: {len(words)}\n")
            f.write(f"Total Characters: {sum(char_freq.values())}")
        with open("output.txt","r") as f:
            print(f.read())
    choice=int(input("Enter 0 to exit and 1 to continue\n"))
    print("\n================================\n")
print("================================")