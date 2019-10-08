class torres(object):

    def __init__(self):
        self.T_A = []
        self.T_B = []
        self.T_C = []

    def clavijas(self,n):
        i = 0
        while i <= n + 1:
            if i < n:
                disk = 2*i + 1
                spaces = n - (i)
                self.T_A.append((spaces * " ") + (disk * "#") + (spaces * " "))
                self.T_B.append(((n) * " ") + ("0") + ((n) * " "))
                self.T_C.append(((n) * " ") + ("0") + ((n) * " "))
            elif i == n:
                self.T_A.append((2*i + 1) * "_")
                self.T_B.append((2*i + 1) * "_")
                self.T_C.append((2*i + 1) * "_")

            elif i == n + 1:
                self.T_A.append(((n) * " ") + ("*") + ((n) * " "))
                self.T_B.append(((n) * " ") + (" ") + ((n) * " "))
                self.T_C.append(((n) * " ") + (" ") + ((n) * " "))

            i += 1

        return self.T_A,self.T_B,self.T_C
