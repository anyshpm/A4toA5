#!/usr/bin/env python3

def A4toA5(page_num:int):

    a4_page_num = int(page_num / 4 + 0.9)
    
    a5_side_num = a4_page_num * 4
    
    a = []
    b = []
    offset=1
    for i in range(1, a5_side_num + 1):
        if i <= a5_side_num / 2:
            if len(a) > len(b):
                b.insert(0,str(i))
            else:
                a.insert(0,str(i))
        else:
            if len(a) >= len(b):
                b.insert(offset, str(i))
                offset = offset + 1
            else:
                a.insert(offset - 2, str(i))
                offset = offset + 1
    
    return [a5_side_num, ",".join(b), ",".join(a)]
