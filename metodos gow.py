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
        "blacksmiths mold":"37",
        "bm" : "37",
        "bs mold" : "37",
        "37" : "blacksmith's mold",
        "artisan mold" : "38",
        "am" : "38",
        "38" : "artisan mold",
    }
    return items_dic.get(to_search)


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

def getUsersStock(id):
    msg = open("file.txt","r")
    msg = msg.read()
    indice_inicio = msg.index(id)
    stock_temporal = msg[indice_inicio:len(msg)]  #Aki hubo un cambio no se xq
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
    file = open("file.txt","r")
    allStocks = file.read()
    file.close()    # cerrando el fichero
    if id not in allStocks:
        file = open("file.txt","a")   # agregando al final del archivo
        file.write(id + " " + msg + ", ")
        file.close()
    else:
         stock = id + " " + msg
         previous_stock = id + " " + getUsersStock(id)
         replaced_bd = allStocks.replace(previous_stock,stock)
         file = open("file.txt","w")  # sobreescribiendo el archivo desde 0
         file.write(replaced_bd)
         file.close()
        
        
def removeFile():
    file = open("file.txt","w")
    file.close()


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
                 seccion = seccion + "i-" + text[contador][4:len(text[contador])] + " "
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
                seccion = seccion + "i-" + searchItem(compuesta) + " " #este GetCode de aki es el metodo q tenias q implementar y lo mismo d arriba con la c
                c = c+1
            else:
                seccion = seccion + "i-" + searchItem(text[c]) + " "
            
            c = c+1

    return seccion


def sendSellCodes(id,msg):  # Recibe un string como "Vende 20 ms a 18" para devolver "/wts_13_20_18"
    stock = getUsersStock(id)
    stock = stock.split()
    selling = msg.split()
    item_qtt = selling[1]
    item_price = selling[len(selling)-1]
    if len(selling) == 5:   #en caso de q el nombre sea unico
        item_code = search(selling[2])
    else:
        item_code = search("{} {}".format(selling[2] , selling[3])) # en caso de que el nombre sea compuesto
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
        print("/wts_"+item_code +"_"+item_qtt+"_"+item_price)
    else: #si da negativo tonces:
        print("Usted no tiene la cantidad necesaria de {}".format(search(item_code)))       
    

storage = "📦Storage (4337/4500): Artisan frame (1) Bauxite (3) Blacksmith frame (2) Blacksmith mold (2) Bone powder (2) Bone (17) Charcoal (4) Coal (16) Coke (28) Cord (26) Crafted leather (14) Leather (3)"
storage_con_sg = "📦Storage (4133/4500): Use /sg_{code} to trade some amount of resource for 1💰/pcs /sg_30 Artisan frame (1) /sg_11 Bauxite (3) /sg_29 Blacksmith frame (1) /sg_37 Blacksmith mold (2) /sg_21 Bone powder (2) /sg_04 Bone (15) /sg_06 Charcoal (5) /sg_09 Cloth (1) /sg_05 Coal (16) /sg_12 Cord (25) /sg_35 Crafted leather (8) /sg_08 Iron ore (2) /sg_20 Leather (4) /sg_33 Metal plate (5)"



