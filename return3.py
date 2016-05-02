import sys

genoma= sys.argv[1].lower()

n=0
n = input()

tam_genoma = len(genoma)

dic = {}

cont=0;

#print(genoma[cont:n+cont])

for x in (genoma[cont:tam_genoma]):
	if(genoma[cont:cont+n]  not in dic):	
		dic.update({genoma[cont:cont+n] :1})
	else:
		dic[genoma[cont:cont+n]]+=1

	cont+=1

#print(dic)

print max(dic, key=dic.get)
 

