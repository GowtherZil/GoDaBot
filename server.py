import telebot
from telebot import types

bot = telebot.TeleBot("El token papu")

listaPermitidos=[lista de usuarios permitidos]

listaGruposPermitidos = [lista de grupos permitidos]


usuarito = el sexy
usuaritin = el sexy ^ 2
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
                 bot.send_message(message.from_user.id, msg[contador])
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
                 bot.send_message(message.chat.id, msg[contador])
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
        "06" : "solvent",
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
    comandos = ""
    d = 0
    while d < len(hide):
        c = 0
        while c < len(stock):
            if stock[c] == hide[d]:
                comandos = comandos + "/wts_" + stock[c] + "_" + stock[c+1] + "_1000" + " "
            c = c+2
        d = d+1
    print("comandos : " + comandos)
    comandos = comandos.split()
    for x in comandos:
        bot.send_message(id, x)




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
                comandos.append("/g_deposit " + stock[c] + " " + stock[c+1] + " ")
            c = c+2
        d = d+1
    print("Comandos:")
    print(comandos)
    # print("Comandos:" + comandos)
    # comandos = comandos.split()
    z = 1
    while z != len(comandos):
        bot.send_message(id, comandos[z])
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
        bot.send_message(id,"/wts_"+item_code +"_"+item_qtt+"_"+item_price)
    else: #si da negativo tonces:
        bot.send_message(id,"Usted no tiene la cantidad necesaria de {}".format(GetCode(item_code)))


#Creando botonera
markup = types.ReplyKeyboardMarkup(row_width=2)
helpButton = types.KeyboardButton('Ayuda')
startButton = types.KeyboardButton('Start')
usersButton = types.KeyboardButton('Usuarios')
feedbackButton = types.KeyboardButton('Feedback')
markup.add(startButton, helpButton, usersButton ,feedbackButton)

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
   bot.send_message(usuaritin msg)
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

#handler principal
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    sent = 0
    if(message.text == "Start"):
        bot.send_message(message.from_user.id, "Hola humano, mi nombre es Glados... Si te pierdes y no sabes como acceder a mis funciones preciona el boton de ayuda ahi abajo." , reply_markup=markup)
        sent = 1
    if(message.text == "Ayuda" and sent==0):
        bot.send_message(message.from_user.id, "Oh... vaya, en serio? Bueno, dada tu evidente incompetencia supongo q tendre q explicarte como utilizarme... justo cuando pense que el trabajo de un bot no podia ser mas humillante. Bueno esto es lo que debes saber: Antes de realizar cualquier funcion conmigo debes reenviarme tu stock para poder actualizarlo... no me mires asi, mis desarrolladores fueron demasiado holgazanes para intentar conseguir la API de CW, no es mi culpa. Bien luego de hacer eso tienes las siguientes herramientas a tu dispocision: hide [item] [item] ... El item puede ser tanto el nombre como el codigo del articulo. Al usar ese comando t devolvere las ordenes de venta para el exchange para cada uno de los items con su cantidad max en tu stock." , reply_markup=markup)
        sent = 1
    if(message.text == "Usuarios" and sent==0 ):
        bot.send_message(message.from_user.id, "Actualmente hay {usuarios} usuarios desperdiciando mi preciado CPU".format(usuarios= len(listaPermitidos)) , reply_markup=markup)
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


    # if("hide" in message.text or "hide" in message.text and message.from_user.id in listaPermitidos):
    #     hideShit(message.from_user.id , message.text)
    #     sent = 1
    # elif("Hide" in message.text or "hide" in message.text and message.from_user.id not in listaPermitidos):
    #     bot.send_message(usuarito, "Me escribio el usuario @{}".format(message.from_user.username))

    # else:
    #     if(sent == 0):
    #         # bot.send_message(message.from_user.id,message.text)
    #         pass





#Correr el bot
bot.polling()

# if message.chat.type == "group"
