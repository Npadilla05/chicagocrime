import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Chicago Crimes', page_icon=':fire:', layout='wide')

url = 'https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2'
crime_csv = r'crimecapstone.csv'
st.title('Chicago Crimes Capstone Project')

def summary():
    df = pd.read_csv(crime_csv)
    st.image('https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/WCITY_07_1000by500px_1000x.jpg')
    st.title('This page goes over the workflow of my analysis')
    st.write("<h1 style='font-size: 24px;'>Step 1: Get all necessary imports</h1>", unsafe_allow_html=True)
    st.write("<h1 style='font-size: 24px;'>Step 2: API call then transfer to Pandas DataFrame</h1>", unsafe_allow_html=True)
    st.write('- API is an Application Programming Interface')
    st.write('- Set of rules and protocols that allow programs to communicate and share data or funcionality to each other')
    st.write('- Pandas DataFrame is a 2-dimensional labeled data structure')
    st.image(r'https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/finalfinal11.png')
    st.image(r'https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/rawdata.png')
    st.write("<h1 style='font-size: 24px;'>Step 3: Clean and drop unwanted columns</h1>", unsafe_allow_html=True)
    st.write('- Lower-case values in DataFrame for ease of access')
    st.write('- Convert data to their respective data types')
    st.image(r'https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/final3.png')
    st.write("<h1 style='font-size: 24px;'>Step 4: Formulate hypothesis and questions based on data</h1>", unsafe_allow_html=True)
    st.dataframe(df)
    st.write("<h1 style='font-size: 28px;'>Questions to ask myself...</h1>", unsafe_allow_html=True)
    st.write('- Are there certain districts that have crimes of higher severity compared to others?')
    st.write("<h1 style='font-size: 28px;'>Null hypothesis - No relation between districts and crime rates</h1>", unsafe_allow_html=True)
    st.write("<h1 style='font-size: 28px;'>Alternate hypothesis - Lower numbered districts (low income poor area) will have higher crime rates compared to higher district numbers</h1>", unsafe_allow_html=True)
    st.write('- This dataset did not have any way to calculate a score to determine severity')
    st.write("<h1 style='font-size: 24px;'>Step 5:  Data was missing a crime severity rating so I engineered a new column called crime_rating to describe crime severity from 1-5</h1>", unsafe_allow_html=True)
    st.image(r'https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/functions.png')
    st.write("<h1 style='font-size: 24px;'>Step 6: Used Chi-squared test for statistical analysis.</h1>", unsafe_allow_html=True)
    st.image(r'https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/finalfinal6.png')
    st.write("<h1 style='font-size: 24px;'>Step 7: Bar charts to help visualize the answer to my hypothesis</h1>", unsafe_allow_html=True)
    st.image(r'https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/finalfinal7.png')
    st.write("<h1 style='font-size: 34px;'>Conclusion:</h1>", unsafe_allow_html=True) 
    st.write("<h1 style='font-size: 28px;'>The visuals and statistical tests show high crime rating crimes in each district but vary in the types</h1>", unsafe_allow_html=True)
    st.write("<h1 style='font-size: 28px;'>District 24, which is a higher income area has a higher theft count than lower income districts like district 7</h1>", unsafe_allow_html=True)
    st.write("<h1 style='font-size: 28px;'>District 7 shows more battery and assault crimes compared to district 24</h1>", unsafe_allow_html=True)
    st.write("<h1 style='font-size: 28px;'>This evidence allows me to fail to reject my null hypothesis</h1>", unsafe_allow_html=True)


