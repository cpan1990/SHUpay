#checks for numerical values

def quantity(q_str):
    i = 0
    while i < len(str(q_str)):
        c = (str(q_str))
                
        if (c in range (0, 47) or c in range(58, 255)) and c != 46:
            print ("Whole Numbers Only")
            break
                
        else:
            i = i + 1
            
    if i == len(str(q_str)):
        qty = float (q_str)
        if qty != int(qty) or qty <= 0:
            print ("Please try valid quantity")

