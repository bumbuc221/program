from pdb import set_trace
import csv
a = []
def conectorii():
    print("𝐍𝐄𝐆𝐀𝐓𝐈𝐀:",'¬ ',"sau"," ","!")
    print("𝐃𝐈𝐒𝐉𝐔𝐍𝐂𝐓𝐈𝐀:",'∨ ',"sau"," ","|")
    print("𝐂𝐎𝐍𝐉𝐔𝐍𝐂𝐓𝐈𝐀:",'∧ ',"sau"," ","&")
    print("𝐈𝐌𝐏𝐋𝐈𝐂𝐀𝐓𝐈𝐀:",'⇒ ',"sau"," ",">")
    print("𝐄𝐂𝐇𝐈𝐕𝐀𝐋𝐄𝐍𝐓𝐀:",'⇔ ',"sau"," ","=")
    print("𝐈𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐞𝐭𝐢 𝐟𝐨𝐫𝐦𝐮𝐥𝐚:")
def interpretari(x):
    global a
    for i in range(2 ** x):
        l = [0] * x
        j = len(l) - 1
        k = i
        while k != 0:       #crearea interpretarilor
            l[j] = k % 2
            k //= 2
            j = j - 1
        a.append(l)
from pdb import set_trace
rezultat = 0
def negatie(a):
    global rezultat
    rezultat = 1 - a
def conjunctie(a, b):
    global rezultat
    if a + b <= 1:
        rezultat = 0
    else:                #functii pentru calcularea interpretarilor
        rezultat = 1
def dijunctie(a, b):
    global rezultat
    if a + b == 0:
        rezultat = 0
    else:
        rezultat = 1
def implicatie(a, b):
    global rezultat
    if a == 1 and b == 0:
        rezultat = 0
    else:
        rezultat = 1
def echivalenta(a, b):
    global rezultat
    if a == b:
        rezultat = 1
    else:
        rezultat = 0
