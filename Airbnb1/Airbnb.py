import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import plotly.express as px
import os

# Streamlit application
st.title('Airbnb Analysis 🧮 ')

# Create a Streamlit sidebar with menu options
menu_choice = st.sidebar.radio("Menu", ["Home",  "Visualize data", "Contact"])

if menu_choice == "Home":
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; font-size: 24px;">
             Home 🏠
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create two columns for layout
    left_column, right_column = st.columns(2)

    # PhonePe logo in the left column
    left_column.image("Airbnb.png", width=300)

    # Description in violet color in the right column
    with right_column:
        st.markdown(
            """
            Airbnb, established in 2008, is a widely-used online platform connecting travelers with unique lodging options worldwide. 
            The service enables individuals to rent out their homes or rooms, offering a diverse range of accommodations. 
            Airbnb has revolutionized travel, providing more personalized experiences compared to traditional hotels. 
            Users can explore listings based on location, price, and amenities, fostering a sense of community and cultural exchange. 
            With millions of listings, Airbnb has become a significant player in reshaping global tourism dynamics
            """,
            unsafe_allow_html=True
        )

    # Add the YouTube video link in the center
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/dA2F0qScxrI" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
    #creating space between video and button
    st.markdown(
        """ """,
        unsafe_allow_html=True
    )

    # Add a styled button with margin
    st.markdown(
        """
        <a href="https://play.google.com/store/apps/details?id=com.airbnb.android&pcampaignid=web_share"
        target="_blank" rel="noopener noreferrer" style="display: inline-block; background-color: #007BFF;
        color: #FFFFFF; padding: 10px 20px; text-align: center; text-decoration: none; border-radius: 5px; margin-bottom: 20px;">
        Download Airbnb
        </a>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        Airbnb has grown rapidly since its launch in 2008, becoming a leading platform for vacation rentals and short-term stays. Here are some key statistics that highlight the company's success:

           Over 6 million active listings in over 220 countries and regions, offering a wide range of accommodations, from private rooms to entire apartments and villas.
           Over 4 billion guest arrivals since its inception, demonstrating the platform's popularity among travelers worldwide.
           Over 4 million hosts who have welcomed guests from all corners of the globe.
           A global economic impact of over $1 trillion, with significant contributions to local economies and job creation.
           Here are some additional statistics that provide more insights into Airbnb's impact:

           The average Airbnb booking is for 4.3 nights.
           Airbnb guests are primarily millennials, with 52% of guests aged 25-34.
           Airbnb guests are increasingly coming from emerging markets, with China, India, and Brazil among the top source markets.
           Airbnb is popular for both business and leisure travel, with 40% of bookings made for business purposes.
           These statistics underscore Airbnb's significant role in the global travel industry. The company has transformed the way people travel, offering more personalized and affordable lodging options, and fostering a sense of community and cultural exchange. As Airbnb continues to grow, it is likely to have an even greater impact on the world of travel.""",
        unsafe_allow_html=True
    )

    # Add a styled button with margin
    st.markdown(
        """
        <a href="https://www.airbnb.co.in/"
        target="_blank" rel="noopener noreferrer" style="display: inline-block; background-color: #007BFF;
        color: #FFFFFF; padding: 10px 20px; text-align: center; text-decoration: none; border-radius: 5px; margin-bottom: 20px;">
        Airbnb Website
        </a>
        """,
        unsafe_allow_html=True
    )

