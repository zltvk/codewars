''' 
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

'''

def accum(st):
    multiplier = 1
    for i in st:
        print(i * multiplier, end='-')
        multiplier +=1
        



accum("abcd")

