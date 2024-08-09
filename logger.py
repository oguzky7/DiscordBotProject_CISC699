# logger.py

import pandas as pd
import datetime

# Define a global DataFrame to store log entries
df_logs = pd.DataFrame(columns=['Product', 'Brand', 'Price', 'Datetime'])
df_logs_kosmos = pd.DataFrame(columns=['ID', 'Name', 'Code', 'Foreign Code', 'Description', 'Foreign Name', 'Data Type', 'Datetime'])

async def log_data(data, channel):
    global df_logs  # Declare the DataFrame as global to access and modify it within the function
    
    formatted_local_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add the formatted_local_datetime column to the data DataFrame
    data['Datetime'] = formatted_local_datetime
    print(formatted_local_datetime)

    # Append the new data to the global DataFrame
    df_logs = pd.concat([df_logs, pd.DataFrame(data)], ignore_index=True)

async def return_logs():
    return df_logs

async def log_data_kosmos(data):
    global df_logs_kosmos

    formatted_local_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Add the formatted_local_datetime column to the data DataFrame
    data['Datetime'] = formatted_local_datetime
    print("local_date_time geliyor")
    print(formatted_local_datetime)
    print("local_date_time gidiyor")

    df_logs_kosmos = pd.concat([df_logs_kosmos, pd.DataFrame(data)], ignore_index=True)

async def return_kosmos_logs():
    return df_logs_kosmos