def progress(corrida):
    dias = 0        
    b = corrida[0]
    for i in (corrida):
        if b < i:
            dias +=1
        b = i
    return dias
