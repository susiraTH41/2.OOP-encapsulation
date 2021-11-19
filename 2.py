class Calcu:


    def __init__(self, num1=0, num2=0,operator=""):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    
    def cal(self):
        try :
            if self.operator =="+":
                print('out : '+str(self.num1 + self.num2))
            elif self.operator =="-":
                print('out : '+str(self.num1 - self.num2))
            elif self.operator =="*":
                print('out : '+str(self.num1 * self.num2))
            elif self.operator =="/":
                print('out : '+str(self.num1 / self.num2))
        except:
            print("error")
        
    def getExp(self,exp) :
        try :
            if '+' in exp :
                self.operator = '+'
                exp = exp.split('+')
            elif '-' in exp :
                self.operator = '-'
                exp = exp.split('-')
            elif '*' in exp :
                self.operator = '*'
                exp = exp.split('*')
            elif '/' in exp :
                self.operator = '/'
                exp = exp.split('/')
            self.num1 = float(exp[0])
            self.num2 = float(exp[1])
        except:
            print("error type")

while 1 :
    cal = Calcu()
    exp = input("input : ")
    cal.getExp(exp)
    cal.cal()
    