def tabel(ss):
    global rezultat
    oko=ss.split(" ")
    ss=str()
    for i in oko:        #scotem spatiile in caz ca are
        ss+=i
    k = 0
    q = 0
    formule = []
    nr = 0
    R = []
    con = ['¬','∧','∨','⇒','⇔']
    coloana_valori = []
    conector = str()
    prima_propozitie = str()
    a_doua_propozitie = str()
    propozitii = []
    for i in range(len(ss)):
        if con.count(ss[i]) == 0 and ss[i] != '(' and ss[i] != ')':
            if propozitii.count(ss[i]) == 0:
                propozitii.append(ss[i])   #scoatem variabilele pt a le altura interpretari
    # print(propozitii)
    interpretari(len(propozitii))
    for valori in a:
        s = ss
        for i in range(len(s)):
            if propozitii.count(s[i]) != 0: #inlocuirea variabilelor cu interpretari
                kk = str(valori[propozitii.index(s[i])])
                s = s.replace(s[i], kk)
        afirma=1
        #set_trace()
        while afirma!=0 and len(s)>1:
            t = str()
            afirma=0
            for i in range(len(s)):
                if s[i] == '(':      #gaseste ultima paranteza deschisa
                    k = i
                    afirma=1
            for i in range(k, len(s)):
                if s[i] == ')':
                    q = i            #prima paranteza inchisa dupa prima deschisa
                    afirma=1
                    break
            if afirma!=0:        #in cauzul in care are paranteze se ia dupa ordinea parantezelor
                nr_conectori=0
                for i in range(k,q):
                    if con.count(s[i])!=0:
                        nr_conectori+=1       #se contorizeaza cati conectori
                if nr_conectori>1:
                    for conector_leg in con: #calculeaza valoarea pana ajunge la un singur conector
                        da=0
                        da=s.count(conector_leg,k,q)
                        if da>0:
                            while da>0 and nr_conectori>1:
                                for o in range(k,q):
                                    if s[o] == conector_leg:
                                        pozitie = o
                                if s[pozitie] != '¬':           #pozitiile variabilelor fata de conectori
                                    a_doua_propozitie = s[pozitie + 1]
                                    prima_propozitie = s[pozitie - 1]
                                    conector = s[pozitie]
                                else:
                                    conector = "¬"
                                    prima_propozitie = s[pozitie + 1]
                                if conector == '∧':
                                    conjunctie(int(prima_propozitie), int(a_doua_propozitie))
                                elif conector == '∨':
                                    dijunctie(int(prima_propozitie), int(a_doua_propozitie))
                                elif conector == '⇒':
                                    implicatie(int(prima_propozitie), int(a_doua_propozitie))
                                elif conector == '⇔':
                                    echivalenta(int(prima_propozitie), int(a_doua_propozitie))
                                elif conector == '¬':
                                    negatie(int(prima_propozitie))
                                i = 0
                                ok = 0
                                tt=str()
                                if conector == '¬': #dupa ce s-a calculat valoarea inlocuim cele doua
                                    q = pozitie    #variabile si conecotul cu valoarea calculata
                                else:
                                    q = pozitie - 1
                                while i < len(s):
                                    if i < q or i > pozitie + 1:
                                        tt += s[i]
                                    else:
                                        if ok == 0:
                                            if rezultat != 0:#inlocuirea
                                                tt += '1'
                                            else:
                                                tt += '0'
                                            ok = 1
                                    i += 1
                                s = str()
                                for i in range(len(tt)):
                                    s += tt[i]
                                for i in range(len(s)):#verificarea daca a mai rams paranteze
                                    if s[i] == '(':
                                        k = i
                                        afirma = 1
                                for i in range(k, len(s)):
                                    if s[i] == ')':
                                        q = i
                                        afirma = 1
                                        break
                                da=da-1
                                nr_conectori=nr_conectori-1 #scaderea nr de conectori
                            if nr_conectori==1:
                                break
            for i in range(len(s)):
                if s[i] == '(':
                    k = i
                    afirma=1
            for i in range(k, len(s)): #se verifica dupa ce termina conecotrii daca
                if s[i] == ')':        #se mai gasesc paranteze
                    q = i
                    afirma=1
                    break
            if afirma!=0:     #daca intr o paranteza a ramas doar doua variabile si
                if nr == 0:   #un conector se efectueaza calculul valori dintre cele doua
                    nou = str()
                    for i in range(k, q + 1):
                        nou += ss[i]
                    formule.append(nou)
                if s[k + 1] != '¬':
                    a_doua_propozitie = s[q - 1]
                    prima_propozitie = s[k + 1]
                    for i in range(k, q):
                        if con.count(s[i]) != 0:
                            conector = s[i]
                            break
                else:
                    conector = "¬"
                    prima_propozitie = s[k + 2]
                # set_trace()
                if conector == '∧':
                    if prima_propozitie=='1':
                        a1=1
                    else:
                        a1=0
                    if a_doua_propozitie=='1':
                        b1=1
                    else:
                        b1=0
                    conjunctie(a1,b1)
                elif conector == '∨':
                    if prima_propozitie=='1':
                        a1=1
                    else:
                        a1=0
                    if a_doua_propozitie=='1':
                        b1=1
                    else:
                        b1=0
                    dijunctie(a1,b1)
                elif conector == '⇒':
                    if prima_propozitie=='1':
                        a1=1
                    else:
                        a1=0
                    if a_doua_propozitie=='1':
                        b1=1
                    else:
                        b1=0
                    implicatie(a1,b1)
                elif conector == '⇔':
                    if prima_propozitie=='1':
                        a1=1
                    else:
                        a1=0
                    if a_doua_propozitie=='1':
                        b1=1
                    else:
                        b1=0
                    echivalenta(a1,b1)
                elif conector == '¬':
                    if prima_propozitie=='1':
                        a1=1
                    else:
                        a1=0
                    negatie(a1)
                i = 0
                ok = 0
                while i < len(s):
                    if i < k or i > q:
                        t += s[i]
                    else:
                        if ok == 0:
                            if  rezultat!= 0:
                                t += '1'
                            else:
                                t += '0'
                            ok = 1
                    i += 1
                s = str()
                for i in range(len(t)):
                    s += t[i]
        #set_trace()
        if len(s)>1:   #daca nu mai avem paranteze lucram dupa puterea conectorilor
            for conector_leg in con:
                if len(s)>1:
                    da = 0
                    da = s.count(conector_leg)
                    tt = str()
                    if da != 0:
                        for nm in range(da):
                            for o in range(len(s)):
                                if s[o] == conector_leg:
                                    pozitie = o
                            if s[pozitie] != '¬':
                                a_doua_propozitie = s[pozitie + 1]
                                prima_propozitie = s[pozitie - 1]
                                conector = s[pozitie]
                            else:
                                conector = "¬"
                                prima_propozitie = s[pozitie + 1]
                            if conector == '∧':
                                conjunctie(int(prima_propozitie), int(a_doua_propozitie))
                            elif conector == '∨':
                                dijunctie(int(prima_propozitie), int(a_doua_propozitie))
                            elif conector == '⇒':
                                implicatie(int(prima_propozitie), int(a_doua_propozitie))
                            elif conector == '⇔':
                                echivalenta(int(prima_propozitie), int(a_doua_propozitie))
                            elif conector == '¬':
                                negatie(int(prima_propozitie))
                            i = 0
                            ok = 0
                            tt=str()
                            if conector == '¬':
                                q = pozitie
                            else:
                                q = pozitie - 1
                            while i < len(s):
                                if i < q or i > pozitie + 1:
                                    tt += s[i]
                                else:
                                    if ok == 0:
                                        if rezultat != 0:
                                            tt += '1'
                                        else:
                                            tt += '0'
                                        ok = 1
                                i += 1
                            s = str()
                            for i in range(len(tt)):
                                s += tt[i]
                else:
                    break
        nr = 1
        coloana_valori.append(int(s))
    linia_1 = []
    for i in propozitii:
        linia_1.append(i)  #copierea de variabile si formula pt a aseza in tabel
    linia_1.append(ss)
    L = []
    # print(e, " ", ss)
    for i in range(len(a)):
        lux = []
        for j in a[i]:
            lux.append(j)
        lux.append(coloana_valori[i]) #copierea tuturor combinatiilor
        L.append(lux)
    with open("tabel2.csv", "w", encoding="utf-8") as csv_f:
        f = csv.writer(csv_f)
        f.writerow(linia_1) #afisarea in csv
        f.writerows(L)
    FND = str()
    ok2 = 0
    FNC=str()
    #set_trace()
    lista1=[]
    for i in range(len(coloana_valori)): #FND
        if coloana_valori[i] == 1:
            ok3 = 0  #preluarea tuturor combinatiilor si
            lista1.append(i+2)
            if ok2 == 0:        #transformarea in FNC SI FND
                FND += '('
                for j in range(len(a[i])):
                    if a[i][j] == 0:   #in functie dupa valoarea care s a calculat
                        if ok3 == 0:
                            FND += '¬' + propozitii[j]
                            ok3 = 1
                        else:
                            FND += '∧' + '¬' + propozitii[j]
                    else:
                        if ok3 == 0:
                            FND += propozitii[j]
                            ok3 = 1
                        else:
                            FND += '∧' + propozitii[j]
                FND += ')'
                ok2=1
            else:
                FND += '∨'
                FND += '('
                ok3 = 0
                for j in range(len(a[i])):
                    if a[i][j] == 0:
                        if ok3 == 0:
                            FND += '¬' + propozitii[j]
                            ok3 = 1
                        else:
                            FND += '∧' + '¬' + propozitii[j]
                    else:
                        if ok3 == 0:
                            FND += propozitii[j]
                            ok3 = 1
                        else:
                            FND += '∧' + propozitii[j]
                FND += ')'
    ok2=0
    clauze=[]
    m_c=[]
    lista2=[]
    for i in range(len(coloana_valori)): #FNC
        if coloana_valori[i] == 0:
            ok3 = 0
            lista2.append(i+2)
            if ok2 == 0:
                FNC += '('
                m_c=[]
                for j in range(len(a[i])):
                    if a[i][j] == 0:
                        if ok3 == 0:
                            m_c.append(propozitii[j])
                            FNC +=propozitii[j]
                            ok3 = 1
                        else:
                            m_c.append(propozitii[j])
                            FNC +='∨'+ propozitii[j]
                    else:
                        if ok3 == 0:
                            m_c.append('¬'+propozitii[j])
                            FNC +='¬'+propozitii[j]
                            ok3 = 1
                        else:
                            m_c.append('¬' + propozitii[j])
                            FNC += '∨'+'¬'+ propozitii[j]
                FNC += ')'
                ok2=1
                clauze.append(m_c)
            else:
                m_c=[]
                FNC += '∧'
                FNC += '('
                ok3 = 0
                for j in range(len(a[i])):
                    if a[i][j] == 0:
                        if ok3 == 0:
                            m_c.append(propozitii[j])
                            FNC +=propozitii[j]
                            ok3 = 1
                        else:
                            m_c.append(propozitii[j])
                            FNC += '∨'+ propozitii[j]
                    else:
                        if ok3 == 0:
                            m_c.append('¬'+propozitii[j])
                            FNC +='¬'+propozitii[j]
                            ok3 = 1
                        else:
                            m_c.append('¬' + propozitii[j])
                            FNC +='∨'+'¬'+propozitii[j]
                clauze.append(m_c)   #caluleaza clauzele
                FNC += ')'
    if len(FND)==0:
        print("1.")
        print("𝐅𝐨𝐫𝐦𝐚 𝐧𝐨𝐫𝐦𝐚𝐥 𝐝𝐢s𝐣𝐮𝐧𝐜𝐭𝐢𝐯𝐚:",'⊥')
        print("_______________________________________________________________________________________________________________________________________________________________________")
    else:
        print("1.")
        print("𝐅𝐨𝐫𝐦𝐚 𝐧𝐨𝐫𝐦𝐚𝐥 𝐝𝐢s𝐣𝐮𝐧𝐜𝐭𝐢𝐯𝐚:", FND)
        print("𝐒𝐞 𝐟𝐨𝐫𝐦𝐞𝐚𝐳𝐚 𝐝𝐢𝐧 𝐮𝐫𝐦𝐚𝐭𝐨𝐫𝐚𝐫𝐞𝐥𝐞 𝐥𝐢𝐧𝐢𝐢 𝐝𝐢𝐧 𝐭𝐚𝐛𝐞𝐥:")
        print(lista1)
        print("_______________________________________________________________________________________________________________________________________________________________________")
        print("\n")
    if len(FNC)==0:
        print("2.")
        print("𝐅𝐨𝐫𝐦𝐚 𝐧𝐨𝐫𝐦𝐚𝐥 𝐜𝐨𝐧𝐣𝐮𝐧𝐜𝐭𝐢𝐯𝐚:",'⊤')
        print("_______________________________________________________________________________________________________________________________________________________________________")
        print("𝐌𝐮𝐥𝐭𝐢𝐦𝐞𝐚 𝐝𝐞 𝐜𝐥𝐚𝐮𝐳𝐞:",'⊤')
    else:
        print("2.")
        print("𝐅𝐨𝐫𝐦𝐚 𝐧𝐨𝐫𝐦𝐚𝐥 𝐜𝐨𝐧𝐣𝐮𝐧𝐜𝐭𝐢𝐯𝐚:",FNC)
        print("𝐒𝐞 𝐟𝐨𝐫𝐦𝐞𝐚𝐳𝐚 𝐝𝐢𝐧 𝐮𝐫𝐦𝐚𝐭𝐨𝐫𝐚𝐫𝐞𝐥𝐞 𝐥𝐢𝐧𝐢𝐢 𝐝𝐢𝐧 𝐭𝐚𝐛𝐞𝐥:")
        print(lista2)
        print("\n")
        print("_______________________________________________________________________________________________________________________________________________________________________")
        print("3.")
        print("𝐌𝐮𝐥𝐭𝐢𝐦𝐞𝐚 𝐝𝐞 𝐜𝐥𝐚𝐮𝐳𝐞:",clauze)
