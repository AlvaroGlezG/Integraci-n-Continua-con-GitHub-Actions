# import string
# from codecs import encode as _dont_use_this_


def rot13(str_in, shift):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(str_in)
    str_out = ""

    for i in range(n):
        c = str_in[i].upper()
        loc = alpha.find(c)
        newloc = (loc + shift) % 26
        str_out += alpha[newloc]

    return str_out
