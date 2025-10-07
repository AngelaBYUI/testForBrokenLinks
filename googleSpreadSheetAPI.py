import gspread

# Use the credentials file to authenticate the service account.
gc = gspread.service_account(filename='credentials.json')

# Open a Google Sheet by its ID.
# Replace 'YOUR_SPREADSHEET_ID' with the ID from your sheet's URL.
try: #get the file and the specific sheet
    spreadsheet = gc.open_by_key('14Ipv7V2Is7FbfDvDAWMZ6aCQp6cWs8iPGIpPHfpIUfU') #the key is url for the sheet but only the strings between /d/ and /edit
    worksheet = spreadsheet.get_worksheet(1) #to access the sheet by index. The first sheet should be 0 and so on.
    try: #get the dta from specific column but restrict in the len(rows) bc we don't want to mark a thousand empty lines.
        allDataInList = worksheet.get_all_values()
        num_rows = len(allDataInList) #to get how many lines/rows have data and we will restrict the marking stuff in this range.
        col_number = 2  # column 'A' is 1, 'B' is 2, and so on.
        col_data = worksheet.col_values(col_number)
        print(f"Data from row {col_number}:")
        print(col_data)

        try: #get and mark the non-url line in the WhatsApp links sheet
            # for col in col_data:
            #     if col == "":
            #         rowNumber =
            #         print(col)
            #         print("It's empty")
        except gspread.exceptions.APIError as e:
            print("Error happened for marking the empty data")

    except gspread.exceptions.APIError as e:
        print(f"An API error occurred: {e}")

    # Get all values from the worksheet and print them.
    # data = worksheet.get_all_values()
    # print(data)

except gspread.exceptions.SpreadsheetNotFound:
    print("Error: Spreadsheet not found. Check the ID and sharing permissions.")

