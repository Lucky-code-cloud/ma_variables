#Malamulo a Kalembedwe Code ku Python
#https://github.com/Lucky-code-cloud/ma_variables.git

#Example 1
#Iyi ndi Comment ndipo siimaoneka mukapanga run
print("Moni Amalawi!")


#Example 2
"""
Kalembedwe ka 
comment kena
pakakhala mizele 
yambili
"""
print("Comment Ina")



#Example 3
#Indentation ndi Space ya kumayambililo
if 3 > 2:
    print("3 ndi wamkulu kwa 2")



#Example 4
"""
Kulemba ma variable
Ma variable amasungila ma values
"""
Danny = "Mphunzitsi"
Sandram = "Student"
print(Danny)
print(Sandram)



#Example 5
#Casting imafunika popanga specify data type
Hope = str(1)
Dan = int(1)
Python = float(1)
print(Hope)
print(Dan)
print(Python)



#Example 6
#Kudziwa Data type
x = 5
y = "Five"
print(type(x))
print(type(y))



#Example 7
#Single Ndi Double Quote Saasiyana
Asher = "Woyimba Guitar"
Asher = 'Woyimba Guitar'



#Example 8
#Kusiyana ma Capital Letters Kumasiyanisa ma Variable
a = "Distinction"
A = 100
print(a)
print(A)



#Example 9
#Maina a ma Variable
"""
-Yambani ndi ma letter kapena underscore
-Osayamba ndi ma number
-Ofunika ma aplha numeric values(A-Z, 0-9, _)
-Ma Case amasiyana(lucky, Lucky ndi LUCKY ndi osiyana)
-Osagwilisa ntchito ma Keywords
"""
#Camel Case
luckyHarveyBanda = "Black"
#Pascal Case
LuckyHarveyBanda = "Black"
#Snake Case
lucky_harvey_banda = "Black"



#Example 10
#Kupeleka ma values angapo nthawi imodzi
G,M = "Gerald","Mwalwanda"
print(G)
print(M)



#Example 11
#Kupeleka value Imodzi ku ma variable angapo
Arthur = Michael = Bunaya = "Arthedonia"
print(Arthur)
print(Michael)
print(Bunaya)



#Example 12
#Kutambasula gulu la zinthu(Unpacking a collectio[lists, tuples and dictionaries])
ma_galimoto_omwe_lucky_amakonda = ["Mercedez AMG GT 63", "Dodge Challenger", "Ford Mustang"]
Benz,Dodge,Ford = ma_galimoto_omwe_lucky_amakonda
print(Benz)
print(Dodge)
print(Ford)



#Example 13
#Kupanga Display ma variables kugwilisa ntchito print function
Malawi = "The Warm Heart Of Africa"
print(Malawi)

#Kupanga display ma variable angapo
Mzuzu = "Northern"
Lilongwe = "Central"
Blantyre = "Southern"
print(Mzuzu, Lilongwe, Blantyre)
#print(Mzuzu + Lilongwe + Blantyre)

#Kupanga display data ya ma type osiyana
Beans = "Nyemba"
Meat = "Nyama"
Rice = "Mpunga"
Palibeso = 1
#Sprint(Rice + "wa" + Beans + "Komaso" + "Meat" + "ndi number" + Palibeso)
print(Rice, "wa", Beans, "Komaso", Meat, "ndi number", Palibeso)



#Example 14
#Global Variables
"""
Ma Global Variable ndi ma variable amane 
Tikhoza kugwilisa nthcito mkati kapena
kunja kwa ma function athu
"""
Keith = "Murray"

def functionYaKeith():
    Keith = "Padre"
    print("Keith ndi " + Keith)
functionYaKeith()

#Ngati Variable ili mkati mwa function, siigwila ntchito panja
Anthony = "Emmanuel"

def functionYaEmmanuel():
    Anthony = "Ntchana"
    print("Anthony ndi " + Anthony)
functionYaEmmanuel()

print("Anthony ndi " + Anthony)

#Kupanga kuti variable ikhale global koma ili mkati mwa function
def functionYaHelbert():
    global Helbert
    Helbert = "Engineer"
functionYaHelbert()
print("Helbert ndi " + Helbert)

#Kusintha value kugwilisa ntchito global
Francis = "blackhat"

def functionYaFrancis():
    global Francis
    Francis = "Black Hat"
functionYaFrancis()
print("Francis ndi " + Francis)