# This is a project to check all the WhatsApp broken links in spreadsheet.

## Idea
Any broken WhatsApp links have the same picture which is made by WhatsApp. 
In this case, we only need to check if the links have that picture by bt4 img src="https://static.whatsapp.net/rsrc.php/v4/yB/r/_0dVljceIA5.png".
If it contains this picture, it means the link is broken.

### Step by step:
1. Using bt4 to check if the links contain the picture.
2. Using Google Console (Service account) to access the documents(Google spread sheet) we need. After connect it, we can use the google library in Pycharm. **detail [1]


### Dtails:
**[1]: we need to share the document with the Sevice account email as an editor. 
