class dog():
    def __init__(self,breed,color,age):
        self.breed=breed
        self.color=color
        self.age=age
#模板
        print("The dog's breed is ",breed,",dog's color is ",color,",dog's age is ",age,".")
    def eat(self):
        print("The dog is eating")
    def sleep(self):
        print("The dog is sleeping")
    def bark(self):
        print("The dog is barking")

dog1=dog("labrador","yellow",7)
dog1.eat()
dog1.sleep()
dog1.bark()

dog2=dog("shepherd","white",10)
dog2.eat()
dog2.sleep()
dog2.bark()

dog3=dog("pug","brown",9)
dog3.eat()
dog3.sleep()
dog3.bark()

dog4=dog("dachshund","black",13)
dog4.eat()
dog4.sleep()
dog4.bark()
