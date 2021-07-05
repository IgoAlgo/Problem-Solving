def boost_dec2hex(number):
    notation = "0123456789ABCDEF"
    base = len(notation)
    q, r = divmod(number, base)
    n = notation[r]
    return boost_dec2hex(q)+n if q else n # str type


def boost_dec2bin(number): # input is int type
    ans =""
    while number:
        ans = str(number % 2) + ans
        number //= 2

    while len(ans) < 8:
        ans = "0" + ans

    return ans


def boost_bin2hex(number):
    ans = 0
    number = number[::-1]
    for i in range(len(number)):
        ans += (2**i)*int(number[i])
    return "0x" + boost_dec2hex(ans) #return str


def LD_cmd(register, target, origin):
    if target == origin : return "NOOP"
    real_cmd = "01" + register[target] + register[origin]
    return boost_bin2hex(real_cmd)

def LN_cnd(register, target, origin):
    bin_val = boost_dec2bin(int(origin))
    real_cmd = "00" + register[target] + "110" + bin_val
    return boost_bin2hex(real_cmd)


def solution(param0):
    if param0[0:2] not in ["LD", "LN"] or param0[2] != " " : 
        return "ERROR"
    elif "," not in param0: return "ERROR"
    # need to imple
    register = {"A": "111", "B": "000", "C": "001", "D": "010", "E": "011", "H": "100", "L": "101"}


    answer = ''
    cmd, r = param0.split()
    target, origin = r.split(",")
    if target not in register.keys(): return "ERROR"
    elif origin not in register.keys() and cmd == "LD": return "ERROR"

    if cmd == "LD":
        return LD_cmd(register, target, origin)

    elif cmd == "LN":
        return LN_cnd(register, target, origin)
