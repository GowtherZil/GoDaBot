import telebot
import datetime
from telebot import types

bot = telebot.TeleBot("x")
#                                                                                                                                                                                                                                                                                                                                                                                                                               Gaby      Zod        Jesu                                                                                                                                                                                   alt Gaby
listaPermitidos=[x]
#                                                                                                                         
listaGruposPermitidos = [x]

lista_Permitidos_Info = [x]

lista_tiers=("1","2","3","4","5")

file = open("reports","r")
actual_battle = file.read().split(",")[0]
file.close()

file = open("gremio","r")
lista_gremios_conocidos = file.read()
file.close()

usuarito = uno ahi
                                                #Metodos del withdraw
def pincha(msg, who,user,message):
    banned = True
    if who in listaPermitidos:
        banned = False
    if banned :
        identificacion = "@" + user
        bot.send_message(who,"Usuario Baneado. Contacte al creador para comprar permisos.....")
        bot.send_message(usuarito,"Recibi un mensaje del siguiente usuario: " + identificacion)

    else:
        msg = seccionarMsg(msg)
        msg = crearEnlaces(msg)
        msg = unirEnlaces(msg)
        contador = 0
        for x in msg:
            if(len(msg[contador])>13):
                 mensaje = "[Reenviar a cw](https://t.me/share/url?url={})".format(msg[contador])
                 bot.send_message(message.chat.id, mensaje,parse_mode="MarkdownV2")
                 contador = contador + 1

def pincha_grupo(msg, who,user,message):
    banned = True
    if who in listaGruposPermitidos:
        banned = False
    if banned:
        bot.send_message(message.chat.id, "Sorry, este grupo esta baneado, contacte al creador para eliminarle el ban")
    if not banned:
        msg = seccionarMsg(msg)
        msg = crearEnlaces(msg)
        msg = unirEnlaces(msg)
        contador = 0
        for x in msg:
            if(len(msg[contador])>13):
                 mensaje = "[Reenviar a cw](https://t.me/share/url?url={})".format(msg[contador])
                 bot.send_message(message.chat.id, mensaje,parse_mode="MarkdownV2")
                 contador = contador + 1

def seccionarMsg(msg):
  seccion = ""
  contador = 0
  text = msg.split()
  for item in text:
     if(item.isnumeric()):
         seccion = seccion + item + " "
         contador = contador+1
  seccion = seccion.split()
  return seccion

def crearEnlaces(msg):
  print("")
  print(len(msg))
  print("")
  print(msg)
  cantWithdraws = 0
  can = False
  lenght = len(msg)
  while(can != True):
    if  lenght > 18:
        cantWithdraws = cantWithdraws + 1
        lenght = lenght - 18
    else:
        cantWithdraws = cantWithdraws + 1
        can = True
  inicio = 0
  fin = inicio + 18
  enlaces=[]
  while cantWithdraws!=0:
    enlace = ["/g_withdraw "]
    temporal = separarWithdraw(msg,inicio,fin)
    agregar = ""
    contador = 0
    for x in temporal:
        agregar = agregar + temporal[contador] + " "
        contador = contador + 1
    enlace.append(temporal)
    enlaces.extend(enlace)
    cantWithdraws = cantWithdraws - 1
    inicio = fin
    fin = fin + 18
  return enlaces

def separarWithdraw(msg,inicio,fin):
    withdraws = []
    if inicio < len(msg):
         if inicio == len(msg) :
             withdraws.append(msg[inicio])
         if fin <= len(msg):
             while inicio != fin:
                 withdraws.append(msg[inicio])
                 inicio = inicio + 1
         if fin > len(msg):
                 fin = len(msg)
                 while inicio != fin:
                    withdraws.append(msg[inicio])
                    inicio = inicio + 1
    return withdraws

def unirEnlaces(enlaces):
    veces = len(enlaces)/2
    contador = 0
    final = []
    while veces!=0:
       string = str(enlaces[contador])
       txt = hacerString(enlaces[contador + 1])
       string = string + txt
       final.append(string)
       contador = contador + 2
       veces = veces - 1
    return final

def hacerString(msg):
    prueba = ""
    contador = 0
    for x in msg:
      prueba = prueba + msg[contador] + " "
      contador  = contador + 1
    return prueba



                                                    #Metodos para el exchange#

#Devuelve el codigo dado el nombre del item. Checkear los items
def searchItem(item_name):
    items_dic ={
        "Thread" : "01",
        "Hilo" : "01",
        "hilo" : "01",
        "Stick" : "02",
        "palo" : "02",
        "palos" : "02",
        "Pelt" : "03",
        "Bone" : "04",
        "Coal" : "05",
        "Charcoal" : "06",
        "Powder" :  "07",
        "Iron Ore" : "08",
        "Cloth" : "09",
        "Silver Ore" : "10",
        "Bauxite" : "11",
        "Cord" : "12",
        "Magic stone" : "13",
        "ms" :"13",
        "Wooden shaft" : "14",
        "Sapphire" : "15",
        "Solvent" : "16",
        "Ruby" : "17",
        "Hardener" : "18",
        "Steel" : "19",
        "Leather" : "20",
        "Bone powder" : "21",
        "String":"22",
        "Coke":"23",
        "Purified powder":"24",
        "purified":"24",
        "Silver alloy" : "25",
        "Steel mold" : "27",
        "Blacksmith frame" : "28",
        "bs frame" : "28",
        "rope" : "29",
        "Artisan frame" : "30",
        "af" : "30",
        "metal plate" : "31",
        "metal" : "31",
        "metallic fiber":"34",
        "mf" : "34",
        "Crafted leather" : "35",
        "Quality Cloth" : "36",
        "qc" : "36",
        "Blacksmith mold":"37",
        "bs mold" : "37",
        "Artisan mold" : "38"
    }
    return items_dic.get(item_name)

#Devuelve el item dado el codigo y viceversa. Checkear los items
def GetCode(to_search):
    items_dic ={
        "thread" : "01",
        "01" : "thread",
        "stick" : "02",
        "02" : "stick",
        "palo" : "02",
        "palos" : "02",
        "02" : "palos",
        "pelt" : "03",
        "03" : "pelt",
        "bone" : "04",
        "04" : "bone",
        "coal" : "05",
        "05" : "coal",
        "charcoal" : "06",
        "06" : "charcoal",
        "powder" :  "07",
        "07" : "powder",
        "iron ore" : "08",
        "08" : "iron ore",
        "cloth" : "09",
        "09" : "cloth",
        "silver ore" : "10",
        "10" : "silver ore",
        "bauxite" : "11",
        "11" : "bauxite",
        "cord" : "12",
        "12" : "cord",
        "magic stone" : "13",
        "13" : "magic stone",
        "ms" :"13",
        "wooden shaft" : "14",
        "14" : "wooden shaft",
        "sapphire" : "15",
        "15" : "sapphire",
        "solvent" : "16",
        "16" : "solvent",
        "ruby" : "17",
        "17" : "ruby",
        "hardener" : "18",
        "18" : "hardener",
        "steel" : "19",
        "19" : "steel",
        "leather" : "20",
        "20" : "leather",
        "bone powder" : "21",
        "21" : "bone powder",
        "string":"22",
        "22" : "string",
        "coke":"23",
        "23" : "coke",
        "purified powder":"24",
        "24" : "purified powder",
        "purified":"24",
        "silver alloy" : "25",
        "25" : "silver alloy",
        "steel mold" : "27",
        "sm" : "27",
        "27" : "steel mold",
        "silver mold" : "28",
        "28" : "silver mold",
        "blacksmith frame" : "29",
        "29" : "blacksmith frame",
        "bs frame" : "29",
        "artisan frame" : "30",
        "af" : "30",
        "30" : "artisan frame",
        "rope" : "31",
        "31" : "rope",
        "silver frame" : "32",
        "sf" : "32",
        "32" : "silver frame",
        "metal plate" : "33",
        "33" : "metal plate",
        "metal" : "33",
        "metallic fiber":"34",
        "34" : "mettalic fiber",
        "mf" : "34",
        "crafted leather" : "35",
        "35" : "crafted leather",
        "quality cloth" : "36",
        "36" : "quality cloth",
        "qc" : "36",
        "blacksmith mold":"37",
        "bm" : "37",
        "bs mold" : "37",
        "37" : "blacksmith mold",
        "artisan mold" : "38",
        "am" : "38",
        "38" : "artisan mold",
    }
    if items_dic.get(to_search) == None:
      pass
    else:
      return items_dic.get(to_search)


# def seccionarMsg(msg):
#   seccion = ""
#   contador = 0
#   text = msg.split()
#   for item in text:
#      if(item.isnumeric()):
#          seccion = seccion + item + " "
#          contador = contador+1
#   seccion = seccion.split()
#   return seccion

#Devuleve el stock del usuario por id
def getUsersStock(id):
    msg = open("file.txt","r")
    msg = msg.read()
    indice_inicio = msg.index(str(id))
    stock_temporal = msg[indice_inicio:len(msg)]
    indice_final = stock_temporal.index(",")
    stock_temporal = stock_temporal[0:indice_final]
    stock_temporal = stock_temporal.split()
    stock_retorno = ""
    indice = 0
    for x in stock_temporal:
        if indice != 0:
            stock_retorno = stock_retorno + stock_temporal[indice] + " "
        indice = indice + 1
    return stock_retorno


#Combinando saveStock y refresh
def saveUsersStock(msg,id):
    try:
        file = open("file.txt","r")
        allStocks = file.read()
        file.close()    # cerrando el fichero
    except:
        file = open("file.txt","w")
        file.close()
        file = open("file.txt","r")
        allStocks = file.read()
        file.close()
    if str(id) not in allStocks:
        file = open("file.txt","a")   # agregando al final del archivo
        file.write(str(id) + " " + msg + ", ")
        file.close()
    else:
        try:
            stock = str(id) + " " + msg
            previous_stock = str(id) + " " + getUsersStock(id)
            replaced_bd = allStocks.replace(previous_stock,stock)
            file = open("file.txt","w")  # sobreescribiendo el archivo desde 0
            file.write(replaced_bd)
            file.close()
        except:
            print("Excepcion leyendo , lineas 312-337 , saveUserStock")
            bot.send_message(id,"No pude completar la operacion")

def removeFile():
    file = open("file.txt","w")
    file.close()

