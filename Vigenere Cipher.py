m=input("메세지:")
k=(lambda x:x*(len(m)//len(x)+1))(input("키:"))
print("암호화 :", "".join(j if j==" " else chr(ord(j)+ord(k[i])-97) if ord(j)+ord(k[i])-97 < 123 else chr(ord(j)+ord(k[i])-97-26) for i,j in enumerate(m)))
print("복호화 :", "".join(j if j==" " else chr(ord(j)-ord(k[i])+97) if ord(j)-ord(k[i])+97 > 96 else chr(ord(j)-ord(k[i])+97+26) for i,j in enumerate(m)))