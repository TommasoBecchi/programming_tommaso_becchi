import input_data
s1=input_data.seq1
s2=input_data.seq2
blosum=input_data.BLOSUM52

def matrix (s1,s2,blosum,d):
    s1="0"+s1
    s2="0"+s2
    F=[[x*-d for x in range (len(s1))]]
    P=[]
    rP=["0"]
    for i in range (len(s1)-1):
        rP.append("S")
    P.append(rP)
    for i in range (1,len(s2)):
        riga=[i*-d]
        F.append(riga)
        riga=["A"]
        P.append(riga)
    for i in range (1, len(s2)):
        for j in range (1, len (s1)):
            if s1[j]+s2[i] in blosum.keys():
                chiave=s1[j]+s2[i]
            else:
                chiave=s2[i]+s1[j]
            F[i].append(max(F[i-1][j-1]+blosum[chiave],F[i-1][j]-d,F[i][j-1]-d))
            if F[i][j]==F[i-1][j-1]+blosum[chiave]:
                P[i].append("D")
            elif F[i][j]==F[i-1][j]-d:
                P[i].append("A")
            else:
                P[i].append("S")
    return [F,P]

def alignment (s1,s2,F,P):
    a1=""
    a2=""
    c=len(F[0])-1
    r=len(F)-1
    s=F[r][c]
    while P[r][c]!="0":
        if P[r][c]=="D":
            a1+=s1[c-1]
            a2+=s2[r-1]
            r-=1
            c-=1
        elif P[r][c]=="S":
            a1+=s1[c-1]
            a2+="-"
            c-=1
        else:
            a1+="-"
            a2+=s2[r-1]
            r-=1
    x=a1[::-1]
    y=a2[::-1]
    return [x,y,s]
    
F=matrix(s1,s2,blosum,2)[0]
P=matrix(s1,s2,blosum,2)[1]
a1=alignment(s1,s2,F,P)[0]
a2=alignment(s1,s2,F,P)[1]
score=alignment(s1,s2,F,P)[2]
print a1,"\n",a2,"\n score= ",score
