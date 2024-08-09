import discord
import responses
from discord.ext import tasks, commands
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
import random


df = pd.DataFrame(columns=['Product', 'Brand', 'Price'])
df_logs = pd.DataFrame(columns=['Product', 'Brand', 'Price', 'Datetime'])


# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTIzMTM3MDEwNTcyNDczNTUyOA.G9m_Zc.YH6hvCusgJtGZFH4t6Pi0XKwpDeT98MgiEQQxY'

    utc = datetime.timezone.utc

    time = datetime.time(hour=00, minute=32, tzinfo=utc)

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
#       auto_send_message.start()
        send_fiyat.start()

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        
        if user_message == 'eyv':
            raise SystemExit
        
        if user_message == 'fiyat' or user_message == 'fiyat2' or user_message == 'fiyat3':
            send_fiyat.start()
        if user_message == 'logs':
            send_logs.start()
        
    @tasks.loop(seconds=5.0, count=5)
    async def auto_send_message():
        kanal = client.get_channel(1231371511798042727)
        await kanal.send('slm')

    @tasks.loop(seconds=5.0, count=1)
    async def send_logs():
        kanal = client.get_channel(1231371511798042727)
        for index, row in df_logs.iterrows():
                product_name = row['Product']
                brand = row['Brand']
                price = row['Price']
                datetime = row['Datetime']
                message_to_send = "Marka : " + brand + "\n" "Ürün : " + product_name + "\n" + "Fiyat : " + price + "\n" "Sorgu Zamanı : " + datetime + "\n----------------"
                await kanal.send(message_to_send)
        message_to_send = "**Toplam sorgu sayısı: " + str(len(df_logs)) + "**"
        await kanal.send(message_to_send)

    #@tasks.loop(time=time)
    @tasks.loop(minutes = 120.0)
    async def send_fiyat():
        global df
        global df_logs

        # Get the current local date and time
        local_now = datetime.datetime.now()
        # Format the local datetime object as a string
        formatted_local_datetime = local_now.strftime("%Y-%m-%d %H:%M:%S")
        print("çalıştım" + formatted_local_datetime)
        kanal = client.get_channel(1231371511798042727)
        random_number = random.randint(1, 2)
        #if random_number == 1:
        #    url = 'https://www.trendyol.com/sr?q=English%20Home%20Tobacco&qt=English%20Home%20Tobacco&st=English%20Home%20Tobacco&os=1'
        #else:
        #    url = 'https://www.trendyol.com/sr?q=%20English%20Home%20Tobacco%203%27l%C3%BC%20Kokulu%20Kese%20%C5%9Eeffaf%20&qt=%20English%20Home%20Tobacco%203%27l%C3%BC%20Kokulu%20Kese%20%C5%9Eeffaf%20&st=%20English%20Home%20Tobacco%203%27l%C3%BC%20Kokulu%20Kese%20%C5%9Eeffaf%20&os=1'
        url = 'https://www.trendyol.com/sr?q=Tuberose%203%27l%C3%BC%20Kokulu%20Kese%20%C5%9Eeffaf&qt=Tuberose%203%27l%C3%BC%20Kokulu%20Kese%20%C5%9Eeffaf&st=Tuberose%203%27l%C3%BC%20Kokulu%20Kese%20%C5%9Eeffaf&os=1'

        # Send a GET request to the URL
        response = requests.get(url)
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the div with class 'prc-box-dscntd'
        price_elements = soup.find_all('div', class_='prc-box-dscntd')
        name_elements = soup.find_all('div', class_='prdct-desc-cntnr')

        new_data = []
        log_data = []
        # Ensure the number of prices and names match
        if len(price_elements) == len(name_elements):
        # Iterate over both sets of elements simultaneously
            for price_element, name_element in zip(price_elements, name_elements):
                price = price_element.text.strip()  # Get the text content of the price div
                print(price)
                #name = name_element.text.strip()  # Get the text content of the name div
                spans = name_element.find_all('span')
                if len(spans) >= 2:
                    brand = spans[0].text.strip()
                    product_name = spans[1].text.strip()
                    new_data.append((product_name, brand, price))
                    log_data.append((product_name, brand, price,formatted_local_datetime))
                    
                    
                    #message_to_send = "Fiyatı : " + price + "\n" + "Markası : " + brand + "\n" + "Adı : " + product_name
                    #await kanal.send(message_to_send)
            
            print(df)
        else:
            print("Error: Number of prices and names do not match.")

        new_df = pd.DataFrame(new_data, columns=['Product', 'Brand', 'Price'])
        new_df_logs = pd.DataFrame(log_data, columns=['Product', 'Brand', 'Price', 'Datetime'])

        if not df.empty and not new_df.equals(df):  # Check if the new data is different from the previous one
            # Update the DataFrame with new data
            change_flag = ''
            for index, row in new_df.iterrows():
                product_name = row['Product']
                brand = row['Brand']
                price = row['Price']
                #product_comp_df = df[df['Product'] == product_name]
                product_comp_df = df[(df['Product'] == product_name) & (df['Brand'] == brand)]

                if not product_comp_df.empty:
                    old_price = product_comp_df.iloc[0]['Price']
                    if price != old_price:
                        message_to_send = "**Aynı ürün başlığı için fiyat değişti!**\n" + "Marka : " + brand + "\n" "Ürün : " + product_name + "\n" + "Fiyat : " + price + "\n----------------"
                        await kanal.send(message_to_send)
                        change_flag = 'X'
            if change_flag == 'X':        
                message_link = "URL: [Arama Linki](" + url + ")"        
                await kanal.send(message_link)
            
            for index, row in new_df.iterrows():
                product_name = row['Product']
                brand = row['Brand']
                price = row['Price']
                message_to_send = "**Kontrollere takılmadı ama bir şeyler değişti, sen bi bak**\n" + "Marka : " + brand + "\n" "Ürün : " + product_name + "\n" + "Fiyat : " + price + "\n----------------"
                await kanal.send(message_to_send)
            df = new_df
            #message_to_send = "Bulunan Toplam Ürün Sayısı : " + str(len(price_elements))
            #await kanal.send(message_to_send)
            #message_to_send = "Bir şeyler değişti!:\n" + "Marka : " + df['Brand'].to_string(index=False) + "\n" "Ürün : " + df['Product'].to_string(index=False) + "\n" + "Fiyat : " + df['Price'].to_string(index=False)
            #await kanal.send(message_to_send)
            
            
        elif df.empty:  # If DataFrame is empty, populate it with new data
            df = new_df
            for index, row in new_df.iterrows():
                product_name = row['Product']
                brand = row['Brand']
                price = row['Price']
                message_to_send = "**Ürün buldum!**\n" + "Marka : " + brand + "\n" "Ürün : " + product_name + "\n" + "Fiyat : " + price + "\n----------------"
                await kanal.send(message_to_send)
            #message_to_send = "Ürün buldum!\n" + "Marka : " + df['Brand'].to_string(index=False) + "\n" "Ürün : " + df['Product'].to_string(index=False) + "\n" + "Fiyat : " + df['Price'].to_string(index=False)
            #await kanal.send(message_to_send)
            message_link = "URL: [Arama Linki](" + url + ")"
            await kanal.send(message_link)
        
        if not df_logs.empty:  
            
            df_logs = pd.concat([df_logs, new_df_logs], ignore_index=True)
        elif df_logs.empty: 
            df_logs = new_df_logs


        #for div_element in div_elements:
        #    value = div_element.text.strip()  # Get the text content and remove leading/trailing whitespaces
        #    message_to_send = "'English Home Tuberose 3'lü Kokulu Kese Şeffaf' fiyatı:" + value
        #    await kanal.send(message_to_send)


    client.run(TOKEN)