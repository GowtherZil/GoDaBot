#Aki empiezo

def Save_stock(msg, who, user, message):
    banned = True
    if who in listaPermitidos:
        banned = False
    if banned :
        identificacion = "@" + user
        bot.send_message(who,"Usuario Baneado. Contacte al creador para comprar permisos.....")
        bot.send_message(716072728,"Recibi un mensaje del siguiente usuario: " + identificacion)

    else:
        msg = seccionarStock(msg)
        
        bot.save(msg) #Esto no sirve, aki va el codigo para guerdar dentro de la clase. Hasta aki el bot deberia guardar un String con los codigos y cantidades(marcadas con una c al final) del stock del user


def hide(msg, who, user, message):
    banned = True
    if who in listaPermitidos:
        banned = False
    if banned :
        identificacion = "@" + user
        bot.send_message(who,"Usuario Baneado. Contacte al creador para comprar permisos.....")
        bot.send_message(716072728,"Recibi un mensaje del siguiente usuario: " + identificacion)

    else:

        stock = bot.getStock() #este metodo debes implementarlo... algo para obtener el stock ya guardado de un usuario
        stock = stock.split()
        hide = SeccionarHide(msg)
        comandos = ""
        c = 0

        for x in hide:
            for y in stock: #aki me sirvio lo de marcar las cantidades xq asi el no confundira un codigo con una cant
                if y == x:  # ERROR AKI: El stock no se da igual cada vez que se usa el comando, asi que las posiciones de los items variaran
                    comandos = comandos + "/wts_" + x + "_" + stock[c+1] + "_1000" + " " 
                    c = c+1

        comandos = comandos.split()

        for x in comandos:
            bot.send_message(message.from_user.id, x)



def seccionarStock(msg):
    seccion = ""
    c = 2
    text = msg.split()

#en este caso no c han usado los gnomos
    if "/sg_" in msg:

        for x in text:
            if "/sg_" in x:
                seccion = seccion + Quitar_sg(x) + " " 

            if x.isnumeric():
                seccion = seccion + x + "c" + " " #esta c q annado al final es para identificar q ese valor pertenece a una cantidad y no a un codigo
#en este caso ya c usaron los gnomos
    else:
        while c < len(text):
            if "(" in text[c]:
                z = ""
                x = text[c].split()
                for y in x:
                    if y.isnumeric():
                        z=z+y
                seccion = seccion + z + " "
            else if !("(" in text[c]) and !("(" in text[c+1]):
                compuesta = ""
                compuesta = text[c] + text[c+1]
                seccion = seccion + GetCode(compuesta) + " " #este GetCode de aki es el metodo q tenias q implementar y lo mismo d arriba con la c
                c = c+1
            else:
                seccion = seccion + GetCode(text[c])
            
            c = c+1

    return seccion


#este es un metodo solo para remover el /sg_ y poder cojer el codigo de ahi directamente en lugar de usar el GetCode
def Quitar_sg(text):
    cod = ""
    text = text.split()
    for x in text:
        if x.isnumeric():    # ERROR AKI: Aqui el problema es ponernos de acuerdo en la forma que se le pasa el texto, si se le pasa integro, entonces el /stock integro no tiene valores numericos reales, si no strings q contienen numericos
            cod = cod + x
    return cod     

#este metodo es para convertir la orden de hide en una lista de Strings con los codigos de lo q c quiere esconder
def SeccionarHide(msg):  # TALLA AKI : Este parece tar en talla
    seccion = ""
    text = msg.split()
    for x in text:
        if (x != "Hide" or x != "hide"):
            if x.isnumeric() == False:
                seccion = seccion + GetCode(x) + " "
            else:
                seccion = seccion + x + " "

    return seccion

def GetCode(item_name):
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
        "Silver ore" : "10",
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
        "bs frame" : "29",
        "Blacksmith frame" : "29",
        "Artisan frame" : "30",
        "af" : "30",
        "Rope" : "31",
        "rope" : "31",
        "Silver frame" : "32",
        "Metal plate" : "33",
        "Metallic fiber":"34",
        "mf" : "34",
        "Crafted leather" : "35",
        "Quality Cloth" : "36",
        "qc" : "36",
        "Blacksmith mold":"37",
        "bs mold" : "37",
        "Artisan mold" : "38"
    }
    return items_dic.get(item_name)


storage_con_sg = "📦Storage (4133/4500): Use /sg_{code} to trade some amount of resource for 1💰/pcs /sg_30 Artisan frame (1) /sg_11 Bauxite (3) /sg_29 Blacksmith frame (1) /sg_37 Blacksmith mold (2) /sg_21 Bone powder (2) /sg_04 Bone (15) /sg_06 Charcoal (5) /sg_09 Cloth (1) /sg_05 Coal (16) /sg_12 Cord (25) /sg_35 Crafted leather (8) /sg_08 Iron ore (2) /sg_20 Leather (4) /sg_33 Metal plate (5)"
print(Quitar_sg(storage_con_sg))
# print(GetCode("Bone powder"))