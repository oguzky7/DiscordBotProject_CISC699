import pandas as pd

async def check_price(data, logs):
    # Initialize an empty list to store changed rows
    changed_rows = []

    # Get the last log data as a DataFrame
    last_log_data = logs.iloc[[-2]]  # Fetch the last row as a DataFrame
    last_log_data.reset_index(drop=True, inplace=True)  # Reset index for proper comparison

    # Iterate over each row in the new data
    for index, row in data.iterrows():
        product_name = row['Product']
        brand = row['Brand']
        price = row['Price']

        # Check if there is a matching row in the last log data
        matching_row = last_log_data[(last_log_data['Product'] == product_name) & 
                                     (last_log_data['Brand'] == brand) & 
                                     (last_log_data['Price'] == price)]

        # If no matching row is found, add it to the list of changed rows
        if matching_row.empty:
            changed_rows.append(row)

    # Convert the list of changed rows to a DataFrame
    changed_rows_df = pd.DataFrame(changed_rows)

    # Return the DataFrame containing the changed rows
    return changed_rows_df


async def check_kosmos_max_date(data, logs):
    # Initialize an empty list to store changed rows
    changed_rows = []

    # Get the last log data as a DataFrame
    last_log_data = logs.iloc[[-2]]  # Fetch the last row as a DataFrame
    last_log_data.reset_index(drop=True, inplace=True)  # Reset index for proper comparison

    # Iterate over each row in the new data
    for index, row in data.iterrows():
        data_type = row['Data Type']
        name = row['Name']

        # Check if there is a matching row in the last log data
        matching_row = last_log_data[(last_log_data['Data Type'] == data_type) & 
                                     (last_log_data['Name'] == name)]

        # If no matching row is found, add it to the list of changed rows
        if matching_row.empty:
            changed_rows.append(row)

    # Convert the list of changed rows to a DataFrame
    changed_rows_df = pd.DataFrame(changed_rows)

    # Return the DataFrame containing the changed rows
    return changed_rows_df
