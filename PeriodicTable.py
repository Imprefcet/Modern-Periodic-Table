class PeriodicTable():
    def add(self):
        f=open("PeriodicTable.txt",'a')
        f.write('\n')
        f.write(input("Enter the Atomic Number\n"))
        f.write('\t')
        f.write(input("Enter the Element Name\n"))
        f.write('\t')
        f.write(input("Enter the Element Symbol\n"))
        f.write('\t')
        f.write(input("Enter the Atomic mass\n"))
        f.write('\t')
        f.write(input("Enter the Number of Neutrons\n"))
        f.write('\t')
        f.write(input("Enter the Number of protons\n"))
        f.write('\t')
        f.write(input("Enter the Number of Electrons\n"))
        f.write('\t')
        f.write(input("Enter the Period of the element\n"))
        f.write('\t')
        f.write(input("Enter the Group of the element\n"))
        f.write('\t')
        f.write(input("Enter the Phase of the element(Solid,Liquid,Gas)\n"))
        f.write('\t')
        f.write(input("Enter the Radio Active\n"))
        f.write('\t')
        f.write(input("Enter if the element is Naturally found\n"))
        f.write('\t')
        f.write(input("Enter if the element is a Metal\n"))
        f.write('\t')
        f.write(input("Enter if the element is a Non-Metal\n"))
        f.write('\t')
        f.write(input("Enter if the element is a Metalloid\n"))
        f.write('\t')
        f.write(input("Enter the Type of the Metal(Metal,Nonmetal,Metalloid)\n"))
        f.write('\t')
        f.write(input("Enter the Atomic Radius\n"))
        f.write('\t')
        f.write(input("Enter the Electronegativity of the element\n"))
        f.write('\t')
        f.write(input("Enter the First Ionization\n"))
        f.write('\t')
        f.write(input("Enter the Density\n"))
        f.write('\t')
        f.write(input("Enter the Melting Point\n"))
        f.write('\t')
        f.write(input("Enter the Boiling Point\n"))
        f.write('\t')
        f.write(input("Enter the Number of Isotopes\n"))
        f.write('\t')
        f.write(input("Enter the Discoverer\n"))
        f.write('\t')
        f.write(input("Enter the Year\n"))
        f.write('\t')
        f.write(input("Enter the Specific Heat\n"))
        f.write('\t')
        f.write(input("Enter Number of shells\n"))
        f.write('\t')
        f.write(input("Enter Number of Valence\n"))
        f.close()
        
    def printIt(self,List,KeyList):
        for number in range(len(KeyList)):
            print(KeyList[number],':',List[number])
        print('\n')

    def result(self,option,elementSearch):
        f=open("PeriodicTable.txt",'r')
        data=f.read().split('\n')
        flag=0
        KeyList=data[0].split('\t')
        print(KeyList)
        for i in data:
            List=i.split('\t')
            if option == 1:
                flag=1
                if elementSearch.lower()==List[1].lower():
                    print('\nElement found\n')
                    self.printIt(List,KeyList)
                    break
            if option == 2:
                if elementSearch==List[2]:
                    print('\nElement found\n')
                    flag=1
                    self.printIt(List,KeyList)
                    break
            if option == 3:
                if elementSearch==int(List[0]):
                    print('\nElement found\n')
                    flag=1
                    self.printIt(List,KeyList)
                    break
            if option == 4:
                if round(elementSearch)==round(float(List[3])):
                    print('\nElement found\n')
                    flag=1
                    self.printIt(List,KeyList)
                    break
        f.close()
        if flag==0:
            print("\nSorry element not found\n")
            
    def explore(self):
        print('\n')
        check=True
        while check:
            try:
                print("1.Search by element")
                print("2.Symbol")
                print("3.Atomic number")
                print("4.Atomic Weight")
                option=int(input("Enter Your Option\n"))
                if option>0 and option<5:
                    check=False
                    if option==1:
                        elementSearch=input("Enter the element to be searched\n")
                    elif option==2:
                        elementSearch=input("Enter the symbol to be searched\n")
                    elif option==3:
                        elementSearch=int(input("Enter the Atomic Number to be searched\n"))
                    elif option==4:
                        elementSearch=float(input("Enter the Atomic Weight to be searched\n"))
                    self.result(option,elementSearch)
                else:
                    print("\nPlease enter a number from 1-4\n")
            except ValueError:
                print('\nPlease Enter a number\n')

def main():
    pt=PeriodicTable()
    while True:
        try:
            print('1.Add new element')
            print('2.Explore')
            print('3.End')
            a=int(input('Enter your choice\n'))
            if a==1:
                pt.add()
            elif a==2:
                pt.explore()
            elif a==3:
                break
            else:
                print("\nYour have entered a wrong number\n")
        except ValueError:
            print("\nPlease enter a number\n")

                    
if __name__=='__main__':
   main()