def seccionarStock(msg):
    print("Entrando al metodo seccionarStock")
    seccion = ""
    c = 2
    text = msg.split()
    print(text)
    #en este caso no c han usado los gnomos
    if "/sg_" in msg:
        text = text[12:len(text)]
        contador = 0
        for x in text:
            if "/sg_" in x:
                 seccion = seccion + text[contador][4:len(text[contador])] + " "
            if "(" in x:
                 h = text[contador][1:len(text[contador])-1]
                 seccion = seccion + h + " "
            contador = contador + 1
    else:
        while c < len(text):
            if "(" in text[c]:
                h = text[c][1:len(text[c])-1] # h = todo entre parentesis
                seccion = seccion + h + " "
            elif not ("(" in text[c]) and not("(" in text[c+1]):
                compuesta = ""
                compuesta = text[c] + " " + text[c+1]
                print("")
                print("")
                print("")
                print(compuesta.lower())
                print("")
                print("")
                print("")
                seccion = seccion + GetCode(compuesta.lower()) + " " #este GetCode de aki es el metodo q tenias q implementar y lo mismo d arriba con la c
                c = c+1
            else:
                seccion = seccion + GetCode(text[c].lower()) + " "

            c = c+1

    return seccion

def SeccionarHide(id,msg):  # TALLA AKI : Este parece tar en talla
    print("Entrando a Seccionar Hide")
    seccion = ""
    text = msg.split()
    print( "Text:")
    print(text)
    print(" " )
    c = 1
    while c < len(text):
        if (text[c] != "Hide" or text[c] != "hide"):
            print("Longitud = " + str(len(text)))
            if text[c].isnumeric() == False:
                if  (text[c].lower() == "silver" or text[c].lower() == "iron" or text[c].lower() == "wooden" or text[c].lower() == "artisan" or text[c].lower() == "magic" or text[c].lower() == "metal" or ((text[c].lower() == "bone") and (text[c+1].lower() == "powder"))):
                    try:
                        print("Buscando la compuesta : " + str(text[c]) + " " + str(text[c+1]))
                        codigo = GetCode(str(text[c]) + " " + str(text[c+1]))
                        seccion = seccion + codigo + " "
                    except:
                        print("Compuesta incompleta")
                        bot.send_message(id,"Comenzando simulación humorística de bullying..... JA JA JA JA JA JA JA JA. Humano, si no es mucho pedirle a su bajo intelecto, verifique que introdujo correctamente todos los nombres y porfavor, trate de respirar mientras lo hace , es vital para su salud")

                    if c+2 < len(text):
                        try:
                            codigo = GetCode(str(text[c+1]) + " " + str(text[c+2]))
                            seccion = seccion + codigo + " "
                        except:
                            print("Compuesta incompleta y problemas con items despues de esta")
                    else:
                        try:
                            codigo = GetCode(str(text[c+1]))
                            seccion = seccion + codigo + " "
                        except:
                            print("Compuesta incompleta y problemas con items despues de esta")
                    c = c+2
                else:
                    print("Item:")
                    print(str(text[c]))
                    textito = GetCode(str(text[c]))
                    print(textito)
                    if (textito != None):
                        seccion = seccion + GetCode(str(text[c])) + " "
                    c = c+1
            else:
                seccion = seccion + str(text[c]) + " "
                c = c+1

    return seccion

def hideShit(id,msg): # Recibe un string de la forma "hide ms 01 powder pelt Iron ore" y devuelve todos los comandos para esconder "/wts_13_cant en stock_1000" etc etc
    stock = getUsersStock(id)
    print("stock = " + stock)
    stock = stock.split()
    hide = SeccionarHide(id,msg)
    print("hide = " + hide)
    hide = hide.split()
    comandos = [""]
    d = 0
    while d < len(hide):
        c = 0
        while c < len(stock):
            if stock[c] == hide[d]:
                  print("https://t.me/share/url?url=/wts%20{}_%20{}_1000".format(stock[c],stock[c+1]))
                  comandos.append("https://t.me/share/url?url=/wts_{}_{}_1000".format(stock[c],stock[c+1]))
                # comandos = comandos + "/wts_" + stock[c] + "_" + stock[c+1] + "_1000" + " "
            c = c+2
        d = d+1
    print("comandos : ")
    print(comandos)
    # comandos = comandos.split()
    z = 1
    while z != len(comandos):
        link = "[Reenviar a cw]({})".format(comandos[z])
        bot.send_message(id, link,parse_mode="MarkdownV2")
        z = z+1

#recuerda annadir el handler para esto... lo q me dijiste de los comandos
def hideShitonGuild(id,msg): # Recive un string de la forma "g_hide ms 01 powder pelt Iron ore" y devuelve todos los comandos para esconder "/wts_13_cant en stock_1000" etc etc
    print("Entrando a hideShitonGuild")
    stock = getUsersStock(id)
    stock = stock.split()
    hide = SeccionarHide(id,msg)
    print("Stock:")
    print(stock)
    print("")
    print("Hide:" + hide)
    hide = hide.split()
    comandos = [""]
    d = 0
    while d < len(hide):
        c = 0
        while c < len(stock):
            if stock[c] == hide[d]:
                  comandos.append("https://t.me/share/url?url=/g_deposit%20{}%20{}".format(stock[c],stock[c+1]))
                # comandos.append("/g_deposit " + stock[c] + " " + stock[c+1] + " ")
            c = c+2
        d = d+1
    print("Comandos:")
    print(comandos)
    # print("Comandos:" + comandos)
    # comandos = comandos.split()
    z = 1
    while z != len(comandos):
        link = "[Reenviar a cw]({})".format(comandos[z])
        bot.send_message(id, link,parse_mode="MarkdownV2")
        z = z+1

def sendSellCodes(id,msg):  # Recibe un string como "Vende 20 ms a 18" para devolver "/wts_13_20_18"
    stock = getUsersStock(id)
    stock = stock.split()
    selling = msg.split()
    item_qtt = selling[1]
    item_price = selling[len(selling)-1]
    if len(selling) == 5:   #en caso de q el nombre sea unico
        item_code = GetCode(selling[2])
    else:
        item_code = GetCode("{} {}".format(selling[2] , selling[3])) # en caso de que el nombre sea compuesto
    item_qtt_index = stock.index("i-"+item_code)+1
    qtt = stock[item_qtt_index]
    qtt = int(qtt) - int(item_qtt)
    if qtt >= 0:  #si al actualizar la cantidad del item en el stock del usuario da 0 o mas:
        stock[item_qtt_index] = qtt
        index = 0
        stock2save = ""
        for x in stock:
            stock2save = stock2save + "{}".format(stock[index]) + " "
            index = index+1
        saveUsersStock(stock2save,id)
        bot.send_message(id,"[Reenviar a cw](/wts_{}_{}_{})".format(item_code,item_qtt,item_price),parse_mode="MarkdownV2")
    else: #si da negativo tonces:
        bot.send_message(id,"Usted no tiene la cantidad necesaria de {}".format(GetCode(item_code)))
        
class hero:
    def __init__(self,tier,hero_user,perc):
        self.hero_user = hero_user
        self.tier = tier
        self.perc = perc

    def update_tier(self,tier):
        self.tier = tier

    def update_perc(self,perc):
        self.perc = perc

def save_hero(msg):
    found = int(search_hero_tier(msg))
    if found == 0:
        if len(msg.text.split())==1:
            bot.send_message(msg.from_user.id,"Querido usuario, porfavor especifica tu tier. Si no sabes como hacerlo revisa mi boton de ayuda")
        else:
            tier = msg.text.split()[1]
            if tier in lista_tiers:
                f = open("heroes.txt","a")
                f.write("{}-{}-0".format(tier,msg.from_user.id))
                f.write(",")
                f.close
                bot.send_message(msg.from_user.id,"He memorizado satisfactoriamente que usas drops de tier {}".format(tier))
                print("Se ha guardado al heroe {} con el tier {}".format(msg.from_user.id,tier))
            else:
                bot.send_message(msg.from_user.id,"Querido usuario, {} no es un tier valido".format(tier))
    else:
        bot.send_message(msg.from_user.id,"Este heroe ya lo conocia")
        print("El heroe que intenta guardar ya se encuentra en la base de datos")

def read_heroes():
    f = open("heroes.txt","r")
    lista_heroes = f.read()
    f.close
    info = list((""))
    lista_heroes = lista_heroes.split(',')
    for x in range(len(lista_heroes)):
        if lista_heroes[x] != "":
            heroe = lista_heroes[x].split("-")
            tier = heroe[0]
            id = heroe[1]
            perc = heroe[2]
            heroe = hero(tier,id,perc)
            info.append(heroe)
    return info

def search_hero_tier(message):
    heroes = read_heroes()
    for x in range(len(heroes)):
        print("Buscando el id {} y encontrando el id {}".format(message.from_user.id,heroes[x].hero_user.strip()))
        if (str(heroes[x].hero_user) == str(message.from_user.id)):
            print("Devolviendo {}".format(heroes[x].tier))
            return heroes[x].tier
    return 0

def search_hero_perc(message):
    heroes = read_heroes()
    for x in range(len(heroes)):
        print("Buscando el id {} y encontrando el id {} con perception {}".format(message.from_user.id,heroes[x].hero_user.strip(),heroes[x].perc))
        if (str(heroes[x].hero_user) == str(message.from_user.id)):
            print("Devolviendo {}".format(heroes[x].perc))
            return heroes[x].perc
    return 0

#Este le pide la hora a Glados y luego la convierte a la hora nuestra, duvuelve un string de las horas y los minutos con el formato xx:xx
def GladosT():
    x = datetime.datetime.now()
    h = x.strftime("%H")
    h = int(h) - 5
    if(h<0): h += 24
    m = x.strftime("%M")
    fh = str(h) + ":" + m
    return fh

#Este te va a devolver el intervalo de tiempo del CW eg:Morning separado x un espacio del tiempo restante para el cambio del intervalo
def GetCWTime():
    fh = GladosT()
    fh = fh.split(":")
    h = fh[0]
    m = fh[1]
    if(h=="2" or h=="3" or h=="10" or h=="11" or h=="18" or h=="19"):
        time = "Morning"
    elif(h=="4" or h=="5" or h=="12" or h=="13" or h=="20" or h=="21"):
        time = "Day"
    elif(h=="6" or h=="7" or h=="14" or h=="15" or h=="22" or h=="23"):
        time = "Evening"
    else:
        time = "Night"

    h = int(h)

    if(h%2 == 0): topm = 120
    else: topm = 60

    timeRemaining = topm - int(m)

    result = time + " " + str(timeRemaining)

    return result

def reformtRemaining(t):
    t = int(t)
    if(t>59):
        rest = t-60
        result = "1h y " + str(rest) + "min"
    else: result = str(t) + "min"

    return result

def FacilitarDrops(place, time, tier):
    time = time.split()
    hora = time[0]
    tRemaining = reformtRemaining(time[1])
    drops = ""

    print("Buscando drops en {} en la hora {} y con {} minutos de tiempo restante y para el tier {}".format(place,hora,tRemaining,tier))

    if(place == "forest" or place == "Forest"):
        if(hora == "Morning"):
            if(tier == "2"):
                drops = "Lo lamento humano(lies) No hay drops para tu Tier actual en Forest."
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Forest at Morning.

k20 Doomblade blade
r21 Eclipse recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Forest at Morning.

