
class MyCalc:
    ans = 0

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def add(self, num1, num2):
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 + num2
        return self.ans

    def sub(self, num1, num2):
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 - num2
        return self.ans

    def mult(self, num1, num2):
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 * num2
        return self.ans

    def div(self, num1, num2):
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1 / num2
        return self.ans

    def sqrt(self,N):#dap44
        if self._as_number(N) < 0:
            print('Square root of negative number does not exist!')
            return
        else:
            sqrt = self._as_number(N)**0.5
            print('Square root of number {}: {}'.format(N,sqrt))
            return sqrt

    def square(self, n):#dap44
        if self._as_number(n) < 0:
            return
        else:
            return self._as_number(n) ** 2

    def mean(self, data):##dap44
        for l in data:
        n = [float(i) for i in l]

    m=sum(n)/len(n)
    return m

    def median(self, L):##dap44
        for l in nums:
        n = [float(i) for i in l]

    l=len(n)
    n.sort()
    half=int(l/2)
    if half % 2 != 0:
        m=n[half]
    else:
        left=n[half-1]
        right=n[half]
        m=(left+right)/2
    return m

    def mode(self, L):##dap44
        for l in nums:
        n = [float(i) for i in l]

    mode=max(n)
    return mode

    def variance(self, data):#dap44
        for l in nums:
        n = [float(i) for i in l]

    m=sum(n)/len(n)
    variance = sum([((x - m) ** 2) for x in n]) / len(n)
    return variance

    def std_dev(self, ls):#dap44
        for l in nums:
        n = [float(i) for i in l]

    m=sum(n)/len(n)
    variance = sum([((x - m) ** 2) for x in n]) / len(n)
    std=variance**0.5

    return std





if __name__ == '__main__':

    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    print(calc)
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                if "+" in iSTR:
                    nums = iSTR.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done before - check to hanlde negative values
                elif "/" in iSTR:
                    nums = iSTR.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

                elif "*" in iSTR or "x" in iSTR:
                    nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done last so negative numbers work
                elif "-" in iSTR:
                    nums = iSTR.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

                elif "smean" in iSTR:
                    print("Calculating mean")
                    nums = iSTR.split("smean")[1].strip("[").strip("]").split(",")
                    r = calc.smean(nums)
                    print("R is " + str(r))


                elif "median" in iSTR:
                    print("Calculating median")
                    nums = iSTR.split("median")[1].strip("[").strip("]").split(",")  # assumes a comma list of values for median
                    r = calc.median(nums)
                    print("R is " + str(r))

                elif "mode" in iSTR:
                    print("Calculating mode")
                    nums = iSTR.split("mode")[1].strip("[").strip("]").split(",")
                    r = calc.mode(nums)
                    print("R is " + str(r))

                elif "sstd_dev" in iSTR:
                    print("Calculating sstd_dev")
                    nums = iSTR.split("sstd_dev")[1].strip("[").strip("]").split(",")
                    r = calc.sstd_dev(nums)
                    print("R is " + str(r))

                elif "svariance" in iSTR:
                    print("Calculating svariance")
                    nums = iSTR.split("svariance")[1].strip("[").strip("]").split(",")
                    r = calc.svariance(nums)
                    print("R is " + str(r))
                elif "sqrt" in iSTR:
                    nums = iSTR.split("sqrt")[1].strip("[").strip("]")
                    r = calc.sqrt(nums)
                    print("R is " + str(r))
                elif "square" in iSTR:
                    nums = iSTR.split("square")[1].strip("[").strip("]")
                    r = calc.square(nums)
                    print("R is " + str(r))

                    # etc






    else:

        print("Good bye")


