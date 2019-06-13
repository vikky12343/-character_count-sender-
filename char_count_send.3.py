f=open("character.txt","w+")
s=raw_input('Enter the character:')
i=0
s1=''
s2=''
j=0
while i<len(s):
	if s[i]==' ':
		s1=s1+str(j)+s2
		s2=''
		j=0
	else:
		s2=s2+s[i]
		j=j+1
	i=i+1
s1=s1+str(j)+s2
print s1
f=open("character.txt","w")
f.write(s2)




