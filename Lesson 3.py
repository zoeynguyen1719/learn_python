import re
import string
nstring=[] 
astring=["abc","bcd","bce"]
for x in astring:
    nstring.append(x.replace('bc','x'))
print(nstring)

tup=('bc','x')
def replace_substr(string_list, replacement):
    nstring = []
    for x in string_list:
        nstring.append(x.replace(replacement[0], replacement[1]))
    return nstring



replace_substr(["abc","bcd","bce"], ('c','x'))

"""
Bai hoc o day la chia tach code thanh tung function voi logic tach biet
(separation of concern)
Cac function xac dinh input, output va exceptions
input co the empty, output co the empty, exception co the ko bi raise.
Nhung logic giua cac function phai ro rang va tach biet
Cai nay phai tap, de sau nay viet code cho nguoi khac con doc.
good.
"""