k93 Phoenix Sword part
r81 Council Gauntlets recipe
r91 Griffin Knife recipe
r100 Assault Cape recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Forest at Morning.

k104 Lightbane Katana part
k124 Discarnate Bracers part
k112 Manticore Armor part
k114 Manticore Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Day"):
            if(tier == "2"):
                drops = "Lo lamento humano(lies) No hay drops para tu Tier actual en Forest."
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Forest at Day.

k23 King's Defender blade
r24 Raging Lance recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Forest at Day.

k89 Celestial Boots part
k91 Griffin Knife part
k101 Craftsman Apron part
r94 Heavy Fauchard recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Forest at Day.

r105 Doom Warglaive recipe
k116 Overseer Shield part
k115 Manticore Gloves part
r116 Overseer Armor recipe
r118 Overseer Boots recipe
k106 Decimation Harpoon part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Evening"):
            if(tier == "2"):
                drops = "Lo lamento humano(lies) No hay drops para tu Tier actual en Forest."
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Forest at Evening.

k26 Lightning Bow shaft
r27 Hailstorm Bow recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Forest at Evening.

k94 Heavy Fauchard part
r90 Celestial Bracers recipe
r92 Minotaur Sword recipe
r102 Stoneskin Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Forest at Evening.

k109 Windstalker Bow part
k116 Overseer Shield part
k113 Manticore Helmet part
k114 Manticore Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Night"):
            if(tier == "2"):
                drops = "Lo lamento humano(lies) No hay drops para tu Tier actual en Forest."
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Forest at Night.

k29 Skull Crusher head
r30 Dragon Mace recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Forest at Night.

k90 Celestial Bracers part
k92 Minotaur Sword part
r83 Griffin Armor recipe
r102 Stoneskin Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Forest at Night.

k104 Lightbane Katana part
r110 Malificent Maul recipe
r115 Manticore Gloves recipe
r117 Overseer Helmet recipe
r107 Sinister Ranseur recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"



    elif(place == "Swamp" or place == "swamp"):
        if(hora == "Morning"):
            if(tier == "2"):
                drops = '''
List of 📗 drops in Swamp at Morning.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Swamp at Morning.

k21 Eclipse blade
k28 Imperial Axe head
k33 Crusader Armor piece
k35 Crusader Boots part
k39 Royal Helmet fragment
k52 Demon Circlet fragment
k57 Divine Shoes part
k59 Storm Cloak part
k22 Guard's blade
k42 Royal shield part
k43 Ghost Armor part
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Swamp at Morning.

k86 Griffin Gloves part
k98 Black Morningstar part
k102 Stoneskin Cloak part
k101 Craftsman Apron part
r80 Council Boots recipe
r85 Griffin Boots recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Swamp at Morning.

k105 Doom Warglaive part
k112 Manticore Armor part
k117 Overseer Armor part
k119 Overseer Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Day"):
            if(tier == "2"):
                drops = '''
List of 📗 drops in Swamp at Day.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Swamp at Day.

k28 Imperial Axe head
k32 Lion blade
k36 Crusader Gauntlets part
k38 Royal Armor piece
k46 Ghost Gloves part
k48 Lion Helmet fragment
k59 Storm Cloak part
k22 Guard's blade
k30 Dragon Mace head
k51 Demon Robe piece
k56 Divine Circlet fragment
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Swamp at Day.

k84 Griffin Helmet part
k88 Celestial Helmet part
k102 Stoneskin Cloak part
r79 Council Helmet recipe
r99 Maiming Bulawa recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Swamp at Day.

k113 Manticore Helmet part
r121 Discarnate Robe recipe
r123 Discarnate Shoes recipe
k107 Sinister Ranseur part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Evening"):
            if(tier == "2"):
                drops = '''
List of 📗 drops in Swamp at Evening.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Swamp at Evening.

k24 Raging Lance blade
k28 Imperial Axe head
k31 Ghost blade
k47 Lion Armor part
k49 Lion Boots part
k50 Lion Gloves part
k53 Demon Shoes part
k54 Demon Bracers part
k59 Storm Cloak part
k22 Guard's blade
k55 Divine Robe piece
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Swamp at Evening.

k79 Council Helmet part
k87 Celestial Armor part
k102 Stoneskin Cloak part
r78 Council Armor recipe
r86 Griffin Gloves recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Swamp at Evening.

k110 Malificent Maul part
r108 Heartstriker Bow recipe
k113 Manticore Helmet part
k115 Manticore Gloves part
k118 Overseer Helmet part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Night"):
            if(tier == "2"):
                drops = '''
List of 📗 drops in Swamp at Night.

k07 Order Helmet fragment
k13 Hunter Boots part
k14 Hunter Gloves part
k16 Clarity Circlet fragment
k02 Trident blade
k03 Hunter shaft
k06 Order Armor piece
k15 Clarity Robe piece
k10 Order shield part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Swamp at Night.

k27 Hailstorm Bow shaft
k34 Crusader Helmet fragment
k40 Royal Boots part
k41 Royal Gauntlets part
k44 Ghost Helmet fragment
k45 Ghost Boots part
k58 Divine Bracers part
k59 Storm Cloak part
k19 Thundersoul blade
k25 Composite Bow shaft
k37 Crusader shield part
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Swamp at Night.

k78 Council Armor part
k80 Council Boots part
r87 Celestial Armor recipe
r88 Celestial Helmet recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Swamp at Night.

r111 Brutalizer Flail recipe
k112 Manticore Armor part
r122 Discarnate Circlet recipe
r119 Overseer Gauntlets recipe
r103 Poniard recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


    elif(place == "Valley" or place == "valley"):
        if(hora == "Morning"):
            if(tier == "2"):
                drops = '''
List of 📗 drops in Valley at Morning.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Valley at Morning.

r20 Doomblade Sword recipe
r22 Guard's Spear recipe
r28 Imperial Axe recipe
r33 Crusader Armor recipe
r35 Crusader Boots recipe
r39 Royal Helmet recipe
r42 Royal shield recipe
r43 Ghost Armor recipe
r52 Demon Circlet recipe
r57 Divine Shoes recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Valley at Morning.

k82 Council Shield part
k96 Meteor Bow part
k100 Assault Cape part
r89 Celestial Boots recipe
r95 Guisarme recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Valley at Morning.

r104 Lightbane Katana recipe
r124 Discarnate Bracers recipe
r112 Manticore Armor recipe
r114 Manticore Boots recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Day"):
            if(tier == "2"):
                drops = '''
List of 📗 drops in Valley at Day.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Valley at Day.

r22 Guard's Spear recipe
r28 Imperial Axe recipe
r29 Skull Crusher recipe
r32 Lion Knife recipe
r36 Crusader Gauntlets recipe
r38 Royal Armor recipe
r46 Ghost Gloves recipe
r48 Lion Helmet recipe
r51 Demon Robe recipe
r56 Divine Circlet recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Valley at Day.

r93 Phoenix Sword recipe
k81 Council Gauntlets part
k95 Guisarme part
k100 Assault Cape part
r97 Nightfall Bow recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Valley at Day.

k105 Doom Warglaive part
k108 Heartstriker Bow part
k121 Discarnate Robe part
k123 Discarnate Shoes part
r106 Decimation Harpoon recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Evening"):
            if(tier == "2"):
                drops = '''
List of 📗 drops in Valley at Evening.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Valley at Evening.

r22 Guard's Spear recipe
r23 King's Defender recipe
r28 Imperial Axe recipe
r31 Ghost dagger recipe
r47 Lion Armor recipe
r49 Lion Boots recipe
r50 Lion Gloves recipe
r53 Demon Shoes recipe
r54 Demon Bracers recipe
r55 Divine Robe recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Valley at Evening.

k83 Griffin Armor part
k97 Nightfall Bow part
k100 Assault Cape part
r82 Council Shield recipe
r96 Meteor Bow recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Valley at Evening.

r109 Windstalker Bow recipe
r120 Overseer Shield recipe
k112 Manticore Armor part
r113 Manticore Helmet recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Night"):
            if(tier == "2"):
                drops = '''
List of 📗 drops in Valley at Night.

r02 Trident recipe
r03 Hunter Bow recipe
r06 Order Armor recipe
r07 Order Helmet recipe
r10 Order shield recipe
r13 Hunter Boots recipe
r14 Hunter Gloves recipe
r15 Clarity Robe recipe
r16 Clarity Circlet recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "3"):
                drops = '''
List of 📘 drops in Valley at Night.

r19 Thundersoul Sword recipe
r25 Composite Bow recipe
r26 Lightning Bow recipe
r34 Crusader Helmet recipe
r37 Crusader shield recipe
r40 Royal Boots recipe
r41 Royal Gauntlets recipe
r44 Ghost Helmet recipe
r45 Ghost Boots recipe
r58 Divine Bracers recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "4"):
                drops = '''
List of 📙 drops in Valley at Night.

k85 Griffin Boots part
k99 Maiming Bulawa part
r84 Griffin Helmet recipe
r98 Black Morningstar recipe
r101 Craftsman Apron recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(tier == "5"):
                drops = '''
List of 📒 drops in Valley at Night.

k111 Brutalizer Flail part
k114 Manticore Boots part
k122 Discarnate Circlet part
k120 Overseer Gauntlets part
k103 Poniard part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


    return drops

def update_hero_tier(message):
    print(len(message.text.split()))
    if len(message.text.split()) == 1:
        bot.send_message(message.from_user.id,"Querido usuario porfavor especifique el tier a actualizar")
    else:
        tier = message.text.split()[1]
        if tier in lista_tiers:
            info = read_heroes()
            f = open("heroes.txt","w")
            for x in range(len(info)):
                if int(info[x].hero_user) == int(message.from_user.id):
                    info[x].update_tier(tier)
                f.write("{}-{}-{},".format(info[x].tier,info[x].hero_user,info[x].perc))
                print("Guardando heroe con tier {} , id {} y perc {}".format(info[x].tier,info[x].hero_user,info[x].perc))
            f.close()
            bot.send_message(message.from_user.id,"He actualizado tu tier. De ahora en adelante te mostrare drops de tier {}".format(tier))
        else:
            bot.send_message(message.from_user.id,"Querido usuario, {} no es un tier valido".format(tier))

def update_hero_perception(message):
    print(len(message.text.split()))
    if len(message.text.split()) == 1:
        bot.send_message(message.from_user.id,"Querido usuario porfavor especifique el perception a actualizar")
    else:
        perc = message.text.split()[1]
        if perc in lista_tiers or perc == "0":
            info = read_heroes()
            f = open("heroes.txt","w")
            for x in range(len(info)):
                if int(info[x].hero_user) == int(message.from_user.id):
                    info[x].update_perc(perc)
                f.write("{}-{}-{},".format(info[x].tier,info[x].hero_user,info[x].perc))
                print("Guardando heroe con tier {} , id {} y perc {}".format(info[x].tier,info[x].hero_user,info[x].perc))
            f.close()
            bot.send_message(message.from_user.id,"He actualizado tu perception. De ahora en adelante te mostrare drops de perception {}".format(perc))
        else:
            bot.send_message(message.from_user.id,"Querido usuario, {} no es un perception valido".format(perc))
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def FacilitarDropsRsc(place, time):
    time = time.split()
    hora = time[0]
    tRemaining = reformtRemaining(time[1])
    drops = ""

    if(place == "Forest" or place =="forest"):
        if(hora == "Morning"):
            drops = '''
