import gspread
from gspread import cell
from gspread.utils import rowcol_to_a1
from testForBrokenLinks import check_links_func
import re

# Use the credentials file to authenticate the service account.
gc = gspread.service_account(filename='credentials.json')

# Open a Google Sheet by its ID.
# Replace 'YOUR_SPREADSHEET_ID' with the ID from your sheet's URL.
try: #get the file and the specific sheet
    spreadsheet = gc.open_by_key('14Ipv7V2Is7FbfDvDAWMZ6aCQp6cWs8iPGIpPHfpIUfU') #the key is url for the sheet but only the strings between /d/ and /edit
    worksheet = spreadsheet.get_worksheet(0) #to access the sheet by index. The first sheet should be 0 and so on.
    try: #get the dta from specific column but restrict in the len(rows) bc we don't want to mark a thousand empty lines.
        allDataInList = worksheet.get_all_values()
        num_rows = len(allDataInList) #to get how many lines/rows have data and we will restrict the marking stuff in this range.
        col_data = worksheet.col_values(2)  # column 'A' is 1, 'B' is 2, and so on.
        col_data +=[""]*(num_rows-len(col_data)) #Pad the list if it's shorter than num_rows

        cell_to_mark_empty=[] #to catch the cells which need to show there's no url
        cell_to_mark_broken=[]
        i=0
        for row, cell in enumerate(col_data, start=1):
            if not cell.strip():  # if the cell is empty or just spaces
                cell_location = rowcol_to_a1(row, 7)
                cell_to_mark_empty.append({
                    'range': cell_location,
                    'values': [["empty"]]
                })
                i=i+1
                print(i,"empty")
            else:
                the_link = re.search(r'https?:\/\/.*', cell)
                if the_link:
                    i=i+1
                    print(i)
                    is_broken=check_links_func(the_link.group())#this function will return true or false
                    if is_broken:
                        cell_location = rowcol_to_a1(row, 7)
                        cell_to_mark_broken.append({
                            'range': cell_location,
                            'values': [["broken"]]
                        })
                        print("broken")


        if cell_to_mark_empty:
            worksheet.batch_update([{
                "range":cell["range"], # the range in cell["range"] is the same as line 25, and it's a key word for line 25 so we can't rename it.
                "values":cell["values"] #same concept as last line
            }for cell in cell_to_mark_empty])
        if cell_to_mark_broken:
            worksheet.batch_update([
                {"range": cell["range"], "values": cell["values"]}
                for cell in cell_to_mark_broken
            ])




    except gspread.exceptions.APIError as e:
        print(f"An API error occurred: {e}")


except gspread.exceptions.SpreadsheetNotFound:
    print("Error: Spreadsheet not found. Check the ID and sharing permissions.")