def homepage():
    df = pd.read_csv(crime_csv)
    st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAAhFBMVEX///+z3fL/AADa7vj/3t7/5ub/+fn/9PT/amr/aGj/29v/k5P/kJD/o6P/6+v/6Oj/d3f/sbH/l5f/z8//KSn/Njb/wMD/Gxv/ISH/jIz/VFT/tLT/b2//eXn/xcX/RET/hIT/Pj7/MDD/ysr/YWH/ubn/q6v/S0v/nZ3/fn7/DQ3/XFyZS15JAAAEWklEQVR4nO3c61biMBSGYWaLoBxE5KAinnVGnfu/v+kBWpqdBJJS0Fnv8w9kr8CX3ZCWzrRaAAAAAAAAAAAAAAAADicwtX7BRCYamWhkopGJRiYamWhkopGJRiYamWhkopGJRiYamWhkopGJRiYamWhkopGJRiYamWhkopGJRiYamWhkopGJRibasW/1AAAAsToHKzrkUPVcxRQNY95pZxgzVNT7q6c3jal6nEQUTR5jhpr2YqpqGUrMlEvM7F1JRFFHorqrloU8hBdNJGbKHyWiux5kETFUPSJP4UV9ieiujkg/fKgniemuWiYiEQvKs0R014PIc/hQU4nprloGInIRWtSVmO5KZly6oUUXSdEgeKh6ZsmYd6FF86ToOnio66RqHlp0lxTNgoeqJTnGRZahVZ8S0V3pjMtn6FDLtOqw27Z0xsMXsZu0aBxYNE6LbkKHyt5fcHfVks24tMOKshmXs8ChziSiu9oS1V0hTs/uqqvcdTZmdVfUuzIWtatBdSuZzbjRXd35sppse/leHSovqnZXr2/s/W771aGGWVF17eq+L09be3Qq8nL72tl4mCp3RRd3yQH8Zlalz/0u38d5XlW++8lgtvkw10sWx42hennRefH30fjc0mxvyXPjUfFwkVeVY7/ezjYf7kWewp+P/BOsZjyf8u786ab6tguX2Wzdr2Z+VZR3V3u4MBJaa1eGGlaH+syGutRDZYHffM4rQ+Xd1ftYGAntyWg1TDLzo/WMJ7uiSf9ZzJnccLn6Y9Jkq8+adlfWVeJcktYvlPNk5hfFC7OuEkckRRfKbDBJd5Sr93QxXj+//0iK4yWbjq/1Ry2fcyyd9+UrihdPy+fsq3S7fMFUVTsiWS/GlRd/bQzVQCSVUDRrl6QufVWuL662r8gRSdkpVo1EsnH4aJ4v2Ht3lfu73BOKM5JKp5hG7qp6nKF49xzOUHzbG2co976hlq6qhrok5QjFeeDkHIePf8fnCMXTJSlHpzQYiSOUrTtTa6ds2wRbQ/F2ScraKY0dODlLKDts1i2hbD8vsISyNRJrKI12SerVHHGnk/8Xs+p9h6K5WfSyy1DXZtXrLlV1WL6QD9gnW1aTlGVFabhPjr2ebA3Fusg2up44tm3f53vHsW1rsFOcO1lvKM79ie9HKef+xBuKc9PWWCiefawnFM/m/ufvYxs433F1ivd8x3kZ+PDnO1vOix2hbERSvPi/OS8uInkb7/P6ia1Tfsr1kwNeZ+tVhrJeZ7McPoe/ztbe5XrsX7Pqu12PDfydwW/H6/a31aomr9sbv6of47q9id93NH4H1Pi92IL7CjTuP9G4T8mC+9k07nvUuD9W4z5qC+631/h3GQAAoCHH/k8kviEy0chEIxONTDQy0chEIxONTDQy0chEIxONTDQy0chEIxONTDQy0chEIxONTDQy0chEIxONTDQy0chEIxONTDQy0VonMB37Vg8AAAAAAAAAAAAAAPB9/QMiXYF3OByUWgAAAABJRU5ErkJggg==') 
    st.markdown('[![LinkedIn](https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/smallLI.png)](https://www.linkedin.com/in/noki-padilla-243bb820a/)')
    st.markdown('[![GitHub](https://raw.githubusercontent.com/Npadilla05/Coding-Temple/main/screenshots/smallGH.png)](https://github.com/Npadilla05)')
    st.write('My application that gathers information about crimes in Chicago.')
    st.write('These crimes are gathered through the City of Chicago API [link](%s)' % url)
    sidebar = st.sidebar
    
    sidebar.title('Filter crimes')
    district = sidebar.selectbox('Select a district', ['All'] + df['district'].unique().tolist())
    district2 = sidebar.selectbox('Select district to compare', ['All'] + df['district'].unique().tolist())
    primary_type = sidebar.selectbox('Select crime type', ['All'] + df['primary_type'].unique().tolist())
    location = sidebar.selectbox('Select location', ['All'] + df['location_description'].unique().tolist())
    arrest = sidebar.selectbox('Select arrested', ['All'] + df['arrest'].unique().tolist())
    rating = sidebar.select_slider('Select rating', ['All'] + sorted(df['crime_rating'].unique()))


