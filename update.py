from dotenv import load_dotenv
from os import getenv
import schedule
import time
from sodapy import Socrata
import pandas as pd

def run():
    load_dotenv() # dotenv is a seperate file to hide app_token, username, and password for security reasons
    key = 'gaFHTdsEerkgHf8zQsgfx2JEC'
    url = 'https://data.cityofchicago.org/resource/ijzp-q8t2.json' # URL to grab data
    client = Socrata('data.cityofchicago.org', 
                    app_token=getenv('app_token'), # Inserts app token from hidden .env file
                    username=getenv('user_name'), # Inserts username from hidden .env file
                    password=getenv('password')) # Inserts password from hidden .env file

    result = client.get('ijzp-q8t2', limit=15000) # Call to API with a limit of 15,000 data

    result # Grab the results
    print('Results grabbed')

    df = pd.DataFrame.from_records(result)
    df = df.drop(columns=[':@computed_region_awaf_s7ux', ':@computed_region_6mkv_f3dw',
                 ':@computed_region_vrxf_vc4k', ':@computed_region_bdys_3d7i',
                 ':@computed_region_43wa_7qmu', ':@computed_region_rpca_8um6',
                 ':@computed_region_d9mm_jgwp', ':@computed_region_d3ds_rm58',
                 'ward', 'location'], axis=1)

    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x) 

    df['date'] = pd.to_datetime(df['date'])
    df['updated_on'] = pd.to_datetime(df['updated_on'])
    df['id'] = df['id'].astype(int)
    df['beat'] = df['beat'].astype(int)
    df['district'] = df['district'].astype(int)
    df['x_coordinate'] = df['x_coordinate'].astype(float)
    df['y_coordinate'] = df['y_coordinate'].astype(float)
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)
    df['community_area'] = df['community_area'].astype(int)
    df['year'] = df['community_area'].astype(int)

    def crime_rat(primary_type):
        key5 = ['battery', 'criminal damage', 'assault', 'narcotics', 'offense', 'criminal', 'sex', 'homicide', 'arson', 'kidnapping', 'weapons', 'criminal', 'concealed'] # Keywords to look for to return 5
        key4 = ['theft', 'motor vehicle theft', 'deceptive practice', 'criminal trespass', 'prostitution', 'robbery', 'burglary', 'deceptive', 'violate'] # Keywords to look for to return 4
        key3 = ['weapons violation', 'interference with public officer', 'stalking', 'interference', 'violation'] # Keywords to look for to return 3
        key2 = ['public', 'obscenity', 'peace'] # Keywords to look for to return 2
        key1 = ['intimidation', 'liquor', 'concealed'] # Keywords to look for to return 1
        for word in primary_type.split(): # Iterate through column 'primary_type' to find word that is inside my keyword lists above
            if word in key5:
                return 5
            elif word in key4:
                return 4
            elif word in key3:
                return 3
            elif word in key2:
                return 2
            elif word in key1:
                return 1
        
    df['crime_rating'] = df['primary_type'].apply(crime_rat) # create crime_rating column -> search 'primary_type' and apply the crime_rat function above

    def fix_rating(description):
        key2 = ['license'] # Keyword to look for to return 2
        key3 = ['harassment', 'telephone', 'vehicle'] # Keywords to look for to return 3
        key4 = ['violate', 'other', 'false', 'gun', 'violation'] # Keywords to look for to return 4
        key5 = ['animal', 'sex', 'money', 'board', 'violent', 'abuse'] # Keywords to look for to return 5
        for word in description.split(): # iterate through description to find if word is inside any of the lists above
            if word in key2:
                return 2 # returns the value I specify
            elif word in key3:
                return 3
            elif word in key4:
                return 4
            elif word in key5:
                return 5
    # apply fix_rating function to columns in df where primary_type is equal to other_offense. fix_rating is updating crime_rating column where the primary_type is other offense
    df.loc[df['primary_type'] == 'other offense', 'crime_rating'] = df.loc[df['primary_type'] == 'other offense', 'description'].apply(lambda x: fix_rating(x)) 
    print('Data Cleaned')
    df.to_csv('crimecapstone.csv',index=False)

    
    run()
    schedule.every().day.at('16:48').do(run)
    while True:
        schedule.run_pending()
        time.sleep(60)