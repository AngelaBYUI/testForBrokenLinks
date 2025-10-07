import gspread

# Use the credentials file to authenticate the service account.
gc = gspread.service_account(filename='credentials.json')

# Open a Google Sheet by its ID.
# Replace 'YOUR_SPREADSHEET_ID' with the ID from your sheet's URL.
try:
    spreadsheet = gc.open_by_key('14Ipv7V2Is7FbfDvDAWMZ6aCQp6cWs8iPGIpPHfpIUfU')

    # Select a worksheet, for example, the first one.
    worksheet = spreadsheet.sheet1

    # Get all values from the worksheet and print them.
    data = worksheet.get_all_values()
    print(data)

except gspread.exceptions.SpreadsheetNotFound:
    print("Error: Spreadsheet not found. Check the ID and sharing permissions.")

