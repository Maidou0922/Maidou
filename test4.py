def lowerToUpper():
    valueList = ["my name is paul,i am 11 years old. i like fencing and coding,i like play video game too.i like eat meat,but i do not like very fat meat.this is all of my information."]
    with open("./lower.txt") as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            valueList.append(line)
           
    with open("./lower.txt") as file:
        for str in valueList:
            file.write(str.upper())
            
if __name__ == "__main__":lowerToUpper
    
           
    
