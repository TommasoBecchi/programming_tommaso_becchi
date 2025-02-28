def matrice (nome):
    matrix={}
    file=open(nome,"r")
    import input_data
    r=input_data.matrix_rows_cols
    tab=[r]
    let=-1
    for line in file:
        if let==-1:
            let+=1
        else:
            riga=[r[let]]
            line=line.rstrip()
            line=line.split()
            for n in line:
                n=n[0:len(n)-1]
                riga.append(int(n))
            tab.append(riga)
            let+=1
    for i in range (1,len(tab)):
        for j in range (1,len(tab[i])):
            matrix[r[j-1]+r[i-1]]=tab[i][j]
            matrix[r[i-1]+r[j-1]]=tab[i][j]
    return matrix

pam250=matrice("PAM250.txt")
blosum62=matrice("BLOSUM62.txt")
gap=-2

def score (s1,s2,matrice,gap):
    punteggio=0
    for i in range(len(s1)):
        if s1[i]!="-" and s2[i]!="-":
            punteggio+=matrice[s1[i]+s2[i]]
        else:
            punteggio=punteggio+gap
    return punteggio

import input_data
sequenze=input_data.alignments
for i in sequenze:
    for j in range (1):
        print i[j],"\n",i[j+1]
        print "PAM: ",score(i[j],i[j+1],pam250,gap)
        print "BLOSUM: ",score(i[j],i[j+1],blosum62,gap)

# Re-score the alignments using an affine gap penalty model
def rescore (s1,s2,matrice,gap0,gap):
    punteggio=0
    for i in range(len(s1)):
        if s1[i]!="-" and s2[i]!="-":
            punteggio+=matrice[s1[i]+s2[i]]
        else:
            if (s1[i]=="-" and s1[i-1]!="-") or (s2[i]=="-" and s2[i-1]!="-"):
                punteggio=punteggio+gap0
            else:
                punteggio=punteggio+gap
    return punteggio
gap=-0.5
gap0=-2
print "Re-score the alignments"
for i in sequenze:
    for j in range (1):
        print i[j],"\n",i[j+1]
        print "PAM: ",rescore(i[j],i[j+1],pam250,gap0,gap)
        print "BLOSUM: ",rescore(i[j],i[j+1],blosum62,gap0,gap)