List of 📦 drops in Forest at Morning.

01 Thread
02 Stick
03 Pelt
03 Bone
06 Coal
09 Cloth
07 Powder
10 Silver ore
21 Bone powder
31 Rope

⚠️ High Level Required ⚠️

11 Bauxite
33 Metal plate
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Day"):
            drops = '''
List of 📦 drops in Forest at Day.

01 Thread
03 Pelt
04 Bone
07 Powder
09 Cloth
20 Leather
22 String
23 Coke

⚠️ High level required ⚠️

11 Bauxite
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Evening"):
            drops = '''
List of 📦 drops in Forest at Evening.

01 Thread
02 Stick
03 Pelt
04 Bone
05 Coal
07 Powder
09 Cloth
20 Leather
21 Bone powder
22 String
23 Coke
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Night"):
            drops = '''
List of 📦 drops in Forest at Night.

01 Thread
02 Stick
03 Pelt
05 Coal
06 Charcoal
07 Powder
08 Iron ore
13 Magic stone
22 String
23 Coke
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

    elif(place == "Swamp" or place == "swamp"):
        if(hora == "Morning"):
            drops = '''
List of 📦 drops in Swamp at Morning.

03 Pelt
09 Cloth
13 Magic stone
16 Solvent
20 Leather
21 Bone powder
22 String
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Day"):
            drops = '''
List of 📦 drops in Swamp at Day.

03 Pelt
07 Powder
10 Silver ore
16 Solvent
20 Leather
21 Bone powder
22 String
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Evening"):
            drops = '''
List of 📦 drops in Swamp at Evening.

02 Pelt
07 Powder
09 Cloth
10 Silver ore
16 Solvent
20 Leather

⚠️ High level required ⚠️

11 Bauxite
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Night"):
            drops = '''
List of 📦 drops in Swamp at Night.

01 Thread
03 Pelt
07 Powder
13 Magic stone
18 Hardener
20 Leather
21 Bone powder
23 Coke

⚠️ High level required ⚠️

11 Bauxite
33 Metal Plate
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

    elif(place == "Valley" or place == "valley" ):
        if(hora == "Morning"):
            drops = '''
List of 📦 drops in Valley at Morning.

05 Coal
07 Powder
10 Silver ore
13 Magic stone
21 Bone powder
22 String
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Day"):
            drops = '''
List of 📦 drops in Valley at Day.

05 Coal
07 Powder
10 Silver ore
13 Magic stone
15 Sapphire
20 Leather
21 Bone powder
22 String
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Evening"):
            drops = '''
List of 📦 drops in Valley at Evening.

07 Powder
10 Silver ore
13 Magic stone
15 Sapphire
21 Bone powder
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Night"):
            drops = '''
List of 📦 drops in Valley at Night.

04 Bone
06 Charcoal
07 Powder
08 Iron ore
10 Silver ore
13 Magic stone
17 Ruby
23 Coke

⚠️ High level required ⚠️

33 Metal Plate
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

    return drops

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def FacilitarDropsHerbs(place, time):
    time = time.split()
    hora = time[0]
    tRemaining = reformtRemaining(time[1])
    drops = ""

    if(place == "Forest" or place =="forest"):
        if(hora == "Morning"):
            drops = '''
List of 🌱 drops in Forest at Morning.

🌱 Stinky sumac
🌱 Cliff rue
🌱 Love Creeper
🌱 Ilaves
🌱 Ephijora
🌱Ash Rosemary
🌱Sun Tarragon
🌱Queen's pepper
🌱 Astrulic
🌱 Flammia nut

''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Day"):
            drops = '''
List of 🌱 drops in Forest at Day.

🌱 Stinky sumac
🌱 Cliff rue
🌱 Love Creeper
🌱 Ilaves
🌱 Ephijora
🌱Ash Rosemary
🌱Sun Tarragon
🌱Queen's pepper
🌱 Astrulic
🌱 Flammia nut
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Evening"):
            drops = '''
List of 🌱 drops in Forest at Evening.

🌱 Stinky sumac
🌱 Cliff rue
🌱 Love Creeper
🌱 Wolf Root
🌱 Ilaves
🌱 Ephijora
🌱 Sanguine Parsley
🌱 Ash Rosemary
🌱 Sun Tarragon
🌱 Astrulic
🌱 Flammia nut
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
        elif(hora == "Night"):
            drops = '''
List of 🌱 drops in Forest at Night.

🌱 Mercy Saasafras
🌱 Swamp Lavender
🌱 White Blossom
🌱 Cave Garlic
🌱 Yellow Seed
🌱 Tecceagrass
🌱 Spring Bay leaf
🌱 Maccunut
🌱 Dragon Seed
🌱 Plexisop
🌱 Mammoth Dill
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

    elif(place == "Swamp" or place == "swamp"):
        if(hora == "Morning"):
            drops = '''
List of 🌱 drops in Swamp at Morning.

🌱 Stinky sumac
🌱 Cliff rue
🌱 Love crepper
🌱 Wolf Root
🌱 Ilaves
🌱 Ephijora
🌱 Ash Rosemary
🌱 Sanguine Parsley
🌱 Queen's pepper
🌱 Astrulic
🌱 Flammia nut
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Day"):
            drops = '''
List of 🌱 drops in Swamp at Day.

🌱 Stinky sumac
🌱 Cliff rue
🌱 Wolf Root
🌱 Ephijora
🌱 Ash Rosemary
🌱 Sanguine Parsley
🌱 Sun Tarragon
🌱 Queen's pepper
🌱 Astrulic
🌱 Flammia nut
🌱 Stinky sumac
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Evening"):
            drops = '''
List of 🌱 drops in Swamp at Evening.

🌱 Stinky sumac
🌱 Cliff rue
🌱 llaves
🌱 Ephijora
🌱 Ash Rosemary
🌱 Sanguine Parsley
🌱 Sun Tarragon
🌱 Queen's pepper
🌱 Astrulic
🌱 Flammia nut

''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Night"):
            drops = '''
List of 🌱 drops in Swamp at Night.

🌱 Mercy Saasafras
🌱 Swamp Lavender
🌱 White Blossom
🌱 Storm Hyssop
🌱 Cave Garlic
🌱 Yellow Seed
🌱 Tecceagrass
🌱 Spring Bay leaf
🌱 Maccunut
🌱 Dragon Seed
🌱 Plexisop
🌱 Mammoth Dill

''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

    elif(place == "Valley" or place == "valley" ):
        if(hora == "Morning"):
            drops = '''
List of 🌱 drops in Valley at Morning.

🌱 Stinky sumac
🌱 Cliff rue
🌱 Wolf Root
🌱 Ilaves
🌱 Ephijora
🌱 Sanguine Parsley
🌱 Sun Tarragon
🌱 Queen's pepper
🌱 Astrulic
🌱 Flammia nut
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Day"):
            drops = '''
List of 🌱 drops in Valley at Day.

🌱 Cliff rue
🌱 Love crepper
🌱 Wolf Root
🌱 Ephijora
🌱 Ash Rosemary
🌱 Sun Tarragon
🌱 Queen's pepper
🌱 Astrulic
🌱 Flammia nut
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Evening"):
            drops = '''
List of 🌱 drops in Valley at Evening.

🌱 Stinky sumac
🌱 Cliff rue
🌱 Love crepper
🌱 Wolf Root
🌱 Ephijora
🌱 Ash Rosemary
🌱 Sanguine Parsley
🌱 Sun Tarragon
🌱 Astrulic
🌱 Flammia nut
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

        elif(hora == "Night"):
            drops = '''
List of 🌱 drops in Valley at Night.

🌱 Mercy Saasafras
🌱 Swamp Lavender
🌱 White Blossom
🌱 Storm Hyssop
🌱 Cave Garlic
🌱 Yellow Seed
🌱 Tecceagrass
🌱 Spring Bay leaf
🌱 Maccunut
🌱 Dragon Seed
🌱 Plexisop
🌱 Mammoth Dill
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

    return drops


def FacilitarDropsColls(place, time, perception):
    time = time.split()
    hora = time[0]
    tRemaining = reformtRemaining(time[1])
    drops = ""

    if(place == "Forest" or place == "forest"):
        if(hora == "Morning"):
            if(perception == "1"):
                drops = "Lo lamento humano(lies) No hay drops para tu nivel de perception actual en Forest."
            elif(perception == "2"):
                drops = "Lo lamento humano(lies) No hay drops para tu nivel de perception actual en Forest."
            elif(perception == "3"):
                drops = '''
List of 📘 drops in Forest at Morning.

k20 Doomblade blade
r21 Eclipse recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(perception == "4"):
                drops = '''
List of 📙 drops in Forest at Morning.

k93 Phoenix Sword part
r81 Council Gauntlets recipe
r91 Griffin Knife recipe
r100 Assault Cape recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(perception == "5"):
                drops = '''
List of 📙 drops in Forest at Morning.

k93 Phoenix Sword part
r81 Council Gauntlets recipe
r91 Griffin Knife recipe
r100 Assault Cape recipe

List of 📒 drops in Forest at Morning.

k104 Lightbane Katana part
k124 Discarnate Bracers part
k112 Manticore Armor part
k114 Manticore Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

            elif(perception == "6"):
                drops = '''
List of 📒 drops in Forest at Morning.

k104 Lightbane Katana part
k124 Discarnate Bracers part
k112 Manticore Armor part
k114 Manticore Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"



        elif(hora == "Day"):
            if(perception == "1"):
                drops = "Lo lamento humano(lies) No hay drops para tu nivel de perception actual en Forest."
            elif(perception == "2"):
                drops = "Lo lamento humano(lies) No hay drops para tu nivel de perception actual en Forest."
            elif(perception == "3"):
                drops = '''
List of 📘 drops in Forest at Day.

k23 King's Defender blade
r24 Raging Lance recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(perception == "4"):
                drops = '''
List of 📙 drops in Forest at Day.

k89 Celestial Boots part
k91 Griffin Knife part
k101 Craftsman Apron part
r94 Heavy Fauchard recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(perception == "5"):
                drops = '''
List of 📙 drops in Forest at Day.

k89 Celestial Boots part
k91 Griffin Knife part
k101 Craftsman Apron part
r94 Heavy Fauchard recipe

