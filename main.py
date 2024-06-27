import pandas as pd



def registration(csv):
    # Read the CSV file
    df = pd.read_csv(csv)

    count_YS = df['Kit_Type_Size__c'].value_counts().get('Mainstream-YS (6-8 Years)', 0)
    count_YM = df['Kit_Type_Size__c'].value_counts().get('Mainstream-YM (9-10 Years)', 0)
    count_YL = df['Kit_Type_Size__c'].value_counts().get('Mainstream-YL (11-12 Years)', 0)
    count_YXL = df['Kit_Type_Size__c'].value_counts().get('Mainstream-YXL (13-14 Years)', 0)
    count_SMALL_ADULT = df['Kit_Type_Size__c'].value_counts().get('Mainstream-Small Adult', 0)
    count_MEDIUM_ADULT = df['Kit_Type_Size__c'].value_counts().get('Mainstream-Medium Adult', 0)

    print(f"Count of 'Mainstream-YS (6-8 Years)': {count_YS}")
    print(f"Count of 'Mainstream-YM (9-10 Years)': {count_YM}")
    print(f"Count of 'Mainstream-YL (11-12 Years)': {count_YL}")
    print(f"Count of 'Mainstream-YXL (13-14 Years)': {count_YXL}")
    print(f"Count of 'Mainstream-Small Adult': {count_SMALL_ADULT}")
    print(f"Count of 'Mainstream-Medium Adult': {count_MEDIUM_ADULT}")
    # Convert 'Date_of_Birth__c' column to datetime if necessary
    # df['Date_of_Birth__c'] = pd.to_datetime(df['Date_of_Birth__c'])

    # Delete the columns by specifying the column names
    columns_to_delete = ['Kit_Required__c', 'Late_Booking__c', 'Alternative_Guardian_Number__c', 
                        'Primary_Guardian_Name__c', 'Primary_Guardian_Number__c', 'Gender__c']
    df.drop(columns=columns_to_delete, inplace=True)

    df['Date_of_Birth__c'] = pd.to_datetime(df['Date_of_Birth__c'])
    # Sort DataFrame by 'Date_of_Birth__c' from youngest to oldest
    df_sorted = df.sort_values(by='Date_of_Birth__c', ascending=False)

    # # Display the modified DataFrame
    # print("Modified DataFrame:")
    # print(df_sorted.head())

    counts_df = pd.DataFrame({
        'Size': ['Mainstream-YS (6-8 Years)', 'Mainstream-YM (9-10 Years)', 'Mainstream-YL (11-12 Years)',
                 'Mainstream-YXL (13-14 Years)', 'Mainstream-Small Adult', 'Mainstream-Medium Adult'],
        'Count': [count_YS, count_YM, count_YL, count_YXL, count_SMALL_ADULT, count_MEDIUM_ADULT]
    })

    # Append the counts DataFrame to the sorted DataFrame
    df_with_counts = pd.concat([df_sorted, counts_df], ignore_index=True)

    # Save the modified DataFrame back to a CSV file
    df_with_counts.to_csv('modified_file.csv', index=False)
    return 'modified_file.csv'

def groups(csv):
    df = pd.read_csv(csv)

    columns_to_delete = ['Kit_Required__c', 'Late_Booking__c', 'Alternative_Guardian_Number__c', 
                        'Primary_Guardian_Name__c', 'Primary_Guardian_Number__c', 'Gender__c', 'Kit_Type_Size__c']
    df.drop(columns=columns_to_delete, inplace=True)

    df['Date_of_Birth__c'] = pd.to_datetime(df['Date_of_Birth__c'])
    # Sort DataFrame by 'Date_of_Birth__c' from youngest to oldest
    df_sorted = df.sort_values(by='Date_of_Birth__c', ascending=False)

    df_chunks = []

    for i in range(0, len(df_sorted), 15):
        # Get the chunk of group_size rows
        chunk = df_sorted.iloc[i:i+15]

        # Append the chunk to the list
        df_chunks.append(chunk)

        # If this is not the last chunk, append NaN rows as a gap
        if i + 15 < len(df):
            gap_df = pd.DataFrame(index=range(5), columns=df.columns)
            df_chunks.append(gap_df)
   
    final_df = pd.concat(df_chunks, ignore_index=True)

    columns_to_delete = ['Date_of_Birth__c']
    final_df.drop(columns=columns_to_delete, inplace=True)

    columns = ['Mon-SignIn', 'Signout', 'Tues-In', 'Tues-Out', 'Wed-In','Wed-Out ' ,'Thurs-In', 'Thurs-Out ','Fri-In','Fri-Out']

    for col in columns:
        final_df[col] = ''

    final_csv_file = 'groups.csv'
    final_df.to_csv(final_csv_file, index=False)

    return final_csv_file

groups('Lionsafc.csv')
registration('Lionsafc.csv')

