''' 
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

'''

def accum(st):
    for i in st:
        st_index = int(st.index(i))
        print(i.upper() * 1 + i.lower() * st_index, end='-')
        
        



accum("RqaEzty")

