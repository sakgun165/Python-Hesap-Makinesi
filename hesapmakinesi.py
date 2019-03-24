import time
print("""
1-Toplama->+
2-Çıkarma->-
3-Çarpma ->x
4->Bölme ->/
İşleminizi giriniz(örn:2+5)     
""")
liste=list()
while(True):
    islem=input()
    yedek1=int(islem[0])
    yedek2=int(islem[-1])
    liste=[yedek1,islem[1],yedek2]
    if(liste[1]=="+"):
        print(liste[0]+liste[-1])
    elif(liste[1]=="-"):
        print(liste[0]-liste[-1])
    elif(liste[1]=="x"):
        print(liste[0]*liste[-1])
    elif(liste[1]=="/"):
        print(liste[0]/liste[-1])
    else:
        print("Lütfen geçerli bir işlem giriniz. Program kapatılıyor...")
        time.sleep(3)
        break;

