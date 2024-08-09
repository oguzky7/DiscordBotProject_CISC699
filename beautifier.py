import config
async def log_beautify_and_send(logs, channel):
    
    for index, row in logs.iterrows():
        product_name = row['Product']
        brand = row['Brand']
        price = row['Price']
        datetime = row['Datetime']
        message_to_send = "Marka : " + str(brand) + "\n" "Ürün : " + str(product_name) + "\n" + "Fiyat : " + str(price) + "\n" "Sorgu Zamanı : " + datetime + "\n----------------"

        await channel.send(message_to_send)

    message_to_send = "**Toplam sorgu sayısı: " + str(len(logs)) + "**"
    await channel.send(message_to_send)

async def trendyol_beautify_and_send(data, channel, change_detected):

    for index, row in data.iterrows():
                
                product_name = row['Product']
                brand = row['Brand']
                price = row['Price']

                if change_detected == True:
                    message_to_send = "**Değişiklik var!**\n" + "Marka : " + brand + "\n" "Ürün : " + product_name + "\n" + "Fiyat : " + price + "\n----------------"
                else:
                    message_to_send = "**Ürün buldum!**\n" + "Marka : " + brand + "\n" "Ürün : " + product_name + "\n" + "Fiyat : " + price + "\n----------------"

                await channel.send(message_to_send)

    url = config.Config.TRENDYOL_URL
    message_link = "URL: [Arama Linki](" + url + ")"
    await channel.send(message_link)


async def kosmos_log_beautify_and_send(logs, channel):
    
    for index, row in logs.iterrows():
        id = row['ID']
        name = row['Name']
        code = row['Code']
        foreign_code = row['Foreign Code']
        description = row['Description']
        foreign_name = row['Foreign Name']
        data_type = row['Data Type']
        datetime = row['Datetime']
        message_to_send = "Maksimum randevu alınabilecek tarih : " + str(name) + "\n" "Sorgu Zamanı : " + datetime + "\n----------------"
        await channel.send(message_to_send)

    message_to_send = "**Toplam sorgu sayısı: " + str(len(logs)) + "**"
    await channel.send(message_to_send)


async def kosmos_beautify_and_send(logs, channel, change_detected):
    
    for index, row in logs.iterrows():
        id = row['ID']
        name = row['Name']
        code = row['Code']
        foreign_code = row['Foreign Code']
        description = row['Description']
        foreign_name = row['Foreign Name']
        data_type = row['Data Type']


        if change_detected == True:
            message_to_send = "**Kosmos Tarih Değişti!**"
            await channel.send(message_to_send)
            message_to_send = "Maksimum randevu alınabilecek yeni tarih : " + str(name) 
            await channel.send(message_to_send)
        else:
            message_to_send = "Maksimum randevu alınabilecek tarih : " + str(name) 
            await channel.send(message_to_send)