f=open('database.txt','a')
timestamp=input("Enter the time: ")
condition=input("Enter the condition: ")
doc=input("Enter the doc: ")
does=input("Enter the does: ")
confirmation=input("Y for confirmation: ").lower()
if confirmation=='y':
    s='\n'+timestamp+'\t'+condition+'\t'+doc+'\t'+does
    f.write(s)
else:
    print("Your operation was discarded")

f.close()
