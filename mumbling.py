''' 
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

'''

def accum(st):
    result_st = ''
    for i in st:
        st_index = int(st.index(i))
        part = i.lower() * (st_index+1)
        result_st += part.capitalize() + '-'
        
    return result_st[:-1]
        



print(accum("RqaEzty"))