l1=[]
l2=[]
l3=[]
def literal_pur(l):
    poz=[];neg=[]
    lit_pur=[]
    total=[]
    for i in l:
        for j in i:
            if total.count(j)==0: #memoreaza literarii ramasi
                total.append(j)
    for i in total:
        if i.count("¬")!=0:
            neg.append(i)    #verifica daca careva ii pur
        else:
            poz.append(i)
    for i in poz:
        aux=str()
        aux="¬"+i
        if neg.count(aux)==0:   #in cazul care a gasit returneaza literalul pur
            lit_pur.append(i)   #si creaza literalul complementar
    for i in neg:
        aux=str()
        aux=i.replace("¬","") #in cazul care a gasit returneaza literalul pur
        if poz.count(aux)==0: #si creaza literalul complementar
            lit_pur.append(i)
    return lit_pur
def un_literal(l):
    un_lit=[]
    for i in l:
        if len(i)==1:
            un_lit.extend(i) #verificare pt un singur literal
    return un_lit
global ramura
ramura=0
l2=[]
def split(l): #impartirea pe ramuri
    global l1
    global l2
    global ramura
    l1=[]
    l2.append([])
    literali=[]
    max=0
    la=[]
    lb=[]
    for i in l:
        for j in range(len(i)):
                literali.append(i[j]) #calculeaza maximul aparitiilor unui literal
    auxm = str()
    for i in literali:
        if literali.count(i) > max: #crearea celor doua ramuri
            auxm = str()
            max = literali.count(i)
            auxm = i
    l1=l.copy()
    l2[ramura]=l1.copy()
    la.append(auxm)
    l1.append(la)
    if auxm[0]=='¬':         #literal fara negatie
        auxm=auxm.replace('¬',"")
        lb.append(auxm)
        l2[ramura].append(lb)
    else:
        auxm='¬'+auxm       #literal cu negatie
        lb.append(auxm)
        l2[ramura].append(lb)
