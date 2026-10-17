def outofbox():
	try: 
		import pygame
		import csv
		import datetime
		import json
		from pathlib import Path
		print("If you fail to complete the setup, please remove files relevant to this install, and try again :)")
		print("For each of the following entries, enter a whole number integer and then press enter")
		monthrecur = int(input("Enter the sum total of your monthly recurring payments as a single integer ex. subscriptions: "))
		monthincome = int(input("Enter the sum total of your monthly income as a single integer: "))
		print("For each of the following entries, type a name of your choosing")
		csvtitle = input("Enter spending category name: ")
		csvtitle2 = input("Enter second spending category name: ")
		graphtitle = input("Enter graph title name (Monthly Profit): ")
		graphtitle2 = input("Enter graph title 2 name (Monthly Cost): ")
		graphtitle3 = input("Enter graph title 3 name (Monthly [Primary Spending Category]): ")
		print("For automatic exports to work, provide the file path to the month folder")
  print("For your convenience, the month folder is automatically detected by utilizing this file's location as the current working directory")
  print("Simply, reply n to the following question to set the month folder's filepath automatically")
		finput = input("Would you like to manually input filepath to month folder? [y/n]: ")
		if finput == "y":
			print("ex:[/home/thomas/program/liquidwrld2/month/]")
			filepathm = input("Please input the full file path to the month folder: ")
		else:
			p = Path('.')
			filepathm = str(p.cwd())+'/month/'
		with open('settings.json','w') as j:
			sd = {'0':monthrecur, 
			'1':monthincome, 
			'2':csvtitle, 
			'3':csvtitle2, 
			'4':graphtitle, 
			'5':graphtitle2, 
			'6':graphtitle3, 
			'color1':(0,0,0), 
			'color2':(255,255,255),
			'filepath':filepathm}
			dat = json.dumps(sd)
			j.write(dat)
		print("\n ---- Setup successful :) ----\n")
		with open('fmonth1.csv','w') as f:
			f.write('Date,TransactionName,Cost\n')
		with open('tmonth1.csv','w') as f:
			f.write('Date,TransactionName,Cost\n')
		with open('mstack.csv','w') as f:
			f.write('Month,Year,FCost,TCost,TFull\n')
		print("To quickly boot and understand ceihunt.py,\n you can use preset data to fill the given csv files with properly formatted data.")
		print("This provides a template to understand how to use the csv files to view data")
		print("Note: the data section's Projections are based on the current numbered day of the week, sample data may cause inaccurate projections")
		sampdataq = input("Load Sample Data? [y/n]: ")
		if sampdataq == "y":
			with open('fmonth1.csv','a') as f:
				for i in range(1,9):
					if 3*i > 9:
						f.write(f'2022-09-{3*i},SampleStore,{10*i}\n')
					else:
						f.write(f'2022-09-0{3*i},SampleStore,{10*i}\n')
			with open('tmonth1.csv','a') as f:
				for i in range(1,9):
					if 3*i > 9:
						f.write(f'2022-09-{3*i},PublicTransportation,{10*i}\n')
					else:
						f.write(f'2022-09-0{3*i},PublicTransportation,{10*i}\n')
			with open('mstack.csv','a') as f:
				for i in range(1,9):
					f.write(f'0{i},2022,{int(360)},{int(360)},{int(720)}\n')
	except ModuleNotFoundError as e:
		print("Please install pygame to continue or check to make sure required modules are installed")
		print(": csv, datetime, json, pygame")
		#try a [sd[str(i)] for i in range(0,7)] note to self
outofbox()
#Step 1: run the setup.py once
#Step 2: run the ceihunt.py
