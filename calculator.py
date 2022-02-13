def is_an_int(x):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    for i in x:
        if not i in digits:
            return False
    return True


def main(userIO):
    question = userIO.input("Write a number or an expression: ")
    booleanquestion = is_an_int(question)

    if booleanquestion == True:
        userIO.print(question)

    else:
        userIO.print("Can't calculate yet")

class inputIO():
    def input(self,prompt):
        return input(prompt)

    def print(self,prompt):
        print(prompt)


if __name__ == "__main__":
    main(inputIO())