global nnn
def rezolutie(l):
    global nnn
    pas=[""]*len(l)
    nnn=[]
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
            l4.append(aux)              #se verifica la inceput daca nu contine clauze triviale
        poz = 0
        if len(l4)>1:
            for inc in range(len(l4) - 1):
                for incc in range(inc + 1, len(l4)):
                    if l4[inc] == l4[incc]:
                        poz = 1         #se elimina clauzele  triviale daca sunt
                        break
                if poz == 1:
                    break
            if poz == 1:
                l.pop(g)
                pas.pop(g)
    afirma=0
    while i<lungime and afirma==0:
        j=i+1
        while j<lungime and afirma==0: #facem combinatiile clauza i cu toate clauzele de pe poz i+1->n
            ok=0
            for k1 in range(len(l[i])):
                h = 0
                h1 = 0
                for k2 in range(len(l[j])):
                    aux=str()
                    if l[i][k1][0]=='¬' and l[j][k2][0]!='¬':
                        aux=l[i][k1]
                        aux=aux.replace("¬","")   #verificrea de literali complementari
                        if aux==l[j][k2]:
                            pas.append([i,j])
                            h=k1;h1=k2
                            ok=1
                            break
                    elif l[i][k1][0]!='¬' and l[j][k2][0]=='¬':
                        aux = l[j][k2]
                        aux = aux.replace("¬","")
                        if aux == l[i][k1]:        #verificrea de literali complementari
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
                        nou.append(l[i][x]) #se memoreaza clauza rezultata
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
                        nou_2.append(aux)               #se verifica daca nu se afla in multime
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
                    if p == 1:         #in cazul in care nu se afla o stregem
                        pas.pop()      #si pasi ii stergem altfel se adauga la multime
                    else:
                        l.append(nou)
                        nnn.append(pas.pop())
                        afirma=1
                        lungime += 1
                else:
                    pas.pop()
            j+=1
        i+=1
