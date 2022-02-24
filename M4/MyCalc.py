class Calculator:
    ans = 0

    @staticmethod
    def _is_float(val):
        try:
            val = float(val)
            return True
        except:
            return False

    @staticmethod
    def _is_int(val):
        try:
            val = int(val)
            return True
        except:
            return False

    @staticmethod
    def _as_number(val):
        if Calculator._is_int(val):
            return int(val)
        elif Calculator._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    # UCID: dap44 Date: 2/20/2022

    def calc(self, num1: object, num2: object, operator: object) -> object:
        if num1 == "ans":
            return self.calc(self.ans, num2, operator)
        num1 = Calculator._as_number(num1)
        num2 = Calculator._as_number(num2)

        if operator == "+":
            self.ans = num1+num2
        elif operator == "/":
            self.ans = num1/num2
        elif operator == "-":
            self.ans = num1-num2
        elif operator == "*":
            self.ans = num1*num2
        return self.ans

if __name__ == '__main__':
    is_running = True
    status = input("Are you ready?")
    calc = Calculator()
    print(calc)
    if status == "yes":
        while is_running:
            equation = input("What is your eq:")
            if equation == "quit" or equation == "q":
                is_running = False
                print("Thank you,Good bye")
            else:
                print("Your equation was " + str(equation))
                ops = ["+", "/", "*","-"]
                for op in ops:
                    if op in equation:
                        nums = equation.split(op)
                        result = calc.calc(nums[0].strip(), nums[1].strip(), op)
                        print("Your result is " + str(result))





    else:
        print("Thank you,Good bye")
        is_running = False