List of 📒 drops in Forest at Day.

r105 Doom Warglaive recipe
k116 Overseer Shield part
k115 Manticore Gloves part
r116 Overseer Armor recipe
r118 Overseer Boots recipe
k106 Decimation Harpoon part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

            elif(perception == "6"):
                drops = '''
List of 📒 drops in Forest at Day.

r105 Doom Warglaive recipe
k116 Overseer Shield part
k115 Manticore Gloves part
r116 Overseer Armor recipe
r118 Overseer Boots recipe
k106 Decimation Harpoon part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"



        elif(hora == "Evening"):
            if(perception == "1"):
                drops = "Lo lamento humano(lies) No hay drops para tu nivel de perception actual en Forest."
            elif(perception == "2"):
                drops = "Lo lamento humano(lies) No hay drops para tu nivel de perception actual en Forest."
            elif(perception == "3"):
                drops = '''
List of 📘 drops in Forest at Evening.

k26 Lightning Bow shaft
r27 Hailstorm Bow recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Forest at Evening.

k94 Heavy Fauchard part
r90 Celestial Bracers recipe
r92 Minotaur Sword recipe
r102 Stoneskin Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "5"):
                drops = '''
List of 📙 drops in Forest at Evening.

k94 Heavy Fauchard part
r90 Celestial Bracers recipe
r92 Minotaur Sword recipe
r102 Stoneskin Cloak recipe

List of 📒 drops in Forest at Evening.

k109 Windstalker Bow part
k116 Overseer Shield part
k113 Manticore Helmet part
k114 Manticore Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "6"):
                drops = '''
List of 📒 drops in Forest at Evening.

k109 Windstalker Bow part
k116 Overseer Shield part
k113 Manticore Helmet part
k114 Manticore Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"



        elif(hora == "Night"):
            if(perception == "1"):
                drops = "Lo lamento humano(lies) No hay drops para tu nivel de perception actual en Forest."
            elif(perception == "2"):
                drops = "Lo lamento humano(lies) No hay drops para tu nivel de perception actual en Forest."
            elif(perception == "3"):
                drops = '''
List of 📘 drops in Forest at Night.

k29 Skull Crusher head
r30 Dragon Mace recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Forest at Night.

k90 Celestial Bracers part
k92 Minotaur Sword part
r83 Griffin Armor recipe
r102 Stoneskin Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "5"):
                drops = '''
List of 📙 drops in Forest at Night.

k90 Celestial Bracers part
k92 Minotaur Sword part
r83 Griffin Armor recipe
r102 Stoneskin Cloak recipe

List of 📒 drops in Forest at Night.

k104 Lightbane Katana part
r110 Malificent Maul recipe
r115 Manticore Gloves recipe
r117 Overseer Helmet recipe
r107 Sinister Ranseur recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

            elif(perception == "6"):
                drops = '''
List of 📒 drops in Forest at Night.

k104 Lightbane Katana part
r110 Malificent Maul recipe
r115 Manticore Gloves recipe
r117 Overseer Helmet recipe
r107 Sinister Ranseur recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"



    elif(place == "Swamp" or place == "swamp"):
        if(hora == "Morning"):
            if(perception == "1"):
                drops = '''
List of 📗 drops in Swamp at Morning.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "2"):
                drops = '''
List of 📗 drops in Swamp at Morning.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part

List of 📘 drops in Swamp at Morning.

k28 Imperial Axe head
k59 Storm Cloak part
k22 Guard's blade
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "3"):
                drops = '''
List of 📘 drops in Swamp at Morning.

k21 Eclipse blade
k28 Imperial Axe head
k33 Crusader Armor piece
k35 Crusader Boots part
k39 Royal Helmet fragment
k52 Demon Circlet fragment
k57 Divine Shoes part
k59 Storm Cloak part
k22 Guard's blade
k42 Royal shield part
k43 Ghost Armor part
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Swamp at Morning.

k86 Griffin Gloves part
k98 Black Morningstar part
k102 Stoneskin Cloak part
k101 Craftsman Apron part
r80 Council Boots recipe
r85 Griffin Boots recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "5"):
                drops = '''
List of 📙 drops in Swamp at Morning.

k86 Griffin Gloves part
k98 Black Morningstar part
k102 Stoneskin Cloak part
k101 Craftsman Apron part
r80 Council Boots recipe
r85 Griffin Boots recipe

List of 📒 drops in Swamp at Morning.

k105 Doom Warglaive part
k112 Manticore Armor part
k117 Overseer Armor part
k119 Overseer Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "6"):
                drops = '''
List of 📒 drops in Swamp at Morning.

k105 Doom Warglaive part
k112 Manticore Armor part
k117 Overseer Armor part
k119 Overseer Boots part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


        elif(hora == "Day"):
            if(perception == "1"):
                drops = '''
List of 📗 drops in Swamp at Day.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "2"):
                drops = '''
List of 📗 drops in Swamp at Day.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part

List of 📘 drops in Swamp at Day.

k28 Imperial Axe head
k59 Storm Cloak part
k22 Guard's blade
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "3"):
                drops = '''
List of 📘 drops in Swamp at Day.

k28 Imperial Axe head
k32 Lion blade
k36 Crusader Gauntlets part
k38 Royal Armor piece
k46 Ghost Gloves part
k48 Lion Helmet fragment
k59 Storm Cloak part
k22 Guard's blade
k30 Dragon Mace head
k51 Demon Robe piece
k56 Divine Circlet fragment
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Swamp at Day.

k84 Griffin Helmet part
k88 Celestial Helmet part
k102 Stoneskin Cloak part
r79 Council Helmet recipe
r99 Maiming Bulawa recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "5"):
                drops = '''
List of 📙 drops in Swamp at Day.

k84 Griffin Helmet part
k88 Celestial Helmet part
k102 Stoneskin Cloak part
r79 Council Helmet recipe
r99 Maiming Bulawa recipe

List of 📒 drops in Swamp at Day.

k113 Manticore Helmet part
r121 Discarnate Robe recipe
r123 Discarnate Shoes recipe
k107 Sinister Ranseur part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "6"):
                drops = '''
List of 📒 drops in Swamp at Day.

k113 Manticore Helmet part
r121 Discarnate Robe recipe
r123 Discarnate Shoes recipe
k107 Sinister Ranseur part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"



        elif(hora == "Evening"):
            if(perception == "1"):
                drops = '''
List of 📗 drops in Swamp at Evening.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "2"):
                drops = '''
List of 📗 drops in Swamp at Evening.

k01 Champion blade
k05 Hunter blade
k12 Hunter Helmet fragment
k17 Clarity Shoes part
k18 Clarity Bracers part
k04 War hammer head
k08 Order Boots part
k09 Order Gauntlets part
k11 Hunter Armor part

List of 📘 drops in Swamp at Evening.

k28 Imperial Axe head
k59 Storm Cloak part
k22 Guard's blade
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "3"):
                drops = '''
List of 📘 drops in Swamp at Evening.

k24 Raging Lance blade
k28 Imperial Axe head
k31 Ghost blade
k47 Lion Armor part
k49 Lion Boots part
k50 Lion Gloves part
k53 Demon Shoes part
k54 Demon Bracers part
k59 Storm Cloak part
k22 Guard's blade
k55 Divine Robe piece
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Swamp at Evening.

k79 Council Helmet part
k87 Celestial Armor part
k102 Stoneskin Cloak part
r78 Council Armor recipe
r86 Griffin Gloves recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "5"):
                drops = '''
List of 📙 drops in Swamp at Evening.

k79 Council Helmet part
k87 Celestial Armor part
k102 Stoneskin Cloak part
r78 Council Armor recipe
r86 Griffin Gloves recipe

List of 📒 drops in Swamp at Evening.

k110 Malificent Maul part
r108 Heartstriker Bow recipe
k113 Manticore Helmet part
k115 Manticore Gloves part
k118 Overseer Helmet part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "6"):
                drops = '''
List of 📒 drops in Swamp at Evening.

k110 Malificent Maul part
r108 Heartstriker Bow recipe
k113 Manticore Helmet part
k115 Manticore Gloves part
k118 Overseer Helmet part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"




        elif(hora == "Night"):
            if(perception == "1"):
                drops = '''
List of 📗 drops in Swamp at Night.

k07 Order Helmet fragment
k13 Hunter Boots part
k14 Hunter Gloves part
k16 Clarity Circlet fragment
k02 Trident blade
k03 Hunter shaft
k06 Order Armor piece
k15 Clarity Robe piece
k10 Order shield part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "2"):
                drops = '''
List of 📗 drops in Swamp at Night.

k07 Order Helmet fragment
k13 Hunter Boots part
k14 Hunter Gloves part
k16 Clarity Circlet fragment
k02 Trident blade
k03 Hunter shaft
k06 Order Armor piece
k15 Clarity Robe piece
k10 Order shield part

List of 📘 drops in Swamp at Night.

k59 Storm Cloak part
k19 Thundersoul blade
k25 Composite Bow shaft
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "3"):
                drops = '''
List of 📘 drops in Swamp at Night.

k27 Hailstorm Bow shaft
k34 Crusader Helmet fragment
k40 Royal Boots part
k41 Royal Gauntlets part
k44 Ghost Helmet fragment
k45 Ghost Boots part
k58 Divine Bracers part
k59 Storm Cloak part
k19 Thundersoul blade
k25 Composite Bow shaft
k37 Crusader shield part
k60 Durable Cloak part
k61 Blessed Cloak part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Swamp at Night.

k78 Council Armor part
k80 Council Boots part
r87 Celestial Armor recipe
r88 Celestial Helmet recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

            elif(perception == "5"):
                drops = '''
List of 📙 drops in Swamp at Night.

k78 Council Armor part
k80 Council Boots part
r87 Celestial Armor recipe
r88 Celestial Helmet recipe

List of 📒 drops in Swamp at Night.

r111 Brutalizer Flail recipe
k112 Manticore Armor part
r122 Discarnate Circlet recipe
r119 Overseer Gauntlets recipe
r103 Poniard recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

            elif(perception == "6"):
                drops = '''
List of 📒 drops in Swamp at Night.

r111 Brutalizer Flail recipe
k112 Manticore Armor part
r122 Discarnate Circlet recipe
r119 Overseer Gauntlets recipe
r103 Poniard recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"





    elif(place == "Valley" or place == "valley"):
        if(hora == "Morning"):
            if(perception == "1"):
                drops = '''
List of 📗 drops in Valley at Morning.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "2"):
                drops = '''
List of 📗 drops in Valley at Morning.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe

List of 📘 drops in Valley at Morning.

r22 Guard's Spear recipe
r28 Imperial Axe recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "3"):
                drops = '''
List of 📘 drops in Valley at Morning.

