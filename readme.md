# Google Sheet Output General
This is a package for handling versions of google sheet api scripts.  I would like to evolve this code from the most primative actions with the api to more avanced ones and port this code around to multiple projects
## 1. Dependencies
Make sure the envrionment has all of what is in requirements.txt
## 2. Plug in Client Secrets
Go to the google dev console, set up your project with oauth Credentials, and download the client secrets file.  Move your client_secrets.json to the runtime directory.
## 3. Enable API
Be sure the google sheets API is enabled before use for the project

## Usage
import GoogleSheetOutput.sheetOutput as gso
sheet = gso.SheetOutput(spreadSheetId=[your-spreadsheet-id], 
                        sheetName=[name-of-spreadsheet-tab], 
                        lastColumn='AA')
