

class Calculation(object):
    def getInput(self):
        inputtext = input("Enter numbers with arithmetic operator: ")
        if (eval(inputtext)) != None:
        	print(eval(inputtext))


calc = Calculation()
try:
	calc.getInput()
except:
	print("lololol")
	calc.getInput()