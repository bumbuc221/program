from pdb import set_trace
afirma=0
def literal_pur(l):
    poz=[];neg=[]
    lit_pur=[]
    total=[]
    for i in l:
        for j in i:
            if total.count(j)==0:
                total.append(j)
    for i in total:
        if i.count("¬")!=0:
            neg.append(i)
        else:
            poz.append(i)
    for i in poz:
        aux=str()
        aux="¬"+i
        if neg.count(aux)==0:
            lit_pur.append(i)
    for i in neg:
        aux=str()
        aux=i.replace("¬","")
        if poz.count(aux)==0:
            lit_pur.append(i)
    return lit_pur
def un_literal(l):
    un_lit=[]
    for i in l:
        if len(i)==1:
            un_lit.extend(i)
    return un_lit
from pdb import set_trace
l=[]
def rezolutie(l):
    pas=[""]*len(l)
    i=0;j=0
    nou=[0]
    global afirma
    lungime=len(l)
    #set_trace()
    l3=[]
    l3.extend(l)
    for g in range(len(l3)):
        l4=[]
        for jk in range(len(l3[g])):
            aux = str()
            aux = l3[g][jk]
            if aux.count('¬') != 0:
                aux = aux.replace("¬", "")
            l4.append(aux)
        poz = 0
        if len(l4)>1:
            for inc in range(len(l4) - 1):
                for incc in range(inc + 1, len(l4)):
                    if l4[inc] == l4[incc]:
                        poz = 1
                        break
                if poz == 1:
                    break
            if poz == 1:
                l.pop(g)
                pas.pop(g)
    afirma=0
    while i<lungime and afirma==0:
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
                            pas.append([i,j])
                            h=k1;h1=k2
                            ok=1
                            break
                    elif l[i][k1][0]!='¬' and l[j][k2][0]=='¬':
                        aux = l[j][k2]
                        aux = aux.replace("¬","")
                        if aux == l[i][k1]:
                            pas.append([i,j])
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
                poz=0
                if len(nou) > 1:
                    nou_2=[]
                    for jk in range(len(nou)):
                        aux = str()
                        aux = nou[jk]
                        if aux.count('¬') != 0:
                            aux = aux.replace("¬", "")
                        nou_2.append(aux)
                    for inc in range(len(nou_2) - 1):
                        for incc in range(inc + 1, len(nou_2)):
                            if nou_2[inc] == nou_2[incc]:
                                poz = 1
                                break
                        if poz == 1:
                            break
                if len(nou)!=0 and poz==0:
                    p = 0
                    for z in range(len(l)):
                        if len(l[z]) == len(nou):
                            p = 1
                            for pp in range(len(nou)):
                                if l[z].count(nou[pp]) == 0:
                                    p = 0
                            if p == 1:
                                break
                    if p == 1:
                        pas.pop()
                    else:
                        l.append(nou)
                        afirma=1
                        lungime += 1
                else:
                    pas.pop()
            j+=1
        i+=1
def davis_putnam(l):
    un_lit=[]
    lit_pur=[]
    ok1=1;ok2=1
    global afirma
    contor=1
    permis=1
    h=0;s=0
    while permis==1:
        un_lit=[]
        lit_pur=[]
        ok1=0;ok2=0
        #set_trace()
        un_lit=un_literal(l)
        print("-------",contor,"--------")
        print("Multimea caluze")
        print(l)
        print("Multimea literali singular:    ",un_lit)
        if len(un_lit)!=0:
            ok1=1
            for lit in un_lit:
                if lit[0]=='¬':
                    s=0
                    while s<len(l):
                        if l[s].count(lit)!=0:
                            l.pop(s)
                        else:
                            aux = str()
                            aux = lit
                            aux = aux.replace('¬', "")
                            if l[s].count(aux)!=0:
                                h=-1
                                for k in range(len(l[s])):
                                    if l[s][k]==aux:
                                        h=k
                                if h!=-1:
                                    l[s].pop(h)
                                    if len(l[s])==0:
                                        print("Este nesatisfiabila!")
                                        return
                            s+=1
                else:
                    i=0
                    while i<len(l):
                        if l[i].count(lit)!=0:
                            l.pop(i)
                        else:
                            aux=str()
                            aux ='¬'+lit
                            if l[i].count(aux)!=0:
                                h=-1
                                for k in range(len(l[i])):
                                    if l[i][k] == aux:
                                        h = k
                                if h != -1:
                                    clauza=l[i]
                                    l[i].pop(h)
                                    if len(l[i]) == 0:
                                        print("Este nesatisfiabila!")
                                        return
                            i+=1
        if ok1!=0:
            print("\n")
            print("Multimea clauze tarnsformate:")
            for i in l:
                print(i)
        lit_pur=literal_pur(l)
        print("Literalii puri:",lit_pur)
        if len(lit_pur)!=0:
            ok2=1
            for lit in lit_pur:
                i=0
                while i<len(l):
                    if l[i].count(lit)!=0:
                        l.pop(i)
                    else:
                        i+=1
        if ok2!=0:
            print("Multimea clauze tarnsformate:")
            for i in l:
                print(i)
        if ok1==0 and ok2==0 and len(l)>0:
            rezolutie(l)
            if afirma==0:
                permis=0
        contor+=1
    if len(l)==0:
        print("Este Valida!")
    else:
        print("Este satisfiabila!")
sub=[['A','¬B','C'],['B','C'],['¬A','C'],['B','¬C'],['¬B']]
davis_putnam(sub)

