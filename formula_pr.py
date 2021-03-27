def formula(s):
    s2=str()
    indici=[]
    pd=int(0);i=0;ok1=int(0);ok2=int(0)
    p_at=['P','R','Q','S','T','P1','P2','B','G']
    con=['⇒','∨','⇔','¬','∧']
    while i<len(s):
        if len(s)==1 and p_at.count(s[i])!=0:
            print(i,":",s2)
            print(True)
            return
        if len(s)>1 and s[0]!='(':
            print(False)
            return
        if s[i]=='(':
            ok1+=1
            indici.append(i)
        if con.count(s[i])!=0:
            ok2+=1
        if s[i]=='(' and i==0:
            s2=s2+s[i]
            pd+=1
        elif s[i]=='(' and p_at.count(s[i-1])!=0:
            s2=s2+s[i]
            print(i,":",s2,False)
            return
        elif s[i]=='¬' and p_at.count(s[i-1])!=0:
            s2=s2+s[i]
            print(i, ":", s2, False)
            return
        elif (s[i]=='(' and s[i-1]=='(') or (s[i]=='(' and con.count(s[i-1])!=0):
            s2=s2+s[i]
            pd+=1
        elif (p_at.count(s[i])!=0 and s[i-1]=='(') or (p_at.count(s[i])!=0 and con.count(s[i-1])!=0):
            s2=s2+s[i]
            print(i, ":",s2)
        elif (con.count(s[i])!=0 and s[i-1]=='(') or (con.count(s[i])!=0 and s[i-1]==')'):
            s2=s2+s[i]
            print(i, ":",s2)
        elif (con.count(s[i])!=0 and p_at.count(s[i-1])!=0):
            s2=s2+s[i]
            print(i, ":",s2)
        elif (p_at.count(s[i])!=0 and s[i-1]!=')') or (p_at.count(s[i])!=0 and con.count(s[i-1])==0):
            s2=s2+s[i]
            print(i,":",s2,False)
            return
        elif (s[i]==')' and p_at.count(s[i-1])!=0):
            c=indici.pop();nr1=0;nr2=0
            for j in range(c,i):
                if s[j]=='(':
                    nr1+=1
                elif con.count(s[j])!=0:
                    nr2+=1
            if nr1!=nr2:
                print(i,":",False)
                return
            pd=pd-1
            s2=s2+s[i]
        elif s[i]==')' and s[i-1]==')':
            c=indici.pop();nr1=0;nr2=0
            for j in range(c,i):
                if s[j]=='(':
                    nr1+=1
                elif con.count(s[j])!=0:
                    nr2+=1
            if nr1!=nr2:
                print(i,":",False)
                return
            s2=s2+s[i]
            pd=pd-1
        else:
            s2=s2+s[i]
            print(i,":",s2)
            print(False)
            return
        i+=1
    if pd==0:
        if(ok1==ok2):
            print(i,":",s2)
            print(True)
        else:
            print(i,":",s2,False)
    else:
        print(i,":",s2,False)
d=str(input())
formula(d)