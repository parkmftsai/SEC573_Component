from PIL import Image
def getGPS(imobject):
    info=imobject._getexif()
    latDegrees =  info[34853][2][0][0]/float(info[34853][2][0][1])
    latDegrees += info[34853][2][1][0]/float(info[34853][2][1][1])/60    
    latDegrees += info[34853][2][2][0]/float(info[34853][2][2][1])/3600        
    lonDegrees =  info[34853][4][0][0]/float(info[34853][4][0][1])
    lonDegrees += info[34853][4][1][0]/float(info[34853][4][1][1])/60    
    lonDegrees += info[34853][4][2][0]/float(info[34853][4][2][1])/3600  
    if(info[34853][1]=='S'):
         latDegrees *= -1
    if(info[34853][4]=='W'):
         lonDegrees *= -1
    return latDegrees,lonDegrees

imobject=Image.open("./IMG_0007.JPG")
lat,lon=getGPS(imobject)

print(lon,lat)
print("http://maps.google.com/maps?q=%.9f,%.9f&z=15" %(lat,lon))