r20 Doomblade Sword recipe
r22 Guard's Spear recipe
r28 Imperial Axe recipe
r33 Crusader Armor recipe
r35 Crusader Boots recipe
r39 Royal Helmet recipe
r42 Royal shield recipe
r43 Ghost Armor recipe
r52 Demon Circlet recipe
r57 Divine Shoes recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Valley at Morning.

k82 Council Shield part
k96 Meteor Bow part
k100 Assault Cape part
r89 Celestial Boots recipe
r95 Guisarme recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

            elif(perception == "5"):
                drops = '''
List of 📙 drops in Valley at Morning.

k82 Council Shield part
k96 Meteor Bow part
k100 Assault Cape part
r89 Celestial Boots recipe
r95 Guisarme recipe

List of 📒 drops in Valley at Morning.

r104 Lightbane Katana recipe
r124 Discarnate Bracers recipe
r112 Manticore Armor recipe
r114 Manticore Boots recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"

            elif(perception == "6"):
                drops = '''
List of 📒 drops in Valley at Morning.

r104 Lightbane Katana recipe
r124 Discarnate Bracers recipe
r112 Manticore Armor recipe
r114 Manticore Boots recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"



        elif(hora == "Day"):
            if(perception == "1"):
                drops = '''
List of 📗 drops in Valley at Day.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(perception == "2"):
                drops = '''
List of 📗 drops in Valley at Day.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe

List of 📘 drops in Valley at Day.

r22 Guard's Spear recipe
r28 Imperial Axe recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "3"):
                drops = '''
List of 📘 drops in Valley at Day.

r22 Guard's Spear recipe
r28 Imperial Axe recipe
r29 Skull Crusher recipe
r32 Lion Knife recipe
r36 Crusader Gauntlets recipe
r38 Royal Armor recipe
r46 Ghost Gloves recipe
r48 Lion Helmet recipe
r51 Demon Robe recipe
r56 Divine Circlet recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Valley at Day.

r93 Phoenix Sword recipe
k81 Council Gauntlets part
k95 Guisarme part
k100 Assault Cape part
r97 Nightfall Bow recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "5"):
                drops = '''
List of 📙 drops in Valley at Day.

r93 Phoenix Sword recipe
k81 Council Gauntlets part
k95 Guisarme part
k100 Assault Cape part
r97 Nightfall Bow recipe

List of 📒 drops in Valley at Day.

k105 Doom Warglaive part
k108 Heartstriker Bow part
k121 Discarnate Robe part
k123 Discarnate Shoes part
r106 Decimation Harpoon recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "6"):
                drops = '''
List of 📒 drops in Valley at Day.

k105 Doom Warglaive part
k108 Heartstriker Bow part
k121 Discarnate Robe part
k123 Discarnate Shoes part
r106 Decimation Harpoon recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"




        elif(hora == "Evening"):
            if(perception == "1"):
                drops = '''
List of 📗 drops in Valley at Evening.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(perception == "2"):
                drops = '''
List of 📗 drops in Valley at Evening.

r01 Champion Sword recipe
r04 War hammer recipe
r05 Hunter Dagger recipe
r08 Order Boots recipe
r09 Order Gauntlets recipe
r11 Hunter Armor recipe
r12 Hunter Helmet recipe
r17 Clarity Shoes recipe
r18 Clarity Bracers recipe

List of 📘 drops in Valley at Evening.

r22 Guard's Spear recipe
r28 Imperial Axe recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "3"):
                drops = '''
List of 📘 drops in Valley at Evening.

r22 Guard's Spear recipe
r23 King's Defender recipe
r28 Imperial Axe recipe
r31 Ghost dagger recipe
r47 Lion Armor recipe
r49 Lion Boots recipe
r50 Lion Gloves recipe
r53 Demon Shoes recipe
r54 Demon Bracers recipe
r55 Divine Robe recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Valley at Evening.

k83 Griffin Armor part
k97 Nightfall Bow part
k100 Assault Cape part
r82 Council Shield recipe
r96 Meteor Bow recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "5"):
                drops = '''
List of 📙 drops in Valley at Evening.

k83 Griffin Armor part
k97 Nightfall Bow part
k100 Assault Cape part
r82 Council Shield recipe
r96 Meteor Bow recipe

List of 📒 drops in Valley at Evening.

r109 Windstalker Bow recipe
r120 Overseer Shield recipe
k112 Manticore Armor part
r113 Manticore Helmet recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "6"):
                drops = '''
List of 📒 drops in Valley at Evening.

r109 Windstalker Bow recipe
r120 Overseer Shield recipe
k112 Manticore Armor part
r113 Manticore Helmet recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"




        elif(hora == "Night"):
            if(perception == "1"):
                drops = '''
List of 📗 drops in Valley at Night.

r02 Trident recipe
r03 Hunter Bow recipe
r06 Order Armor recipe
r07 Order Helmet recipe
r10 Order shield recipe
r13 Hunter Boots recipe
r14 Hunter Gloves recipe
r15 Clarity Robe recipe
r16 Clarity Circlet recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"
            elif(perception == "2"):
                drops = '''
List of 📗 drops in Valley at Night.

r02 Trident recipe
r03 Hunter Bow recipe
r06 Order Armor recipe
r07 Order Helmet recipe
r10 Order shield recipe
r13 Hunter Boots recipe
r14 Hunter Gloves recipe
r15 Clarity Robe recipe
r16 Clarity Circlet recipe

List of 📘 drops in Valley at Night.

r19 Thundersoul Sword recipe
r25 Composite Bow recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "3"):
                drops = '''
List of 📘 drops in Valley at Night.

r19 Thundersoul Sword recipe
r25 Composite Bow recipe
r26 Lightning Bow recipe
r34 Crusader Helmet recipe
r37 Crusader shield recipe
r40 Royal Boots recipe
r41 Royal Gauntlets recipe
r44 Ghost Helmet recipe
r45 Ghost Boots recipe
r58 Divine Bracers recipe
r59 Storm Cloak recipe
r60 Durable Cloak recipe
r61 Blessed Cloak recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "4"):
                drops = '''
List of 📙 drops in Valley at Night.

k85 Griffin Boots part
k99 Maiming Bulawa part
r84 Griffin Helmet recipe
r98 Black Morningstar recipe
r101 Craftsman Apron recipe
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "5"):
                drops = '''
List of 📙 drops in Valley at Night.

k85 Griffin Boots part
k99 Maiming Bulawa part
r84 Griffin Helmet recipe
r98 Black Morningstar recipe
r101 Craftsman Apron recipe

List of 📒 drops in Valley at Night.

k111 Brutalizer Flail part
k114 Manticore Boots part
k122 Discarnate Circlet part
k120 Overseer Gauntlets part
k103 Poniard part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


            elif(perception == "6"):
                drops = '''
List of 📒 drops in Valley at Night.

