import urllib.request
import os 
import pathlib







                                                                                                            


pathlib.Path(f"Avatares xat").mkdir(parents=True, exist_ok=True)
os.chdir(os.path.join(os.getcwd(),f"avatares xat")) 


totalAvatares=0
for i in range(0,1759):
    totalAvatares=totalAvatares+1
   
    DescargarAvatar= open(f'{i}.png','wb')

    print(f"Descargando-> https://xat.com/web_gear/chat/av/{i}.png")
    
    DescargarAvatar.write(urllib.request.urlopen(f'https://xat.com/web_gear/chat/av/{i}.png').read())
    
    DescargarAvatar.close()
print(f"Se han descargado un total de {totalAvatares} avatares.")
