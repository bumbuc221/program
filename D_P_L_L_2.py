from pdb import set_trace
l3=[]
sub=[['A','¬B'],['A','C'],['¬B','C'],['¬A','B'],['B','¬C'],['¬A','¬C']]
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
def split(l):
    global l1
    global l2
    l1=[]
    l2=[]
    literali=[]
    max=0;l_a=[];l_b=[]
    for i in l:
        for j in range(len(i)):
                literali.append(i[j])
    for i in literali:
        if literali.count(i) > max:
            aux_m = str()
            max = literali.count(i)
            aux_m = i
    l1.extend(l)
    l_a.append(aux_m)
    l1.append(l_a)
    l2.extend(l)
    if aux_m[0] == '¬':
        aux_m = aux_m.replace('¬', "")
        l_b.append(aux_m)
        l2.append(l_b)
    else:
        aux_m = '¬' + aux_m
        l_b.append(aux_m)
        l2.append(l_b)
def copiere(s):
    global l1 
    for i in s:
        l1.append(i)
def dpll(l):
    global l3
    global l2
    global l1
    ok1=1;ok2=1
    #set_trace()
    nesatisfiabilitate=0
    contor=0
    while (ok1==1 or ok2==1) and (len(l)!=0 and nesatisfiabilitate==0):
        un_lit=[]
        lit_pur=[]
        ram_s=[];ram_d=[]
        ok1=0;ok2=0
        un_lit=un_literal(l)
        print("-------",contor,"--------")
        print("Multimea clauze!")
        for ko in l:
            print(ko)
        if len(un_lit)!=0:
            ok1=1
            for lit in un_lit:
                print("---------1 lit({})".format(lit))
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
                                        nesatisfiabilitate=1
                                        l3.append(0)
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
                                        nesatisfiabilitate = 1
                                        l3.append(0)
                            i+=1
            print("Multimea Transformata:")
            if nesatisfiabilitate==1 and len(l)==1:
                print([[]])
            else:
                for i in l:
                    print(i)
            print("\n")
        if nesatisfiabilitate==0:
            lit_pur = literal_pur(l)
            if len(lit_pur) != 0:
                ok2 = 1
                for lit in lit_pur:
                    print("literal pur ({})".format(lit_pur()))
                    i = 0
                    while i < len(l):
                        if l[i].count(lit) != 0:
                            l.pop(i)
                        else:
                            i += 1
                print("Multimea Transformata:")
                for k in l:
                    print(k)
                print("\n")
    if len(l)==0:
        l3.append(-1)
    elif nesatisfiabilitate==0:
        print("SPLIT PE RAMURE")
        split(l)
        print("RAMURA 1:")
        for i in range(len(l2)):
            l2[i]=tuple(l2[i])
        dpll(l1)
        print("RAMURA 2:")
        for i in range(len(l2)):
            l2[i] = list(l2[i])
        dpll(l2)
l3=[]
dpll(sub)
ok=0
for i in l3:
    if i==-1:
        print("Este satisfiabila!")
        ok=1
        break
if ok==0:
    print("Este nesatisfiabila!")