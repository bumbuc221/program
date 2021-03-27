from pdb import set_trace
l=[]
def rezolutie(l):
    pas=[""]*len(l)
    i=0;j=0
    nou=[0]
    lungime=len(l)
    #set_trace()
    for id in range(len(l)):
        ok1=0
        if len(l[id])>1:
            for k1_ in range(len(l[id]) - 1):
                for k2_ in range(k1_ + 1, len(l[id])):
                    aux = str()
                    if l[id][k1_][0] == '¬' and l[id][k2_][0] != '¬':
                        aux = l[id][k1_]
                        aux = aux.replace("¬", "")
                        if aux == l[id][k2_]:
                            ok1 = 1
                            break
                    elif l[id][k1_][0] != '¬' and l[id][k2_][0] == '¬':
                        aux = l[id][k2_]
                        aux = aux.replace("¬", "")
                        if aux == l[id][k1_]:
                            ok1 = 1
                            break
                if ok1 != 0:
                    l.pop(id)
                    pas.pop(id)
                    break
    while i<lungime:
        j=i+1
        while j<lungime:
            ok=0
            for k1 in range(len(l[i])):
                h = 0
                h1 = 0
                for k2 in range(len(l[j])):
                    aux=str()
                    if l[i][k1][0]=='¬' and l[j][k2][0]!='¬':
                        aux=l[i][k1]
                        aux=aux.replace("¬","")
                        if aux==l[j][k2]:
                            pas.append([i,j,l[i],l[j]])
                            h=k1;h1=k2
                            ok=1
                            break
                    elif l[i][k1][0]!='¬' and l[j][k2][0]=='¬':
                        aux = l[j][k2]
                        aux = aux.replace("¬","")
                        if aux == l[i][k1]:
                            pas.append([i,j,l[i],l[j]])
                            h = k1
                            h1 = k2
                            ok = 1
                            break
                if ok!=0:
                    break
            if ok!=0:
                nou=[]
                for x in range(len(l[i])):
                    if x!=h:
                        nou.append(l[i][x])
                for y in range(len(l[j])):
                    if y!=h1:
                        nou.append(l[j][y])
                nou=set(nou)
                nou=list(nou)
                if len(nou) != 0:
                    p = 0
                    for z in l:
                        if (z == nou):
                            p = 1
                    if p == 1:
                        pas.pop()
                    else:
                        l.append(nou)
                        lungime += 1
                if len(nou)==0:
                    for ind in range(len(l)):
                        print(ind,")",l[ind],"        ",pas[ind])
                    print("Este nesatisfiabila din {} si {}".format(i,j))
                    return
            j+=1
        i+=1
    if len(l)==0:
        print("Este Valida!")
    else:
        for ind in range(len(l)):
            print(ind, ")", l[ind], "      ", pas[ind])
        print("Este satisfiabila")
sub=[['P','Q','¬R'],['¬P','R'],['P','¬Q','S'],['¬P','¬Q','¬R'],['P','¬S']]
rezolutie(sub)
