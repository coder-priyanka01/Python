class Employee:
    company = "ITC"
    language = ""
    def show(self):
        print(f"The name of the company {self.company} and the language is {self.language}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee,Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()