import numpy as np


class DataAnalytics:
    def __init__(self):
        self.main_arr = None

    def create_arr(self):

        try:
            
            print("Select the Type of array to Create :")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            ch=int(input("Enter Your Choice :"))
            if ch==1:
                el=input("Enter Elements for 1D Array : ").split()
                arr=list(map(int,el))
                self.main_arr=np.array(arr)
                self.arr = self.main_arr
                print(f"Elements : {self.self.main_arr}")
                
                print("Elements Added Sucessfully!")
                return self.main_arr
            elif ch==2:
                row=int(input("Enter the Number of Rows:  "))
                cols=int(input("Enter the Number of Columns:  "))
                
                el=input(f"Enter {row*cols} Elements for the Array Separated By Space :").split()
                arr=list(map(int,el))
                self.main_arr=np.array(arr).reshape(row,cols)
                self.arr = self.main_arr
                print(f"Elements : {self.main_arr}")
                print("Elements Added Sucessfully!")
                return self.main_arr
            elif ch==3:
                dep=int(input("Enter Depth (in Blocks): "))
                row=int(input("Enter the Number of Rows: "))
                cols=int(input("Enter the Number of Columns: "))
                
                el=input(f"Enter {row*cols*dep} Elements for the Array Separated By Space :").split()
                arr=list(map(int,el))
                self.main_arr=np.array(arr).reshape(dep,row,cols)
                self.arr = self.main_arr
                print(f"Elements : {self.main_arr}")
                print("Elements Added Sucessfully!")
                return self.main_arr
        except:
            print("There was an Error in  Creating  Array!")
                    
    def indexing_slicing(self,main_arr):
        try:
            while True:
                print("Choose an Option :")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back To Main Menu")
                cho=int(input("Enter Your Choice : "))

                if cho==1:
                    if main_arr.ndim==1:
                        ind=int(input("Enter a Index Number : "))
                        print("Indexed Array:")
                        print(self.main_arr[ind])
                    elif main_arr.ndim==2:
                        
                        ind=int(input("Enter a Row Number : "))
                        ind2=int(input("Enter a Column Number :"))
                        print("Indexed Array:")
                        print(self.main_arr[ind,ind2])
                    elif main_arr.ndim==3:
                        dep=int(input("Enter Layer Number :"))
                        ind=int(input("Enter a Row Number : "))
                        ind2=int(input("Enter a Column Number :"))
                        print("Indexed Array:")
                        print(self.main_arr[dep,ind,ind2])


                elif cho==2:
                    row_range=input("Enter the Row Range (start:end) : ")
                    col_range=input("Enter the Column Range (start:end) : ")
                    r_start, r_end = map(int, row_range.split(":"))
                    c_start, c_end = map(int, col_range.split(":"))
                    
                    print("Sliced Array: ")
                    print(self.main_arr[r_start:r_end,c_start:c_end])
                elif cho==3:
                    print("Going Back to Main Menu....")
                    break
                
            
        except:
            print("There Was An Error in  Slicing!")
            



    def math_op(self,main_arr):

        try:
        
            print()
            print("="*10)
            print("Choose a Mathematical Operation ")
            print("="*10)
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Divison")

            choice=int(input("Enter Your Choice :"))

            if choice==1:
                same=input(f"Enter the Same Size Array Elements ({self.main_arr.size} Elements Separated by Space): ").split()
                sec_arr=list(map(int,same))
                sec_arr=np.array(sec_arr).reshape(self.main_arr.shape)



                print("Original Array:")
                print(self.main_arr)
                print()
                print("Second Array:")
                print(sec_arr)
                print()
                print("Result of Addition:")
                print(self.main_arr+sec_arr)
            
            elif choice==2:
                same_sized=input(f"Enter the Same Size Array Elements ({self.main_arr.size} Elements Separated by Space): ").split()
                sec_arr=list(map(int,same_sized))
                sec_arr=np.array(sec_arr).reshape(self.main_arr.shape)

                print("Original Array:")
                print(self.main_arr)
                print()
                print("Second Array:")
                print(sec_arr)
                print()
                print("Result of Subtraction:")
                print(self.main_arr-sec_arr)
                
            elif choice==3:
                same=input(f"Enter the Same Size Array Elements ({self.main_arr.size} Elements Separated by Space): ").split()
                sec_arr=list(map(int,same))
                sec_arr=np.array(sec_arr).reshape(self.main_arr.shape)

                print("Original Array:")
                print(self.main_arr)
                print()
                print("Second Array:")
                print(sec_arr)
                print()
                print("Result of Multiplication:")
                print(self.main_arr*sec_arr)
            elif choice==4:
                same=input(f"Enter the Same Size Array Elements ({self.main_arr.size} Elements Separated by Space): ").split()
                sec_arr=list(map(int,same))
                sec_arr=np.array(sec_arr).reshape(self.main_arr.shape)

                print("Original Array:")
                print(self.main_arr)
                print()
                print("Second Array:")
                print(sec_arr)
                print()
                print("Result of Divison:")
                print(self.main_arr/sec_arr)
            else:
                print("Invalid Choice!")
        except:
            print("There was an Error in  a Mathematcal Operation")
             
             
             
             
             
    def combine_arr(self,main_arr):
        try:
            print()
            print("Choose an Option ")
            print("1. Combine Array ")
            print("2. Split Array ")
            choice=int(input("Enter your Choice : "))
            if choice==1:
                
                com=input(f"Enter the Elements of Another Array ({self.main_arr.size} Elements Separated by Space): ").split()
                spi_arr=list(map(int,com))
                spi_arr=np.array(spi_arr).reshape(self.main_arr.shape)

                print("Original Array:")
                print(self.main_arr)
                print()
                print("Second Array:")
                print(spi_arr)
                print()
                print("Combine Array (Vertical Stack):")
                new=np.vstack((self.main_arr,spi_arr))
                print(new)
            elif choice==2:
                print()
                split_arr=int(input("Enter the number of Splits : "))
                split_arr2=np.array_split(self.main_arr,split_arr)
                print()
                print("Original Array:")
                print(self.main_arr)
                print()
                print("Splited Array :")
                print(split_arr2)

            else:
                print("Invalid Choice !")
        except:
            print("Something Went Wrong !! ")
   
   
   
   
   
    def search_arr(self,main_arr):
        try:
            print()
            print("Choose an Option:")
            print("1. Search a Value ")
            print("2. Sort the Array ")
            print("3. Filter Values ")

            choice=int(input("Enter your Choice : "))

            if choice==1:
                print("Orignal Array : ")
                print(self.main_arr)
                search=int(input("Enter a Value You want to Search :"))
            
                if search in self.main_arr:
                    print("Value Founded At Index Number :")
                    p=np.argwhere(self.main_arr==search)
                    print(p)
                else:
                    print("Value does not exist!")
            elif choice ==2:
                    print()
                    print("Original Array")
                    print(self.main_arr)
                    print("Sorted Array ")
                    print(sorted(self.main_arr))


            elif choice ==3:
                print()
                print("Choose an Option ")
                print("1. Values Less-Than")
                print("2. Values Greater-Than")
                option=int(input("Enter Your Choice :-"))
                if option == 1 :
                    print()
                    less_arr=int(input("Enter a Value :"))
                    print("Original Array")
                    print(self.main_arr)
                    print("Filtered Array")
                    print(self.main_arr[self.main_arr<less_arr])
                elif option==2:
                    print()
                    greater_arr=int(input("Enter a Value :"))
                    print("Original Array")
                    print(self.main_arr)
                    print("Filtered Array")
                    print(self.main_arr[self.main_arr>greater_arr])
        except:
            print("There was an Error in Searching or Spliting array")

    def agg_func(self,main_arr):
        try:
            print("="*10,"Aggregates and Statistics","="*10)
            print()
            print("Choose an Option :")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")

            option=int(input("Enter your Choice : "))
            if option ==1:
                print("Original Array :")
                print(self.main_arr)
                print("Sum Of  Original Array :")
                print(np.sum(self.main_arr))
            elif option==2:
                
                print("Original Array :")
                print(self.main_arr)
                print("Mean Of Original Array :")
                print(np.mean(self.main_arr))
            elif option==3:
                
                print("Original Array :")
                print(self.main_arr)
                print("Median Of Original Array :")
                print(np.median(self.main_arr))
            else:
                print("Invalid Choice !!")
        except:
            print("There Was an Error in Aggregration")

    def main_menu(self):
  
            print()
            print("="*20)
            print("Welcome to Numpy Analyzer !")
            print("="*20)
            print("Choose an Option :")
            print("1. Create a Numpy Array ")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays ")
            print("4. Search, Sort or Filter Arrays ")
            print("5. Compute Aggregates and Statistics ")
            print("6. Exit ")

    def Start_programe(self):
        while True :
            self.main_menu()

            choice = int(input("Enter Your Choice : "))

            if choice==1:
                self.main_arr=obj.create_arr()
                obj.indexing_slicing(self.main_arr)
            elif choice==2:
                obj.math_op(self.main_arr)
            elif choice==3:
                obj.combine_arr(self.main_arr)
            elif choice==4:
                obj.search_arr(self.main_arr)
            elif choice==5:
                obj.agg_func(self.main_arr)
            elif choice==6:
                print("Thank You for using Numpy Analyzer! Goodbye!")
                break
 
            else:
                print("Invalid Choice !!")

 




obj=DataAnalytics()
obj.Start_programe()