global parc_r
global hatz
hatz=0
parc_r=0
def dpll(l):
    global l3
    global l2
    global l1
    global parc_r
    global ramura
    global hatz
    ok1=1;ok2=1
    #set_trace()
    nesatisfiabilitate=0
    contor=0
    if hatz==0:
        for i in l3:
            if i==-1:
                hatz=1
                break
    while (ok1==1 or ok2==1) and (len(l)!=0 and nesatisfiabilitate==0):
        un_lit=[]
        lit_pur=[]
        ram_s=[];ram_d=[]
        ok1=0;ok2=0
        un_lit=un_literal(l)
        if hatz == 0:
            print("-------",contor,"--------")
            print("𝐌𝐮𝐥𝐭𝐢𝐦𝐞𝐚 𝐜𝐥𝐚𝐮𝐳𝐞!")
        if hatz == 0:
            for ko in l:
                print(ko)
        if len(un_lit)!=0:
            ok1=1
            for lit in un_lit:
                if hatz == 0:
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
            if hatz == 0:
                print("𝐌𝐮𝐥𝐭𝐢𝐦𝐞𝐚 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐭𝐚:")
            if nesatisfiabilitate==1 and len(l)==1:
                if hatz == 0:
                    print([[]])
            else:
                if hatz == 0:
                    for i in l:
                        print(i)
            if hatz == 0:
                print("\n")
        if nesatisfiabilitate==0:
            lit_pur = literal_pur(l)
            if len(lit_pur) != 0:
                ok2 = 1
                for lit in lit_pur:
                    if hatz == 0:
                        print("literal pur ({})".format(lit_pur))
                    i = 0
                    while i < len(l):
                        if l[i].count(lit) != 0:
                            l.pop(i)
                        else:
                            i += 1
                if hatz==0:
                    print("𝐌𝐮𝐥𝐭𝐢𝐦𝐞𝐚 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐭𝐚:")
                    for k in l:
                        print(k)
                    print("\n")
    #set_trace()
    if len(l)==0:
        l3.append(-1)
    elif nesatisfiabilitate==0:
        if hatz == 0:
            print("𝐒𝐏𝐋𝐈𝐓 𝐏𝐄 𝐑𝐀𝐌𝐔𝐑𝐄")
        tn=1
        split(l)
        if hatz == 0:
            print("𝐑𝐀𝐌𝐔𝐑𝐀 𝟏:")
        for i in range(len(l2[ramura])):
            l2[ramura][i]=tuple(l2[ramura][i])
        ramura+=1
        if len(l1)==0:
            l3.append(-1)
            return
        else:
            if hatz == 0:
                dpll(l1)
                print("𝐑𝐀𝐌𝐔𝐑𝐀 𝟐:")
                for i in range(len(l2[parc_r])):
                    l2[parc_r][i] = list(l2[parc_r][i])
                if len(l2[parc_r]) == 0:
                    l3.append(-1)
                    return
                else:
                    parc_r += 1
                    dpll(l2[parc_r - 1])
