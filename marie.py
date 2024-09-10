def bth(b):
        v = int(b, 2)
        hex_v = hex(v)[2:]
        return hex_v.upper()

def marie_i(c):
        if bth(c[0]) == "3": k = 'Add\n'

        elif bth(c[0]) ==  "B": k = 'AddI\n'

        elif bth(c[0]) == "4": k = "Sub\n"

        elif bth(c[0]) == "9": k = "Jump\n"

        elif bth(c[0]) == "C": k = "JumpI\n"

        elif bth(c[0]) == "1": k = "Load\n"

        elif bth(c[0]) == "D": k = "LoadI\n"

        elif bth(c[0]) == "2": k = "Store\n"

        elif bth(c[0]) == "E": k = "StoreI\n"

        elif bth(c[0]) == "8": k = "Skipcond\n"

        elif bth(c[0]) == "5": k = "Input\n"

        elif bth(c[0]) == "6": k = "Output\n"

        elif bth(c[0]) == "A": k = "Clear\n"

        elif bth(c[0]) == "0": k = "JnS\n"

        elif bth(c[0]) == "7": k = "Halt\n"

        return k

def marie_a(c):
        l = int(c[1], 2)
        if l == 0:
                x = ''

        else:
                x = f'{l}\n'

        return x

def main():
        s = 'Instruções:\n'
        f = 'Endereços acessados:\n'

        while True:
                c = input().split()
                if not c:
                        break
                s += marie_i(c)
                f += marie_a(c)

        print(f"{s}\n{f}")

main()
