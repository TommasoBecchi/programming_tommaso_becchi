f=open("blosum.txt","r")
tab=[]
for line in f:
    line.rstrip()
    line=line.split()
    tab.append(line)

blosum={}
for i in range (0,len(tab[0])):
    for j in range (1, len(tab)):
        blosum[tab[0][i]+tab[j][0]]=tab[i+1][j]

s1="ALASVLIRLITRLYP"
s2="ASAVHLNRLITRLYP"
def score(blosum,s1,s2):
    score=0
    for i in range(len(s1)):
        score=score+int(blosum[s1[i]+s2[i]])
    return  score
print score(blosum,s1,s2)