def davis_putnam(l):
    global nnn
    un_lit=[]
    lit_pur=[]
    ok1=1;ok2=1
    global afirma
    contor=1
    permis=1
    h=0;s=0
    while permis==1 and len(l)>0:
        un_lit=[]
        lit_pur=[]
        ok1=0;ok2=0
        #set_trace()
        un_lit=un_literal(l)
        print("-------",contor,"--------")
        print("𝐌𝐮𝐥𝐭𝐢𝐦𝐞𝐚 𝐜𝐥𝐚𝐮𝐳𝐞:")
        for ko in range(len(l)):
            print(ko,")",l[ko])
        if len(un_lit)!=0:
            ok1=1
            for lit in un_lit:
                print("-----1 lit({})".format(lit))
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
                                        print("𝐄𝐬𝐭𝐞 𝐧𝐞𝐬𝐚𝐭𝐢𝐬𝐟𝐢𝐚𝐛𝐢𝐥𝐚!")
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
                                        print("𝐄𝐬𝐭𝐞 𝐧𝐞𝐬𝐚𝐭𝐢𝐬𝐟𝐢𝐚𝐛𝐢𝐥𝐚!")
                                        return
                            i+=1
        if ok1!=0:
            print("𝐌𝐮𝐥𝐭𝐢𝐦𝐞𝐚 𝐜𝐥𝐚𝐮𝐳𝐞 𝐭𝐚𝐫𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐭𝐞:")
            for ko in range(len(l)):
                print(ko, ")", l[ko])
            print("\n")
        lit_pur=literal_pur(l)
        if len(lit_pur)!=0:
            ok2=1
            for lit in lit_pur:
                print("literal pur ({})".format(lit))
                i=0
                while i<len(l):
                    if l[i].count(lit)!=0:
                        l.pop(i)
                    else:
                        i+=1
        if ok2!=0:
            print("𝐌𝐮𝐥𝐭𝐢𝐦𝐞𝐚 𝐜𝐥𝐚𝐮𝐳𝐞 𝐭𝐚𝐫𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐭𝐞:")
            for ko in range(len(l)):
                print(ko, ")", l[ko])
            print("\n")
        if ok1==0 and ok2==0 and len(l)>0:
            print("𝐒𝐞 𝐚𝐩𝐥𝐢𝐜𝐚 𝐫𝐞𝐳𝐨𝐥𝐮𝐭𝐢𝐚!")
            rezolutie(l)
            if len(nnn)!=0:
                print("\n","𝐔𝐫𝐦𝐚𝐭𝐨𝐚𝐫𝐞𝐚 𝐜𝐥𝐚𝐮𝐳𝐚 𝐬𝐞 𝐨𝐛𝐭𝐢𝐧𝐞 𝐝𝐢𝐧:",nnn[0])
            if afirma==0:
                permis=0
        contor+=1
    print("𝐄𝐬𝐭𝐞 𝐬𝐚𝐭𝐢𝐬𝐟𝐢𝐚𝐛𝐢𝐥𝐚!")
