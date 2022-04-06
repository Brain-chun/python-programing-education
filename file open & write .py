list = ['한국','미국','캐나다','영국','러시아','베트남']

outFp = None
outFp = open("C:/Education/ErrorLog.txt", "w", encoding = 'utf-8')

for _ in list:
    name = input("나라 이름을 입력하세요 : ")
    if name in list:
        print(list.index(name))
    else:
        print("'"+ name +"'","is not in list 국가는 리스트에 존재하지 않습니다. 로그기록")
        outFp.write(name)
        outFp.write('\n')

outFp.close()
