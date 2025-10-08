import gspread
from gspread import cell
from gspread.utils import rowcol_to_a1

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
        col_data = worksheet.col_values(2)  # column 'A' is 1, 'B' is 2, and so on.
        col_data +=[""]*(num_rows-len(col_data)) #Pad the list if it's shorter than num_rows

        cell_to_mark_empty=[] #to catch the cells which need to show there's no url
        cell_to_mark_broken=[]

        for row in range(1, num_rows+1):

            #check if there's a link in the cell of this line
            if not col_data[row-1]:
                cell_location = rowcol_to_a1(row, 5) #rowcol_to_a1 is a fuction from gspread library; (row, col) e.g. (4,3) means cell C4.
                cell_to_mark_empty.append({
                    'range': cell_location,
                    'values': [["empty"]] #means the cell with url doesn't have data. e.g. it's the name of the section in this line.
                })
         # to mark there's no url line
        if cell_to_mark_empty:
            worksheet.batch_update([{
                "range":cell["range"], # the range in cell["range"] is the same as line 25, and it's a key word for line 25 so we can't rename it.
                "values":cell["values"] #same concept as last line
            }for cell in cell_to_mark_empty])



        try: #get and mark the non-url line in the WhatsApp links sheet
            for col in col_data:
                if col == "":
                    rowNumber = 1
                    print(col)
                    print("It's empty")
        except gspread.exceptions.APIError as e:
            print("Error happened for marking the empty data")

    except gspread.exceptions.APIError as e:
        print(f"An API error occurred: {e}")

    # Get all values from the worksheet and print them.
    # data = worksheet.get_all_values()
    # print(data)

except gspread.exceptions.SpreadsheetNotFound:
    print("Error: Spreadsheet not found. Check the ID and sharing permissions.")

