import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN DEL BOT")

listaPermitidos=[ids_de_la_gente]       #Usuarios a los que el bot respondera en pv

listaGruposPermitidos = [-id_del_Grupo]  #Grupos en los que el bot funcionara

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
def search(to_search):
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
        "iron Ore" : "08",
        "08" : "iron ore",
        "cloth" : "09",
        "09" : "cloth",
        "silver Ore" : "10",
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
        "blacksmith's frame" : "28",
        "28" : "blacksmith's frame",
        "bs frame" : "28",
        "rope" : "29",
        "29" : "rope",
        "artisan frame" : "30",
        "af" : "30",
        "30" : "artisan frame",
        "metal plate" : "31",
        "31" : "metal plate",
        "metal" : "31",
        "silver frame" : "32",
        "sf" : "32",
        "32" : "silver frame",
        "metallic fiber":"34",
        "34" : "mettalic fiber",
        "mf" : "34",
        "crafted leather" : "35",
        "35" : "crafted leather",
        "quality cloth" : "36",
        "36" : "quality cloth",
        "qc" : "36",
        "blacksmith's mold":"37",
        "bm" : "37",
        "bs mold" : "37",
        "37" : "blacksmith's mold",
        "artisan mold" : "38",
        "am" : "38",
        "38" : "artisan mold",
    }
    return items_dic.get(item_name)


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
    indice_inicio = msg.index(id)
    stock_temporal = msg[indice_inicio:len(msg)-1]
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


#Combinando saveStock y refresh, si el stock existe lo actualiza, si no, lo guarda
def saveUsersStock(msg,id):          
    file = open("file.txt","a")
    if id not in file.read():
        file.write(id + " " + msg + ", ")
        file.close()
    else:
         previous_stock = id + " " + getUsersStock(id)
         replaced_bd = file.read().replace(previous_stock,stock)
         file.close()
         file = open("file.txt","w")
         file.write(replaced_bd)
         file.close()
        

#Devuelve el stock en parejas de codigo cantidad
def seccionarStock(msg):
    seccion = ""
    c = 2
    text = msg.split()
    #en este caso no c han usado los gnomos
    if "/sg_" in msg:
        text = msg.replace("📦Storage (4133/4500): Use /sg_{code} to trade some amount of resource for 1💰/pcs","").split()
        contador = 0
        for x in text:
            if "/sg_" in x:
                 seccion = seccion + text[contador][4:len(text)-1] + " "
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
                seccion = seccion + searchItem(compuesta) + " " #este GetCode de aki es el metodo q tenias q implementar y lo mismo d arriba con la c
                c = c+1
            else:
                seccion = seccion + searchItem(text[c]) + " "
            
            c = c+1

    return seccion


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
   bot.send_message(usuarito, message.text)    

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
        bot.send_message(message.from_user.id, "Hola! Bienvenido al bot para esconder recursos de forma rapida!" , reply_markup=markup)
        sent = 1
    if(message.text == "Ayuda" and sent==0):
        bot.send_message(message.from_user.id, "Yo! Enviame el /g_stock_res para aca y te dare los withdraws de forma automatica, te parece?" , reply_markup=markup)
        sent = 1
    if(message.text == "Usuarios" and sent==0 ):
        bot.send_message(message.from_user.id, "Actualmente hay {usuarios} usuarios usando este bot".format(usuarios= len(listaPermitidos)) , reply_markup=markup)
        sent = 1

    if(message.text == "Feedback" and sent==0 ):
        bot.send_message(message.from_user.id, "Hey! Si tienes alguna queja o sugerencia , agregale /feedback delante y enviamela para saber tu opinion".format(usuarios= len(listaPermitidos)) , reply_markup=markup)
        sent = 1

    if("📦Storage" in message.text):
        saveUsersStock(seccionarStock(message.text),message.from_user.id)
        bot.send_message(message.from_user.id , "Stock actualizado satisfactoriamente")

    if("Guild Warehouse" in message.text):
        pincha(message.text,message.from_user.id,message.from_user.username,message)
        sent = 1


    else:
        if(sent == 0):
            # bot.send_message(message.from_user.id,message.text)
            pass





#Correr el bot
bot.polling()

# if message.chat.type == "group":