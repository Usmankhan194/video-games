import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('Video_Games.csv')

# Define function for Line Plot
def line_plot():
    # Create a new DataFrame for the sales columns
    sales_df = df[['Year_of_Release', 'EU_Sales', 'NA_Sales', 'JP_Sales', 'Global_Sales']]
    sales_df = sales_df.groupby('Year_of_Release').sum()
    
    # Create the line plot
    sales_df.plot(kind='line')
    plt.title('Video Game Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.show()

# Define function for Pie Chart
def pie_chart():
    # Create a new DataFrame for the rating column
    rating_df = df['Rating'].value_counts()
    
    # Create the pie chart
    rating_df.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Video Game Ratings')
    plt.show()

# Define function for Bar Plot
def bar_plot():
    # Create a new DataFrame for the type of game column
    type_df = df['Type_of_Game'].value_counts()
    
    # Create the bar plot
    type_df.plot(kind='bar')
    plt.title('Video Game Types')
    plt.xlabel('Type of Game')
    plt.ylabel('Number of Games')
    plt.show()
    
# Call the functions to create the plots
line_plot()
pie_chart()
bar_plot()
