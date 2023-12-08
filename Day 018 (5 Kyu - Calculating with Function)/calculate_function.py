import math

def zero(num = "0+"): return math.floor(eval(str(num) + "0"))
def one(num = "0+"): return math.floor(eval(str(num) + "1"))
def two(num = "0+"): return math.floor(eval(str(num) + "2"))
def three(num = "0+"): return math.floor(eval(str(num) + "3"))
def four(num = "0+"): return math.floor(eval(str(num) + "4"))
def five(num = "0+"): return math.floor(eval(str(num) + "5"))
def six(num = "0+"): return math.floor(eval(str(num) + "6"))
def seven(num = "0+"): return math.floor(eval(str(num) + "7"))
def eight(num = "0+"): return math.floor(eval(str(num) + "8"))
def nine(num = "0+"): return math.floor(eval(str(num) + "9"))

def plus(num): return str(num) + "+"
def minus(num): return str(-num) + "+"
def times(num): return str(num) + "*"
def divided_by(num): return str(1/num) + "*"