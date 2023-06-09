import random
class cpf:
    def __init__(self):
        self.cpf_incom = []
        self.verificador = []
        self.reverso = 0
        self.res_som = 0
        self.f_cpf = ""

    def gen_nums(self) :
        for x in range(9):
            n = random.randint(0, 9)
            self.cpf_incom.append(n)

    def calc_ver(self):
        self.gen_nums()
        self.reverso = 10
        for i in self.cpf_incom:
            self.res_mult = i * self.reverso
            self.res_som += self.res_mult
            self.reverso = self.reverso - 1

        res_mod = self.res_som % 11

        if res_mod == 0 or res_mod == 1:
            self.verificador.append(0)
            self.cpf_incom.append(0)
        else :
            res_sub = 11 - res_mod
            self.verificador.append(res_sub)
            self.cpf_incom.append(res_sub)
        self.calc_ver2()
        
    def calc_ver2(self):
        self.reverso = 11
        for i in self.cpf_incom:
            self.res_mult = i * self.reverso
            self.res_som += self.res_mult
            self.reverso = self.reverso - 1

        res_mod = self.res_som % 11

        if res_mod == 0 or res_mod == 1:
            self.verificador.append(0)
            self.cpf_incom.append(0)
        else :
            res_sub = 11 - res_mod
            self.verificador.append(res_sub)
            self.cpf_incom.append(res_sub)
        self.forma()

    def forma(self):
        for i, num in enumerate(self.cpf_incom):
            if i % 3 == 0 and i != 0 and i != 9:
                self.f_cpf += "."         
            elif i == 9:
                self.f_cpf += "-"
            self.f_cpf += str(num)
        self.show()
    def show(self):
        print(self.f_cpf)

a = cpf()

a.calc_ver()