# filter the crimes dataframe based on user input
    df0 = pd.read_csv(crime_csv)
    if primary_type != 'All':
        df = df[df['primary_type'] == primary_type]
    if location != 'All':
        df = df[df['location_description'] == location]
    if rating != 'All':
        df = df[df['crime_rating'] == rating]
    if arrest != 'All':
        df = df[df['arrest'] == arrest]
    if district != 'All':
        df = df[df['district'] == district]
    if district2 != 'All':
        df0 = df0[df0['district'] == district2]
  

    st.write('By filtering through the data in the sidebar, the dataframe and visualizations will update as well, giving you updated information on the most recent crimes.')
    st.write('I created a crime rating column that will return a score rating from 1-5, based on the severity of the crime.')
    st.write('Hope you enjoy using my Streamlit application! :wave:')

    # display the filtered dataframe
    st.write(df)

    # crime rating map of chicago
    st.header('Crimes of Chicago')
    st.write('The interactive map below shows the crimes located in the Chicagoland area. You are able to hover over each point to gather quick information on the crime.')
    fig1 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='crime_rating', hover_data=['primary_type', 'arrest'],
                            zoom=10, height=500, color_continuous_scale='burg')

    fig1.update_layout(mapbox_style = 'open-street-map')
    st.plotly_chart(fig1, use_container_width=True)
    
    # district map of chicago
    st.header('Districts of Chicago')
    st.write('The interactive map below is color coded and shows the unique districts seperating the Chicagoland area.')
    fig2 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='district', hover_data=['primary_type', 'arrest'],
                            zoom=10, height=500, color_continuous_scale='jet')

    fig2.update_layout(mapbox_style = 'open-street-map')
    st.plotly_chart(fig2, use_container_width=True)

    # # Group by district and primary_type
    # df0= df.groupby(['district', 'primary_type']).mean().reset_index()

    # Create bar chart
    st.header('District chart by Crime Type and Crime Rating')
    st.write('The bar chart below shows the crime rating and type of crime commited.')
    fig5 = px.bar(df, x='primary_type', y='district', color='crime_rating', color_continuous_scale='jet',
                labels={'primary_type': 'Primary Type', 'crime_rating': 'Crime Rating'},
                )

    st.plotly_chart(fig5, use_container_width=True) # Display chart in Streamlit app

    st.header('Compared district by Crime Type and Crime Rating')
    st.write('This bar chart below shows the crime rating and type of crime commited in selected district')
    fig6 = px.bar(df0, x='primary_type', y='district', color='crime_rating', color_continuous_scale='jet',
                labels={'primary_type': 'Primary Type', 'crime_rating': 'Crime Rating'},
                )
    st.plotly_chart(fig6, use_container_width=True)


#### Page Selection ####

pages = {
    'Home page': homepage,
    'Summary and Analysis': summary
}
# Navigation for pages
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page with the session state
page = pages[selection]
page()
