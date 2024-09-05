class ManyFunctionsClass():
    def Subfields():
        list =["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("""Sub-fields in AI are:""")
        for i in list:
            print(i)

    def OddEven():
        num= int(input("Enter a number:"))
        if num%2==0:
            result= num, "is Even number"
            return result


    def Elegible():
        Gender = input("Your Gender:")
        Age = int(input("Your Age:"))
        if Gender=="Male" and Age<=21:
            print("Your Gender:",Gender)
            print("your age is:",Age,",SO NOT ELIGIBLE")
        elif Gender=="Female" and Age<=18:
            print("Your Gender:",Gender)
            print("your age is:",Age,",SO NOT ELIGIBLE")

    def percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        Total=(Subject1+Subject2+Subject3+Subject4+Subject5)
        percentage =(Subject1+Subject2+Subject3+Subject4+Subject5)/5
        result1 = "Total : ",Total
        result2 ="percentage : ",percentage
        return result1,result2

    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        Area_of_Triangle =  (Height*Breadth)/2
        print("Area of Triangle:",Area_of_Triangle)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth1 = int(input("Breadth1:"))
        Perimeter_of_Triangle = Height1+Height2+Breadth1
        print("Perimeter of Triangle:",Perimeter_of_Triangle)

    
    