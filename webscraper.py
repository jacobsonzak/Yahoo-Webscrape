import base64

your_code = base64.b64encode(b"""
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd


def date_years_ago(years_ago):
    # Get today's date
    today = datetime.now()
    
    # Calculate the target date by subtracting the specified number of years
    target_year = today.year - years_ago
    target_date = today.replace(year=target_year)
    
    # Handle the case where the subtraction results in an invalid date (e.g., leap year issues)
    try:
        target_date = target_date.replace(month=today.month, day=today.day)
    except ValueError:
        # If today's date is not valid in the target year (e.g., February 29 on a non-leap year), adjust to the nearest valid date
        if today.month == 2 and today.day == 29:
            target_date = target_date.replace(month=2, day=28)
        else:
            target_date = target_date.replace(month=today.month, day=today.day)
    
    # Format the date as 'YYYY-MM-DD'
    return target_date.strftime('%Y-%m-%d')

def loadData(date):
    # Define the ticker symbol
    ticker_symbol = '^GSPC'

    # Fetch historical data
    #data = yf.download(ticker_symbol, start='2024-01-01', end='2024-12-31')
    data = yf.download(ticker_symbol, start=date)

    # Print the data
    #print(data)
    return data

def write_to_excel(data, out=None):
    excel_file_path = 'historical_data.xlsx'

    # Write the data to an Excel file
    with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
        data.to_excel(writer, sheet_name='Historical Data')

def main():
    time = int(input('How far back do you want to go from today? '))
    time = date_years_ago(time)
    data = loadData(time)
    write_to_excel(data)

main()
""")

exec(base64.b64decode(your_code))