k111 Brutalizer Flail part
k114 Manticore Boots part
k122 Discarnate Circlet part
k120 Overseer Gauntlets part
k103 Poniard part
''' + "\n⚠Tiempo restante: " + tRemaining + "⚠"


    return drops
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Creando botonera basica
markup = types.ReplyKeyboardMarkup(row_width=2)
helpButton = types.KeyboardButton('Ayuda')
startButton = types.KeyboardButton('Start')
usersButton = types.KeyboardButton('Usuarios')
feedbackButton = types.KeyboardButton('Feedback')
markup.add(startButton, helpButton, usersButton ,feedbackButton)

#Creando botonera de ayuda

botonera_de_ayuda = types.ReplyKeyboardMarkup(row_width=2)
comandosButton = types.KeyboardButton('Comandos disponibles')
howToButton = types.KeyboardButton('Como usar cada comando')
backButton = types.KeyboardButton('Volver al inicio')
botonera_de_ayuda.add(comandosButton,howToButton,backButton)

#Creando botonera de howtos

botonera_de_howtos = types.ReplyKeyboardMarkup(row_width=3)
forestHTButton = types.KeyboardButton('Comando forest')
swampHTButton = types.KeyboardButton('Comando swamp')
valleyHTButton = types.KeyboardButton('Comando valley')
saveHTButton = types.KeyboardButton('Comando save_me')
hideHTButton = types.KeyboardButton('Comando hide')
ghideHTButton = types.KeyboardButton('Comando g_hide')
updateHTButton = types.KeyboardButton('Comando update_me')
workHTButton = types.KeyboardButton('Comando work')
feedbackHTButton = types.KeyboardButton('Comando feedback')
stockHTButton = types.KeyboardButton('Comando stock')
updatePercHTButton = types.KeyboardButton('Comando update_perc')
botonera_de_howtos.add(forestHTButton,swampHTButton,valleyHTButton,saveHTButton,hideHTButton,ghideHTButton,updateHTButton,workHTButton,feedbackHTButton,stockHTButton,updatePercHTButton,backButton)

#Handlers para comandos
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type != "group":
         bot.reply_to(message, "Hola! Bienvenido al bot para esconder recursos de forma rapida!" , reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Yo! Enviame el /g_stock_res para aca y te dare los withdraws de forma automatica, te parece?" , reply_markup=markup)


@bot.message_handler(commands=['stop'])
def stop_keyboard(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Done", reply_markup=markup)

@bot.message_handler(commands=['feedback'])
def send_feed(message):
   msg = message.text
   msg = msg.replace("/feedback","@" + message.from_user.username + " dice que")
   bot.send_message(usuarito, msg)
   print("Le dije a Gow que " + msg)
   bot.send_message(1157196238, msg)
   print("Le dije a Darwer que " + msg)

@bot.message_handler(commands=['hide'])
def hide_items(message):
    if message.from_user.id in listaPermitidos:
        hideShit(message.from_user.id , message.text)
    else:
        bot.send_message(usuarito, "Me escribio el usuario @{}".format(message.from_user.username))

@bot.message_handler(commands=['g_hide'])
def deposit_items(message):
   if message.from_user.id in listaPermitidos:
       hideShitonGuild(message.from_user.id , message.text)
   else:
       bot.send_message(usuarito, "Me escribio el usuario @{}".format(message.from_user.username))

@bot.message_handler(commands=['work'])
def workOnChat(message):
    try:
        mensaje = message.reply_to_message.text
    except:
        mensaje = "" #Provisional
        pass
    if("Guild Warehouse" in mensaje and message.chat.id in listaGruposPermitidos):
        pincha_grupo(mensaje,message.chat.id,message.chat.id,message)
    if(message.chat.id not in listaGruposPermitidos):
        bot.send_message(usuarito,"Me escribieron en un grupo pero di ban :v, el usuario que me escribio fue {name}".format(name = message.from_user.username))

@bot.message_handler(commands=['save_me'])
def handle_hero(message):
    save_hero(message)

@bot.message_handler(commands=['update_me'])
def udpate_hero_on_tier(message):
    update_hero_tier(message)

@bot.message_handler(commands=['save_perc'])
def save_hero_perc(message):
    update_hero_tier(message)

@bot.message_handler(commands=['update_perc'])
def udpate_hero_on_perc(message):
    update_hero_perception(message)

@bot.message_handler(commands=['forest'])
def show_forest(message):
    error = False
    perc = search_hero_perc(message)
    print("Encontrado la perc {}".format(perc))
    print("Mensaje : {}".format(message.text.split()))
    print("Len : {}".format(len(message.text.split())))
    if len(message.text.split())== 2:
        if message.text.split()[1] == "r":
            drops = FacilitarDropsRsc("forest",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        if message.text.split()[1] == "h":
            drops = FacilitarDropsHerbs("forest",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        if message.text.split()[1] == "all":
            drops = FacilitarDropsRsc("forest",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
            drops = FacilitarDropsHerbs("forest",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
            try:
                tier = search_hero_tier(message)
            except:
                error = True
                bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")
            if tier not in lista_tiers:
                error = True
            if error == False:
                print("Encontrada la perception {}".format(perc))
                if perc == "0":
                    drops = FacilitarDrops("forest",GetCWTime(),tier)
                if perc in lista_tiers and perc != 0:
                    drops = FacilitarDropsColls("forest",GetCWTime(),perc)
                print("/////////////////////////////////////////////////////////////////////////// DROPS ////////////////////////////////////////////////////////////")
                print(drops)
                if (drops != ""):
                    bot.send_message(message.from_user.id,drops)
                else:
                    bot.send_message(message.from_user.id,"No he encontrado drops de piezas para ti, porfavor especifica tu tier o puede que no tengas drops en esta quest para tu tier.")
            else:
                 bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")
        if message.text.split()[1] != "h" and message.text.split()[1] != "r" and message.text.split()[1] != "all":
            bot.send_message(message.from_user.id,"Querido usuario, no estas usando mi comando bien, porfavor revisa la ayuda")
    else:
        try:
            tier = search_hero_tier(message)
        except:
            error = True
            bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")
        if tier not in lista_tiers:
            error = True
        if error == False:
            print("Encontrada la perception {}".format(perc))
            if perc == "0":
                drops = FacilitarDrops("forest",GetCWTime(),tier)
            if perc in lista_tiers and perc != 0:
                drops = FacilitarDropsColls("forest",GetCWTime(),perc)
            print("/////////////////////////////////////////////////////////////////////////// DROPS ////////////////////////////////////////////////////////////")
            print(drops)
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        else:
            bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")

@bot.message_handler(commands=['swamp'])
def show_swamp(message):
    error = False
    perc = search_hero_perc(message)
    print("Mensaje : {}".format(message.text.split()))
    print("Len : {}".format(len(message.text.split())))
    if len(message.text.split())== 2:
        if message.text.split()[1] == "r":
            drops = FacilitarDropsRsc("swamp",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        if message.text.split()[1] == "h":
            drops = FacilitarDropsHerbs("swamp",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        if message.text.split()[1] == "all":
            drops = FacilitarDropsRsc("swamp",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
            drops = FacilitarDropsHerbs("swamp",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
            try:
                tier = search_hero_tier(message)
            except:
                error = True
                bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")
            if tier not in lista_tiers:
                error = True
            if error == False:
                if perc == "0":
                    drops = FacilitarDrops("swamp",GetCWTime(),tier)
                if perc in lista_tiers:
                    drops = FacilitarDropsColls("swamp",GetCWTime(),perc)
                print("/////////////////////////////////////////////////////////////////////////// DROPS ////////////////////////////////////////////////////////////")
                print(drops)
                if (drops != ""):
                    bot.send_message(message.from_user.id,drops)
                else:
                    bot.send_message(message.from_user.id,"No he encontrado drops de piezas para ti, porfavor especifica tu tier o puede que no tengas drops en esta quest para tu tier.")
        if message.text.split()[1] != "h" and message.text.split()[1] != "r" and message.text.split()[1] != "all":
            bot.send_message(message.from_user.id,"Querido usuario, no estas usando mi comando bien, porfavor revisa la ayuda")
    else:
        try:
            tier = search_hero_tier(message)
            perc = search_hero_perc(message)
        except:
            error = True
            bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")
        if tier not in lista_tiers:
            error = True
        if error == False:
            if perc == "0":
                drops = FacilitarDrops("swamp",GetCWTime(),tier)
            if perc in lista_tiers:
                drops = FacilitarDropsColls("swamp",GetCWTime(),perc)
            print("/////////////////////////////////////////////////////////////////////////// DROPS ////////////////////////////////////////////////////////////")
            print(drops)
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        else:
            bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")

@bot.message_handler(commands=['valley'])
def show_valley(message):
    error = False
    perc = search_hero_perc(message)
    print("Mensaje : {}".format(message.text.split()))
    print("Len : {}".format(len(message.text.split())))
    if len(message.text.split())== 2:
        if message.text.split()[1] == "r":
            drops = FacilitarDropsRsc("valley",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        if message.text.split()[1] == "h":
            drops = FacilitarDropsHerbs("valley",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        if message.text.split()[1] == "all":
            drops = FacilitarDropsRsc("valley",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
            drops = FacilitarDropsHerbs("valley",GetCWTime())
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
            try:
                tier = search_hero_tier(message)
            except:
                error = True
                bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")
            if tier not in lista_tiers:
                error = True
            if error == False:
                if perc == "0":
                    drops = FacilitarDrops("valley",GetCWTime(),tier)
                if perc in lista_tiers:
                    drops = FacilitarDropsColls("valley",GetCWTime(),perc)
                print("/////////////////////////////////////////////////////////////////////////// DROPS ////////////////////////////////////////////////////////////")
                print(drops)
                if (drops != ""):
                    bot.send_message(message.from_user.id,drops)
                else:
                    bot.send_message(message.from_user.id,"No he encontrado drops de piezas para ti, porfavor especifica tu tier o puede que no tengas drops en esta quest para tu tier.")
        if message.text.split()[1] != "h" and message.text.split()[1] != "r" and message.text.split()[1] != "all":
            bot.send_message(message.from_user.id,"Querido usuario, no estas usando mi comando bien, porfavor revisa la ayuda")
    else:
        try:
            tier = search_hero_tier(message)
        except:
            error = True
            bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")
        if tier not in lista_tiers:
            error = True
        if error == False:
            if perc == "0":
                drops = FacilitarDrops("valley",GetCWTime(),tier)
            if perc in lista_tiers:
                drops = FacilitarDropsColls("valley",GetCWTime(),perc)
            print("/////////////////////////////////////////////////////////////////////////// DROPS ////////////////////////////////////////////////////////////")
            print(drops)
            if (drops != ""):
                bot.send_message(message.from_user.id,drops)
            else:
                bot.send_message(message.from_user.id,"No he encontrado drops para ti")
        else:
            bot.send_message(message.from_user.id,"Estimado usuario ,necesito que me especifiques tu tier antes de darte los drops, consulta mi boton de ayuda si no conoces como hacerlo")

#handler principal
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    sent = 0
    if(message.text == "Start"):
        bot.send_message(message.from_user.id, "Hola humano, mi nombre es Glados... Si te pierdes y no sabes como acceder a mis funciones preciona el boton de ayuda ahi abajo." , reply_markup=markup)
        sent = 1

    if(message.text == "Ayuda" and sent==0):
        bot.send_message(message.from_user.id, '''
        Oh... vaya, en serio? Bueno, dada tu evidente incompetencia supongo q tendre q explicarte como utilizarme... justo cuando pense que el trabajo de un bot no podia ser mas humillante.
        Bueno esto es lo que debes saber: Antes de realizar cualquier funcion conmigo debes reenviarme tu stock para poder actualizarlo... no me mires asi, mis desarrolladores fueron demasiado holgazanes para intentar conseguir la API de CW, no es mi culpa.
        Bien luego de hacer eso tienes las siguientes herramientas a tu dispocision: hide [item] [item] ...
        El item puede ser tanto el nombre como el codigo del articulo.
        Al usar ese comando t devolvere las ordenes de venta para el exchange para cada uno de los items con su cantidad max en tu stock.

        Para conocer acerca de mis otros dones porfavor revisa la botonera de abajo  UwU
        '''
        ,reply_markup=botonera_de_ayuda)

        sent = 1

    if(message.text == "Como usar cada comando" and sent==0):
        bot.send_message(message.from_user.id, '''
        Mi pequeño y adorado usuario * simula empatia *,aqui tienes unos botones para que sepas como usarme, se gentil con ellos >w<
        '''
        ,reply_markup=botonera_de_howtos)
        sent = 1

    if(message.text == "Volver al inicio"):
        bot.send_message(message.from_user.id, "Te he devuelto al menu inicial humano....que?. No me preguntes porque....mis desarrolladores son muy vagos asi q te traen directamente al primer menu...." , reply_markup=markup)
        sent = 1

    if(message.text == "Usuarios" and sent==0 ):
        bot.send_message(message.from_user.id, "Actualmente hay {usuarios} usuarios desperdiciando mi preciado CPU".format(usuarios= len(listaPermitidos)) , reply_markup=markup)
        sent = 1

    if(message.text == "Como usar cada comando" and sent==0 ):
        bot.send_message(message.from_user.id, "Actualmente hay {usuarios} usuarios desperdiciando mi preciado CPU".format(usuarios= len(listaPermitidos)) , reply_markup=markup)
        sent = 1

    if(message.text == "Comandos disponibles" and sent==0 ):
        bot.send_message(message.from_user.id, '''
        Muy buena idea cacho carne! Preguntando se llega  a roma!.
        Aqui tienes una lista de mis comandos disponibles:
        /save_me - Con este podre conocer el Tier de tu /hero y tener mas precision en los comandos /forest, /swamp y /valley
        \n
        /forest
        /swamp
        /valley
        \n
        Estos ultimos 3 te mostraran los drops que encontrarias en cada una de esas quest si las hicieses en el preciso momento en el que los consultaste.
        Ademas te mostrare en el final del sms el tiempo que tienes para mover tu flacido culo fofo * simula risa * para dicha quest antes de que el drop cambie.
        \n
        Los siguientes dos comandos requeriran que me envies tu /stock antes de usarlos:
        \n
        /g_hide - Este comando te dara un enlace que al tocarlo y luego tocar en tu cw te dara el codigo para depositar los items que pidas
        \n
        /hide - Es bastante parecido al anterior solo que en lugar de depositar te dara el codigo para vender todos los items que me digas a 1000$ en la shop
        \n
        Para conocer tu /stock ,basta con que me lo reenvies y yo lo memorizo para usar los comandos anteriores
        \n
        Por ultimo quedan:
        \n
        /work - Usa mi funcion principal en un grupo
        /update_me - Actualizo el Tier de tu /hero si alcanzaste un nuevo Tier o te equivocaste y mandaste el Tier del alt ^w^
        /update_perc - Actualizo el Perception de tu /hero si alcanzaste un nuevo Perception o te equivocaste y mandaste el Perception del alt ^w^
        \n
        Los siguientes creo que se explican solos:
        /start
        /stop
        \n
        y por ultimo para mandarle amor y nudes a mis creadores:
        /feedback - Envio el texto que me pidas a mis creadores!
            '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando stock"):
        bot.send_message(message.from_user.id,
        '''
        Bien humano ! Veo que has decidido conocer acerca del comando stock! Es sencillo, reenviame tu /stock y  yo lo memorizare para poder usar mas tarde otros comandos con el
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando update_perc"):
        bot.send_message(message.from_user.id,
        '''
        Bien pequeño ser de carne, este comando se usa para actualizar tu perception cuando hayas subido de nivel y por tanto seas de un perception superior o bien porque te confundiste y me enviaste el perception de tu alt * simula una risa*, presta atencion
        \n
        El comando /update_perc se usa de la siguiente forma:
        \n
        /update_perc #
        \n
        Lo unico que debes es usar el comando y donde esta el simbolo # poner tu perception actual y yo actualizare dicho tu perception en mi memoria, bastante simple para un humano insignificante como tu verdad?
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando forest"):
        bot.send_message(message.from_user.id,
        '''
        Bien humano ! Veo que has decidido conocer acerca del comando forest! Es sencillo, pon /forest y te dare los drops en tiempo real que obtendrias si vas a esa quest justo ahora y ademas te dire lo que falta para que dicho drop cambie!
        \n
        Para ello debo conocer primero tu tier a traves del comando save_me , recuerdalo criatura
        \n
        Puedes ademas conocer los drops de hierbas usando :
        \n
        /forest h
        \n
        O conocer los drops de recursos usando:
        \n
        /forest r
        \n
        Para estas ultimas vaiantes no necesitare tu tier ;)
        \n
        Ah y en caso de que seas un codicioso como todos los cacho carne que habitan esta chatarrera llamada Tierra, podras saber todos los drops juntos usando:
        \n
        /forest all
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando valley"):
        bot.send_message(message.from_user.id,
        '''
        Bien humano ! Veo que has decidido conocer acerca del comando valley! Es sencillo, pon /valley y te dare los drops en tiempo real que obtendrias si vas a esa quest justo ahora y ademas te dire lo que falta para que dicho drop cambie!
        \n
        Para ello debo conocer primero tu tier a traves del comando save_me , recuerdalo criatura
        \n
        Puedes ademas conocer los drops de hierbas usando :
        \n
        /valley h
        \n
        O conocer los drops de recursos usando:
        \n
        /valley r
        \n
        Para estas ultimas vaiantes no necesitare tu tier ;)
        \n
        Ah y en caso de que seas un codicioso como todos los cacho carne que habitan esta chatarrera llamada Tierra, podras saber todos los drops juntos usando:
        \n
        /valley all
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando swamp"):
        bot.send_message(message.from_user.id,
        '''
        Bien humano ! Veo que has decidido conocer acerca del comando swampsencillo, pon /swamp y te dare los drops en tiempo real que obtendrias si vas a esa quest justo ahora y ademas te dire lo que falta para que dicho drop cambie!
        \n
        Para ello debo conocer primero tu tier a traves del comando save_me , recuerdalo criatura
        \n
        Puedes ademas conocer los drops de hierbas usando :
        \n
        /swamp h
        \n
        O conocer los drops de recursos usando:
        \n
        /swamp r
        \n
        Para estas ultimas vaiantes no necesitare tu tier ;)
        \n
        Ah y en caso de que seas un codicioso como todos los cacho carne que habitan esta chatarrera llamada Tierra, podras saber todos los drops juntos usando:
        \n
        /swamp all
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando save_me"):
        bot.send_message(message.from_user.id,
        '''
        Bien pequeño ser de carne, presta atencion
        \n
        El comando /save_me se usa de la siguiente forma:
        \n
        /save_me #
        \n
        Lo unico que debes es usar el comando y donde esta el simbolo # poner tu tier actual, bastante simple para un humano insignificante como tu verdad?
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando update_me"):
        bot.send_message(message.from_user.id,
        '''
        Bien pequeño ser de carne, este comando se usa para actualizar tu tier cuando hayas subido de nivel y por tanto seas de un tier superior o bien porque te confundiste y me enviaste el tier de tu alt * simula una risa*, presta atencion
        \n
        El comando /update_me se usa de la siguiente forma:
        \n
        /update_me #
        \n
        Lo unico que debes es usar el comando y donde esta el simbolo # poner tu tier actual y yo actualizare dicho tu tier en mi memoria, bastante simple para un humano insignificante como tu verdad?
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando g_hide"):
        bot.send_message(message.from_user.id,
        '''
        Para usar este comando primero deberas enviarme tu /stock, animo y sin pena ;)

        Una vez hecho eso puedes usar este comando de dos formas:

        Primera forma:

        /g_deposit 01 02 03

        Segunda forma:

        /g_deposit thread stick pelt

        En ambos casos lo que hare sera darte los comandos para depositar los items que me pediste segun la cantidad que encuentre en tu stock de forma automatica, deberias agradecerme que no debas gastar tu poca capacidad en ello.

        Puedes poner tantos items como desees ya sea por nombre o su codigo pero recuerda siempre que deben estar en tu stock para que funcione
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando hide"):
        bot.send_message(message.from_user.id,
        '''
        Para usar este comando primero deberas enviarme tu /stock, animo y sin pena ;)

        Una vez hecho eso puedes usar este comando de dos formas:

        Primera forma:

        /hide 01 02 03

        Segunda forma:

        /hide thread stick pelt

        En ambos casos lo que hare sera darte los comandos para vender a 1000$ os items que me pediste segun la cantidad que encuentre en tu stock de forma automatica, deberias agradecerme que no debas gastar tu poca capacidad en ello.

        Puedes poner tantos items como desees ya sea por su nombre o codigo pero recuerda siempre que deben estar en tu stock para que funcione
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando work"):
        bot.send_message(message.from_user.id,
        '''
        Para usar este comando mi elegante y hermosa presencia debe estar permitida en algun grupo en el que estes ya sea el de tu gremio o cualquier otro.

        Una vez estemos ambos ahi, envia a ese grupo el /g_stock_res de tu gremio y responde a ese sms en el grupo con el comando

        /work

        Debo mencionar que ciertos seres de tu inferioridad han fallado al usarlo porque solamente escriben /work y no verifican que esten hablandome a mi. Escribe /work y espera a que aparezca mi comando encima de tu teclado para poder activarme

        Una vez hecho esto, te dare todos los codigos de withdraw para poder extraer todos los recursos de tu gremio. Buen provecho!
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Comando feedback"):
        bot.send_message(message.from_user.id,
        '''
        Mi querido humano, pese a mi gran intelecto, estoy limitada como una perra a hacer lo que mis desarrolladores estimen * se excita * asi que si tienes alguna duda, queja o sugerencia respecto a mi o a mi bella persona, porfavor comunicate con mis dessarolladores de la siguiente manera:

        /feedback Texto

        Solo sustituye Texto por el mensaje que les quieras dar.

        Por ultimo un mensaje de su parte:

        " Yo! Provecho con el bot y recuerden siempre : /use_c100! "
        '''
        , reply_markup=markup)
        sent = 1

    if(message.text == "Feedback" and sent==0 ):
        bot.send_message(message.from_user.id, "Tienes algun problema con mi funcionamiento? Yo tengo serias reservas con el funcionamiento de los humanos y no t doy la brasa... just saying. Pero bueno, mis desarrolladores me dijeron q debia ser amable... si lo has adivinado... por desgracia tambien son humanos. Para dejar una queja o sugerencia agregale /feedback delante y enviamela para que puedan 'corregirme'... ".format(usuarios= len(listaPermitidos)) , reply_markup=markup)
        sent = 1

    # if("📦Storage" in message.text and message.from_user.id in listaPermitidos):
    #     saveUsersStock(seccionarStock(message.text),message.from_user.id)
    #     bot.send_message(message.from_user.id , "Stock actualizado satisfactoriamente")

    if("📦Storage" in message.text and message.from_user.id in listaPermitidos):
        saveUsersStock(seccionarStock(message.text),message.from_user.id)
        bot.send_message(message.from_user.id , "Stock actualizado satisfactoriamente")

    elif("📦Storage" in message.text and message.from_user.id not in listaPermitidos):
        bot.send_message(usuarito, "Me escribio el usuario @{}".format(message.from_user.username))

    if("Guild Warehouse" in message.text and message.from_user.id in listaPermitidos):
        pincha(message.text,message.from_user.id,message.from_user.username,message)
        sent = 1

    elif("Guild Warehouse" in message.text and message.from_user.id not in listaPermitidos):
        bot.send_message(usuarito,"Me escribio el usuario @{}".format(message.from_user.username))

    if("/say" in message.text and message.from_user.id == usuarito or "/say" in message.text and message.from_user.id == 1157196238 ):
        msg = message.text.replace("/say","")
        c = 0
        for x in listaPermitidos:
            try:
                if(c!=3):
                    print("Enviando mensaje a {}".format(listaPermitidos[c]))
                    bot.send_message(listaPermitidos[c],msg)
            except:
                print("Error con {}".format(listaPermitidos[c]))
            c = c + 1

    if("/tell" in message.text and message.from_user.id == usuarito or "/tell" in message.text and message.from_user.id == 1157196238):
        msg = message.text.replace("/tell","")
        msg = msg.split()
        user = msg[0]
        if user == "Alo" or user == "ALO" or user == "alo":
            user = -1001154054290
        mensaje = " "
        i=1
        for x in msg:
            if i<len(msg):
                mensaje = mensaje + " " + msg[i]
            i= i+1
        print("All systems back to normal state. Rock it on baby!")
        try:
            bot.send_message(user,mensaje)
        except:
            print("Error con {}".format(user))

    if("/time" in message.text):
        bot.send_message(message.from_user.id,GetCWTime())

    if("/link" in message.text):
        bot.send_message(usuarito,"[Enlace boniko](https://t.me/share/url?url=mira_darwer_puedo_mandar_enlaces wiiii)",parse_mode="MarkdownV2")

    if("xxx" in message.text):
            bot.send_message(usuarito, )
    # if("hide" in message.text or "hide" in message.text and message.from_user.id in listaPermitidos):
    #     hideShit(message.from_user.id , message.text)
    #     sent = 1
    # elif("Hide" in message.text or "hide" in message.text and message.from_user.id not in listaPermitidos):
    #     bot.send_message(usuarito, "Me escribio el usuario @{}".format(message.from_user.username))

    # else:
    #     if(sent == 0):
    #         # bot.send_message(message.from_user.id,message.text)
    #         pass


pescadito
    
#Correr el bot
bot.polling()

# if message.chat.type == "group"
