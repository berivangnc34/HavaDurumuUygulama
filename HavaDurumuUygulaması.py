import requests
import json #veri çekme işlemi

origin_url="https://api.openweathermap.org/data/2.5/weather?q=Istanbul,tr&APPID=8b50fa56ed093c1c27f9b164e72151cc"
#json formatına cevirdik chrome üzerinden


response=requests.get(origin_url) #linki aldık gelen mailden

jsonResponse=json.loads(response.text) #bana bölerek verileri getir. bu dosyaya at

print(jsonResponse["name"])

print( "Sicaklik:" + str(jsonResponse["main"]["temp"]))

print("Basinc:"+  str(jsonResponse["main"]["pressure"]))

print("Basinc:"+  str(jsonResponse["main"]["humidity"]))



                

                            
                
                                  
                                  