if menu_choice == "Visualize data":
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; font-size: 24px;">
             Visualize data 📈
        </div>
        """,
        unsafe_allow_html=True
    )

    # Load data from CSV file for heatmap
    df_heatmap = pd.read_csv('######')#your csv path

    # Convert 'Price' column to numeric (remove dollar signs and convert to float)
    df_heatmap['Price'] = df_heatmap['Price'].replace('[\$,]', '', regex=True).astype(float)

    # Create a dynamic price heatmap showing average prices across different locations
    heatmap_fig = px.scatter_geo(df_heatmap,
                                 lat='Latitude',
                                 lon='Longitude',
                                 color='Price',
                                 hover_name='Name',
                                 size='Price',
                                 size_max=40,  # Adjust the size_max parameter to make icons larger
                                 title='Average Prices of Listings Across Different Locations',
                                 projection='natural earth',
                                 color_continuous_scale='Turbo')  # Change the color scale here

    # Show the dynamic price heatmap
    st.plotly_chart(heatmap_fig)

    # Load data for price and review analysis
    df_analysis = pd.read_csv('######')#your csv path

    # Streamlit App
    st.title("Airbnb Price and Review Scores Analysis")

    # User Input: Select Country
    selected_country = st.selectbox("Select a Country", df_analysis['Country'].unique(), key="country_select")

    # User Input: Select Highest or Lowest Prices
    selected_price_type = st.selectbox("Select Price Type", ["Highest", "Lowest"], key="price_type_select")

    # Filter data based on the selected country
    filtered_data = df_analysis[df_analysis['Country'] == selected_country]

    # Function to plot top N max and min prices using Plotly
    def plot_price_analysis(data, top_n=10, price_type="Highest"):
        # Sort data by price
        sorted_data = data.sort_values(by='Price')

        if price_type == "Highest":
            # Top N highest prices in descending order
            selected_prices = sorted_data.tail(top_n)
        elif price_type == "Lowest":
            # Top N lowest prices in descending order
            selected_prices = sorted_data.head(top_n).sort_values(by='Price', ascending=False)
        else:
            st.error("Invalid selection for Price Type")

        # Plotting using Plotly
        st.subheader(f"Top {top_n} {price_type} Prices in {selected_country}")
        fig = px.bar(selected_prices, x='Price', y='Name', orientation='h', text='Price',
                     title=f'Top {top_n} {price_type} Prices')
        st.plotly_chart(fig)

    # Function to plot top N max and min review scores using Plotly
    def plot_review_scores(data, top_n=10, review_type="Highest", selected_country=""):
        # Sort data by review scores
        sorted_data = data.sort_values(by='Review_scores', ascending=False)

        if review_type == "Highest":
            # Top N highest review scores in descending order
            selected_reviews = sorted_data.head(top_n)

        elif review_type == "Lowest":
            # Top N lowest review scores in ascending order
            selected_reviews = sorted_data.tail(top_n)
            selected_reviews = selected_reviews.sort_values(by='Review_scores', ascending=True)
        else:
            st.error("Invalid selection for Review Type")

        # Plotting using Plotly
        st.subheader(f"Top {top_n} {review_type} Review Scores in {selected_country}")
        fig = px.bar(selected_reviews, x='Review_scores', y='Name', orientation='h', text='Review_scores',
                     title=f'Top {top_n} {review_type} Review Scores')
        st.plotly_chart(fig)

    # User Input: Select Highest or Lowest Review Scores
    selected_review_type = st.selectbox("Select Review Type", ["Highest", "Lowest"], key="review_type_select")

    # Plotting for the selected country and price type
    plot_price_analysis(filtered_data, price_type=selected_price_type)

    # Plotting for the selected country and review type
    plot_review_scores(filtered_data, review_type=selected_review_type)

    # Load data from CSV
    df = pd.read_csv('######')#your csv path

    # Streamlit App
    st.title("Availability Analysis for Airbnb Listings")

    # User Input: Select Country
    selected_country_availability = st.selectbox("Select a Country", df['Country'].unique(),
                                                 key="availability_country_select")

    # User Input: Filter by Property Type
    selected_property_type_availability = st.selectbox("Filter by Property Type", df['Property_type'].unique(),
                                                       key="property_type_select")

    # Filter data based on the selected country and property type
    filtered_data_availability = df[
        (df['Country'] == selected_country_availability) & (df['Property_type'] == selected_property_type_availability)]

    # Display the filtered data
    st.subheader(f"Filtered Data for {selected_country_availability} - {selected_property_type_availability}")
    st.dataframe(filtered_data_availability[["Listing_url", "Name", "Description", "House_rules", "Room_type",
                                             "Accomodates", "Total_bedrooms", "Total_beds", "Availability_365",
                                             "Price", "Review_scores", "Amenities", "Host_id", "Host_name",
                                             "Street", "Country", "Country_code"]])

    # Save Button to save filtered data to CSV with a download button
    if st.button("Save Filtered Data to CSV"):
        # Construct the file name
        file_name_availability = f"{selected_country_availability}_{selected_property_type_availability}.csv"

        # Create a download button
        download_button_str_availability = f"Download {file_name_availability}"

        # Create a link for downloading
        csv_availability = filtered_data_availability.to_csv(index=False)
        st.download_button(label=download_button_str_availability, data=csv_availability,
                           file_name=file_name_availability, key='csv_availability')

        st.success(f"Filtered data is ready for download!")

    # Fixed file path for the Folium map CSV data
    csv_file_path_folium = '######'#your csv path

    # Dropdown to select the country for Folium map
    selected_country_folium = st.selectbox("Select a Country for Folium Map", df['Country'].unique())

    # Button to show the Folium map
    if st.button("Show Folium Map"):
        # Load your CSV data for Folium
        df_folium = pd.read_csv(csv_file_path_folium)

        # Filter data based on the selected country for Folium
        filtered_data_folium = df_folium[df_folium['Country'] == selected_country_folium]

        # Define bounding box coordinates for the selected country
        min_latitude_folium = filtered_data_folium['Latitude'].min()
        max_latitude_folium = filtered_data_folium['Latitude'].max()
        min_longitude_folium = filtered_data_folium['Longitude'].min()
        max_longitude_folium = filtered_data_folium['Longitude'].max()

        # Create a base map for Folium
        m_folium = folium.Map(
            location=[filtered_data_folium['Latitude'].mean(), filtered_data_folium['Longitude'].mean()],
            zoom_start=4)

        # Add markers to the Folium map
        for index, row in filtered_data_folium.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=f"Name: {row['Name']}, {row['Property_type']} - ${row['Price']}, Accommodates: {row['Accomodates']}, Reviews: {row['Review_scores']}",
                icon=folium.Icon(color='blue')
            ).add_to(m_folium)

        # Use folium_static to display the map in Streamlit
        folium_static(m_folium)


if menu_choice == "Contact":
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; font-size: 24px;">
            🎓 Contact
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("Regards,")
    st.write(
        "Thank you for exploring the Airbnb Analysis application. This project leverages the power of Streamlit, Folium, Pandas, Plotly, and other Python libraries to provide a comprehensive analysis of Airbnb data.")
    st.write(
        "The application allows users to visualize and analyze key metrics such as average prices, top listings, and availability across different countries. The integration of Folium adds an interactive map feature, enhancing the user experience.")
    st.write(
        "The underlying data analysis includes insights into pricing trends, review scores, and property availability. Users can filter and download specific data for further exploration.")
    st.write(
        "Developing this application was a rewarding experience, and I aimed to create an intuitive interface for users to gain valuable insights into Airbnb trends worldwide.")
    st.write(
        "With gratitude for the support and guidance from GUVI Geek Networks and the IIT Madras Data Science Programme at IIT Madras Research Park (IITMRP), as well as the collaborative efforts of IITMDSA Zen DataScience, GUVI, I look forward to more exciting ventures ahead.")
    st.write("Best Regards,")
    st.write("🎓Rajashekhara S Gowda")
    st.write("  ")
    st.write("For any inquiries or assistance, please feel free to contact me at:")
    st.write("Email: rajusgowda522000@gmail.com")
    st.write("LinkedIn: https://www.linkedin.com/in/raju-s-gowda-5f2000")