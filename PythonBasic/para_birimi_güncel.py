import requests
import sys

# birincidöviz=input("Birinci döviz:")    #### bizim birinci dövizimiz hep EUR çünkğ site bize sadece EUR'yi diğer para birimlerine çevirme olayını sunuyor
# ama biz şöyle bir trick yapabiliriz -> print kısmı :)

birincidöviz=input("Birinci döviz:")
ikincidöviz=input("İkinci döviz:")
miktar=float(input("Miktar:"))

url="http://data.fixer.io/api/latest?access_key=c3300e02be4267cfe562c580b8a56aaa"

response=requests.get(url)

json_verisi=response.json()
try:
    print((json_verisi["rates"][ikincidöviz]/json_verisi["rates"][birincidöviz])*miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru giriniz. Büyük harfle yazmaya dikkat ediniz!")
    sys.stderr.flush()