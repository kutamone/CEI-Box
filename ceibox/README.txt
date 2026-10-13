Project Hunt v0.0.1

required modules:
pygame
built-in (csv,json,datetime)

:updated 9-23-26

Visualize collected financial information in this handy application.
The interface is divided into four clickable quadrants.

Click View - view data from fmonth1.csv and tmonth1.csv
\\Clicking top left corner returns to menu
\\Clicking anywhere else scrolls between each csv
\\Type to append the currently visualized csv with the format of "[TransactionName] [Cost(as an integer)]" and press Enter to update
\\Type "export" and press Enter to manually save recorded data from fmonth1.csv and tmonth1.csv to the month folder, update mdatarecord.json, and add a line to mstack.csv
Click Reports - view data from mstack.csv
\\Clicking top left corner returns to menu
\\Clicking bottom left corner changes the selected graph
\\Clicking bottom right corner scrolls to most recent graph data
Click Data - view projection data based on fmonth1.csv and tmonth1.csv
\\Clicking top left corner returns to menu

csv Formatting Template

fmonth1.csv and tmonth1.csv
----------------------------
Date,TransactionName,Cost
YYYY-MM-DD,GroceryStore,99

mstack.csv
----------
Month,Year,FCost,TCost,TFull
MM,YY,99,99,198

Colors

By editing the settings.json file, and entering RGB values, you may change the menu's colors from the default black and white ((0,0,0) and (255,255,255))

'color1': (###,###,###)
'color2': (###,###,###)

Settings

If there are any errors with the settings.json file, please attempt to reinstall from the start (remove files relevant to this install) and run the setup.py file again. ceihunt.py is dependent on settings.json being located in the same folder to boot preloaded settings from setup.py.

Install Instructions

Note: run files from within the main folder
Step 1: run the setup.py once
Step 2: run the ceihunt.py

Usage Instructions

Utilize the view section to update each csv (fmonth1.csv, tmonth1.csv) with your latest recorded purchases
Note: fmonth1.csv and tmonth1.csv entries must all be from the same month for Projections to work
Utilize the data section to view information on the current month's projected financial results
At the end of the month, "export" once to append financial data for that month to mstack.csv
At the end of the month, wipe your fmonth1.csv and tmonth1.csv (after exporting) to start recording purchases from the new month
Note: Exports are conducted automatically by default on the first launch of the new month
Once your mstack.csv has grown over a period of months, view monthly data in the reports section



*in development:
can export data to month folder on the 1st of the month, seeking manual file path update ability
preset data clearing for non-me users, monthrecur, monthincome, csvs
setup.py for graphs (proportions for those with large income)
