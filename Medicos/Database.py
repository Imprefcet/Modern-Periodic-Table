from difflib import get_close_matches
class Database:
    def __init__(self):
        f=open('database.txt','r')
        self.data=f.read().split('\n')
        f.close()

    def initial(self):
        self.condition=[]
        self.doc=[]
        self.does=[]
        for m in self.data:
            i=m.split('\t')
            self.condition.append(i[1].lower())
            self.doc.append(i[2].lower())
            self.does.append(i[3].lower())

    def search(self,word):
        self.word=word.lower()
        if self.word in self.condition:
            return self.getResult()
        else:
            ListOfConditions=get_close_matches(word, self.condition,cutoff=0.1)
            #prompt user to select the name from the list
            flag=1
            for i in ListOfConditions:
                print(f"{flag}.{i}")
                flag+=1
            if len(ListOfConditions)>0:
                print('0.If not found')
                options=int(input("Enter your option"))
                if options<flag and options!=0:
                    self.word=ListOfConditions[options-1]
                    return self.getResult()
            else:
                return "Sorry your condition is not found"
                
    def getResult(self):
        i=0
        for condition in self.condition:
            if self.word==condition:
                return self.data[i].split('\t')
            i+=1
def main():
    d=Database()
    word=input("Enter the drug to be searched: ")
    d.initial()
    result=d.search(word)
    print(f"<Give your output that you want to add>:\nDoc: {result[2].title()}\nDoes:{result[3].title()}")
if __name__=='__main__':
    main()