def rezolutie_apel(l):
    pas=[""]*len(l)
    i=0;j=0
    nou=[0]
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
                        lungime += 1
                else:
                    pas.pop()
                if len(nou)==0:
                    for ind in range(j+1):
                        print(ind,")",l[ind],"        ",pas[ind])
                    print("Este nesatisfiabila din {} si {}".format(i,j))
                    return
            j+=1
        i+=1
    if len(l)==0:
        print("𝐄𝐬𝐭𝐞 𝐕𝐚𝐥𝐢𝐝𝐚!")
    else:
        for ind in range(len(l)):
            print(ind, ")", l[ind], "      ", pas[ind])
        print("𝐄𝐬𝐭𝐞 𝐬𝐚𝐭𝐢𝐬𝐟𝐢𝐚𝐛𝐢𝐥𝐚!")
l3=[]
ok=0
print("𝐀𝐥𝐞𝐠𝐞𝐭𝐢 𝐮𝐧𝐚 𝐝𝐢𝐧𝐭𝐫𝐞 𝐨𝐩𝐭𝐢𝐮𝐧𝐢:","\n")
print("𝐏𝐞𝐧𝐭𝐫𝐮 𝐭𝐚𝐛𝐞𝐥 𝐬𝐚𝐮 𝐅𝐍𝐂/𝐅𝐍𝐃 𝐢𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐞𝐭𝐢 𝐧𝐮𝐦𝐚𝐫𝐮𝐥 ->>> 𝟏 <<<-!")
print("𝐏𝐞𝐧𝐭𝐫𝐮 𝐫𝐞𝐳𝐨𝐥𝐮𝐭𝐢𝐞,𝐃𝐏,𝐃𝐏𝐋𝐋 𝐢𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐞𝐭𝐢 𝐧𝐮𝐦𝐚𝐫𝐮𝐥 ->>> 𝟐 <<<-!")
print("--------------------------------------------------------")
print("𝐒𝐜𝐫𝐢𝐞𝐭𝐢 𝐨𝐩𝐭𝐢𝐮𝐧𝐞𝐚:")
k=int(input())
if k==1:
    semne = ["!", "&", "|", ">", "="]
    conectorii()
    st = str(input())
    st2 = str()
    for i in st:
        if semne.count(i) == 0:
            st2 += i
        elif i == "!":
            st2 += '¬'
        elif i == "&":
            st2 += '∧'
        elif i == "|":
            st2 += '∨'
        elif i == ">":
            st2 += '⇒'
        elif i == "=":
            st2 += '⇔'
    tabel(st2)
