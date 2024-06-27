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


registration('Lionsafc.csv')

