import csv
a = []
def conectorii():
    print("NEGATIA:",'¬')
    print("DIJUNCTIA:",'∧')
    print("CONJUNCTIA:",'∨')
    print("IMPLICATIA:",'⇒')
    print("ECHIVALENTA:",'⇔')
def interpretari(x):
    global a
    for i in range(2 ** x):
        l = [0] * x
        j = len(l) - 1
        k = i
        while k != 0:
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
    else:
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
    k = 0
    q = 0
    formule = []
    nr = 0
    R = []
    con = ['⇒', '∨', '⇔', '¬', '∧']
    coloana_valori = []
    conector = str()
    prima_propozitie = str()
    a_doua_propozitie = str()
    propozitii = []
    for i in range(len(ss)):
        if con.count(ss[i]) == 0 and ss[i] != '(' and ss[i] != ')':
            if propozitii.count(ss[i]) == 0:
                propozitii.append(ss[i])
    # print(propozitii)
    interpretari(len(propozitii))
    for valori in a:
        s = ss
        for i in range(len(s)):
            if propozitii.count(s[i]) != 0:
                kk = str(valori[propozitii.index(s[i])])
                s = s.replace(s[i], kk)
        while len(s) > 1:
            t = str()
            for i in range(len(s)):
                if s[i] == '(':
                    k = i
            for i in range(k, len(s)):
                if s[i] == ')':
                    q = i
                    break
            if nr == 0:
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
            while i < len(s):
                if i < k or i > q:
                    t += s[i]
                else:
                    if ok == 0:
                        if rezultat != 0:
                            t += '1'
                        else:
                            t += '0'
                        ok = 1
                i += 1
            s = str()
            for i in range(len(t)):
                s += t[i]
        nr = 1
        coloana_valori.append(int(s))
    g = str()
    for i in formule:
        for j in i:
            g += j
        g += " "
    linia_1=[]
    for i in propozitii:
        linia_1.append(i)
    linia_1.append(ss)
    print(linia_1)
    L=[]
    #print(e, " ", ss)
    for i in range(len(a)):
        lux=[]
        for j in a[i]:
            lux.append(j)
        lux.append(coloana_valori[i])
        L.append(lux)
    print(L)
    with open("tabel.csv","w",encoding = "utf-8") as csv_f:
        f=csv.writer(csv_f)
        f.writerow(linia_1)
        f.writerows(L)
    FND = str()
    ok2 = 0
    FNC=str()
    #set_trace()
    for i in range(len(coloana_valori)):
        if coloana_valori[i] == 1:
            ok3 = 0
            if ok2 == 0:
                FND += '('
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
    for i in range(len(coloana_valori)):
        if coloana_valori[i] == 0:
            ok3 = 0
            if ok2 == 0:
                FNC += '('
                for j in range(len(a[i])):
                    if a[i][j] == 0:
                        if ok3 == 0:
                            FNC +=propozitii[j]
                            ok3 = 1
                        else:
                            FNC +='∨'+ propozitii[j]
                    else:
                        if ok3 == 0:
                            FNC +='¬'+propozitii[j]
                            ok3 = 1
                        else:
                            FNC += '∨'+'¬'+ propozitii[j]
                FNC += ')'
                ok2=1
            else:
                FNC += '∧'
                FNC += '('
                ok3 = 0
                for j in range(len(a[i])):
                    if a[i][j] == 0:
                        if ok3 == 0:
                            FNC +=propozitii[j]
                            ok3 = 1
                        else:
                            FNC += '∨'+ propozitii[j]
                    else:
                        if ok3 == 0:
                            FNC +='¬'+propozitii[j]
                            ok3 = 1
                        else:
                            FNC +='∨'+'¬'+propozitii[j]
                FNC += ')'
    print("Forma normal dijunctiva:", FND)
    print("Forma normal conjunctiva:",FNC)
conectorii()
print("Scrieti formula:")
e = str(input())
tabel(e)