else:
    sub=[['P','¬Q'],['P','Q'],['¬Q','¬R'],['¬P']]
    print("𝐀𝐥𝐞𝐠𝐞𝐭𝐢 𝐮𝐧𝐚 𝐝𝐢𝐧𝐭𝐫𝐞 𝐨𝐩𝐭𝐢𝐮𝐧𝐢:", "\n")
    print("𝐏𝐞𝐧𝐭𝐫𝐮 𝐫𝐞𝐳𝐨𝐥𝐮𝐭𝐢𝐞 𝐢𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐞𝐭𝐢 𝐧𝐮𝐦𝐚𝐫𝐮𝐥 ->>> 𝟏 <<<-!")
    print("𝐏𝐞𝐧𝐭𝐫𝐮 𝐃𝐏 𝐢𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐞𝐭𝐢 𝐧𝐮𝐦𝐚𝐫𝐮𝐥 ->>> 𝟐 <<<-!")
    print("𝐏𝐞𝐧𝐭𝐫𝐮 𝐃𝐏𝐋𝐋 𝐢𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐞𝐭𝐢 𝐧𝐮𝐦𝐚𝐫𝐮𝐥 ->>> 𝟑 <<<-!")
    print("---------------------------------------------")
    print("𝐒𝐜𝐫𝐢𝐞𝐭𝐢 𝐨𝐩𝐭𝐢𝐮𝐧𝐞𝐚:")
    x = int(input())
    print("\n")
    if x == 1:
        rezolutie_apel(sub)
    elif x == 2:
        davis_putnam(sub)
    else:
        dpll(sub)
        for i in l3:
            if i == -1:
                print("------------------(None)-----------------","\n")
                print("𝐈𝐍𝐀𝐈𝐍𝐓𝐄 𝐃𝐄 𝐑𝐀𝐌𝐔𝐑𝐀 𝟐 𝐀𝐌 𝐎𝐁𝐓𝐈𝐍𝐔𝐓 𝐌𝐔𝐋𝐓𝐈𝐌𝐄𝐀 𝐕𝐈𝐃𝐀 𝐃𝐄𝐂𝐈",)
                print("𝐑𝐄𝐙𝐔𝐋𝐓𝐀  =>", "𝐄𝐒𝐓𝐄 𝐒𝐀𝐓𝐈𝐒𝐅𝐈𝐀𝐁𝐈𝐋𝐀!")
                ok = 1
                break
        if ok == 0:
            print("𝐄𝐒𝐓𝐄 𝐍𝐄𝐒𝐀𝐓𝐈𝐒𝐅𝐈𝐀𝐁𝐈𝐋𝐀!")
