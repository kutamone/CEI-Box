import pygame
import csv
import datetime
import json
from pathlib import Path
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Project Hunt')
font = pygame.font.Font('freesansbold.ttf',24)
c = 0
c2 = -1
c3 = 0
c4 = 0
f = 0
scar = 0
menuvar = 0
scrollv = 0
scrollh = 0
mstacklen = 0
runtot = 0
tme = int(str(datetime.datetime.now())[8:10])
dte = int(str(datetime.datetime.now())[5:7])
fullstrline = []
fullstrlinet = []
mtfull = []
mfcost = []
mprofit = []
mstacklenl = []
curr = []
cardl = []
textwrite = ""
monthrecur = 55
monthincome = 250
csvtitle = "Food"
csvtitle2 = "Transportation"
graphtitle = "Monthly Profit"
graphtitle2 = "Monthly Cost"
graphtitle3 = f"Monthly {csvtitle}"
filepathm = str(Path('.').cwd())+"/month/" #only my computer line, note this when putting online
dat ={
'0':monthrecur, 
'1':monthincome, 
'2':csvtitle, 
'3':csvtitle2, 
'4':graphtitle, 
'5':graphtitle2, 
'6':graphtitle3, 
'color1':(0,0,0), 
'color2':(255,255,255),
'filepath':filepathm
}
misc = [dat['2'],dat['3']]
month = 30
dayavg = runtot / tme
projspent = (dayavg * (month - tme)) + runtot
amttospend = (dayavg *(month - tme))
projpl = (dat['1']-dat['0']) - projspent
currmonth = int(str(datetime.datetime.now())[5:7])
mstacklstmonth = 0
#settings load if file exists
try:
	with open('settings.json','r') as j:
		dat = json.load(j)
	print("Loading saved settings from settings.json...")
except FileNotFoundError as e:
	print("No settings.json detected, loading with default settings")
	pass
#dat dependent var reassignment
projpl = (dat['1']-dat['0']) - projspent
misc = [dat['2'],dat['3']]
#functionality functions lol
def rewrite():
	linecount = 0
	comparelst = []
	comparelstt = []
	with open('fmonth1.csv','r') as file:
		csvr = csv.DictReader(file)
		for line in csvr:
			comparelst.append(f"{line['Date']} {line['TransactionName']} {line['Cost']}")
		for i in comparelst:
			if i not in fullstrline:
				fullstrline.append(i)
	with open('tmonth1.csv','r') as file:
		csvr = csv.DictReader(file)
		for line in csvr:
			comparelstt.append(f"{line['Date']} {line['TransactionName']} {line['Cost']}")
		for i in comparelstt:
			if i not in fullstrlinet:
				fullstrlinet.append(i)			
def runny(fullstrline,f, txt): #here we can render multiple lines in a list simultaneously
	for i in range(0,len(fullstrline)):
		miscl = font.render(fullstrline[i], True, dat['color2'])
		screen.blit(miscl,(20,f))
		f += 50
	textr = font.render(f'| {textwrite}', True, dat['color2'])
	screen.blit(textr, (20,470))
def slider(misc,c): #here we can shift through items in a list with button/mouse input
	miscl = font.render(f"< {misc[c]} >", True, dat['color2'])
	x1 = 0
	if c == 0:
		x1 += 200
	if c == 1:
		x1 += 140
	screen.blit(miscl,(x1,375))
def adder(textwrite, c):
	if textwrite == "export":
		pass
	else:
		def lastspaceindex(textwrite):
			for i in range((len(textwrite)-1),0,-1):
				if not textwrite[i].isalpha() and not textwrite[i].isalnum():
					return i
		transactname = textwrite[:lastspaceindex(textwrite)]
		costamount = int(textwrite[lastspaceindex(textwrite):])
		if c == 0:
			with open('fmonth1.csv','a') as file:
				file.write(f'{str(datetime.datetime.now())[0:10]},{transactname},{costamount}\n')
		if c == 1:
			with open('tmonth1.csv','a') as file:
				file.write(f'{str(datetime.datetime.now())[0:10]},{transactname},{costamount}\n')
def menu(color1, color2):
	menuopts = ["View", "Reports", "Cards", "Data"]
	pygame.draw.rect(screen, dat['color2'], (25,30,225,225))
	pygame.draw.rect(screen, dat['color2'], (25,275,225,225))
	pygame.draw.rect(screen, dat['color2'], (275,30,225,225))
	pygame.draw.rect(screen, dat['color2'], (275,275,225,225))
	menuone = font.render(menuopts[0], True, dat['color1'])
	menutwo = font.render(menuopts[1], True, dat['color1'])
	menuthree = font.render(menuopts[2], True, dat['color1'])
	menufour = font.render(menuopts[3], True, dat['color1'])
	logotitle = font.render("CEI", True, dat['color2'])
	screen.blit(menuone, (25, 225))
	screen.blit(menutwo, (275, 225))
	screen.blit(menuthree, (25, 465))
	screen.blit(menufour, (275, 465))
	screen.blit(logotitle, (240,5))
def reports(data, scrollh, scrollv):
	x = 50
	y = 250
	numdatapoints = 6
	q = scrollh + numdatapoints
	s = len(data) // numdatapoints
	#plus scrollh until scrollh+numdatapoints > len(data) then scrollh = 0
	if len(data) == 0:
		screen.fill(dat['color1'])
		nodata = font.render("There is no data to display", True, dat['color2'])
		screen.blit(nodata,(100,250))
	else:	
		if scrollv == 0:
			xtitle = font.render(dat['4'], True, dat['color2'])
			ymid = font.render("0", True, dat['color2'])
			screen.blit(xtitle, (300,450))
			screen.blit(ymid, (25,y))
			for xi in range(scrollh,q):
				if xi == len(data):
					xi = 0
				pygame.draw.rect(screen, dat['color2'], (x,(y - data[xi]),10,10))
				re1 = font.render(f'{data[xi]}', True, dat['color2'])
				screen.blit(re1,(x,400))
				x += 75
		if scrollv == 1:
			xtitle = font.render(dat['5'], True, dat['color2'])
			screen.blit(xtitle, (300,450))
			y = 375
			for xi in range(scrollh,q):
				if xi == len(data):
					xi = 0
				pygame.draw.rect(screen, dat['color2'], (x,(y - data[xi]),10,(y-(y-data[xi]))))
				re1 = font.render(f'{data[xi]}', True, dat['color2'])
				screen.blit(re1,(x,400))
				x += 75
		if scrollv == 2:
			xtitle = font.render(dat['6'], True, dat['color2'])
			screen.blit(xtitle, (300,450))
			y = 375
			for xi in range(scrollh,q):
				if xi == len(data):
					xi = 0
				pygame.draw.rect(screen, dat['color2'], (x,(y - data[xi]),10,(y-(y-data[xi]))))
				re1 = font.render(f'{data[xi]}', True, dat['color2'])
				screen.blit(re1,(x,400))
				x += 75
def data(runtot, tme, monthincome, monthrecur, c3):
	flagold = False
	dayavg = runtot / tme
	projspent = (dayavg * (30 - tme)) + runtot #30 is going to be the number of days in a month for projections
	amttospend = (dayavg *(30 - tme)) #30 is going to be the number of days in a month for projections
	projpl = (monthincome - monthrecur) - projspent
	qpl = [sum(mprofit[i:i+3]) for i in range(0,len(mprofit)-1,3)]
	if c3 == 1:
		projtitle = font.render('Projections',True,dat['color2'])
		projline1 = font.render(f'Spend this month: {round(projspent,2)}', True, dat['color2'])
		projline2 = font.render(f'Left to spend this month: {round(amttospend,2)}', True, dat['color2'])
		projline3 = font.render(f'P/L: {round(projpl,2)}', True, dat['color2'])
		projline4 = font.render(f'Daily Avg Spent: {round(dayavg,2)}', True, dat['color2'])
		screen.blit(projtitle, (195,25))
		screen.blit(projline1, (20,100))
		screen.blit(projline2, (20,150))
		screen.blit(projline3, (20,200))
		screen.blit(projline4, (20,250))
	if c3 == 2:
		qrtrtitle = font.render("Quarterly P/L", True, dat['color2'])
		qrtrline1 = font.render(f'0', True, dat['color2'])
		rectangleadd = 250
		for i in range(0,len(qpl)):
			y = (i * 50) + 100 #some math
			if qpl[i] < 0:
				x = 150 + qpl[i]
				rawnum = qpl[i] * -1
				pygame.draw.rect(screen,dat['color2'],(x,y,rawnum,20))
				qrtrtag = font.render(f'{qpl[i]}',True,dat['color2'])
				screen.blit(qrtrtag, (x-40,y))
			else:
				x = 150
				tagpos = qpl[i] + x + 25
				pygame.draw.rect(screen, dat['color2'],(x,y,qpl[i],20))
				qrtrtag = font.render(f'{qpl[i]}',True,dat['color2'])
				screen.blit(qrtrtag, (tagpos,y))
		qrtrline2 = font.render(f'Monthly Avg P/L: {sum(mprofit)/len(mprofit)}', True, dat['color2'])
		qrtrline3 = font.render(f'Total Gain (Including Monthly): {sum(mprofit)}',True,dat['color2'])
		screen.blit(qrtrtitle, (195,25))
		screen.blit(qrtrline1, (250,50))
		screen.blit(qrtrline2, (20,300))
		screen.blit(qrtrline3, (20,350))
	#checks to make sure all entries in fmonth1 and tmonth1 are from the current month
	for line in fullstrline:
		if dte != int(line[5:7]):
			flagold += 1 
	for line in fullstrlinet:
		if dte != int(line[5:7]):
			flagold += 1 
	if flagold > 0:
		excep = font.render("Outdated Data, Inaccurate Projections", True, dat['color2'])
		screen.blit(excep,(25,450))
def exports2port(dat):
		ml = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
		lf = int(str(datetime.datetime.now())[5:7])
		currmonthf = f"f{ml[lf-2]}f.csv"
		currmontht = f"f{ml[lf-2]}t.csv"
		ll = []
		ll2 = []
		lc = []
		c = 0
		fc = 0
		tc = 0
		month = ''
		year = ''
		with open('fmonth1.csv','r') as file:
			csvr = csv.DictReader(file)
			for line in csvr:
				lc.append(line)
			for i in range(0,len(lc)):
				c += int(lc[i]['Cost'])
		with open('fmonth1.csv','r') as file: #copy operation for export
			for line in file:
				ll.append(line)
		with open('tmonth1.csv','r') as file:
			for line in file:
				ll2.append(line)
		with open(f"{dat['filepath']}{currmonthf}",'w') as file:#note that the file path will be different for other users
			for line in ll:
				file.write(line)
		with open(f"{dat['filepath']}{currmontht}",'w') as file:
			for line in ll2:
				file.write(line) #new file export operation conclusion
		print(f"Current expense reports exported as {currmonthf} and {currmontht} to the month folder")
		with open('fmonth1.csv','r') as f: #creating dict for mstack
			csvr = csv.DictReader(f)
			for line in csvr:
				fc += int(line['Cost'])
				month = str(line['Date'])[5:7]
				year = str(line['Date'])[2:4]
		with open('tmonth1.csv','r') as f:
			csvr = csv.DictReader(f)
			for line in csvr:
				tc += int(line['Cost'])
		costco = {'FTotals':fc, 'TTotals':tc, 'Full': (fc + tc)} #dict creation complete
		with open('mdatarecord.json','w') as j:
			dat = json.dumps(costco)
			j.write(dat)
		with open('mdatarecord.json','r') as j:
			mdat = json.load(j)
		with open('mstack.csv','a') as f:
			f.write(f'{month},{year},{mdat["FTotals"]},{mdat["TTotals"]},{mdat["Full"]}\n')
		print("mstack.csv and mdatarecord.json updated...\n")
		print("For the following question, please press y or press n, then press enter")
		wipe = input("Would you like to reset fmonth1.csv and tmonth1.csv? [y/n]: ")
		if wipe == 'y':
			with open('fmonth1.csv','w') as f:
				f.write('Date,TransactionName,Cost')
			with open('tmonth1.csv','w') as f:
				f.write('Date,TransactionName,Cost')
def exportm(textwrite):
	if textwrite == "export":
		exports2port(dat)
def cardz(c2, c4):
	cardl = ["Fire Trex", "Water Trex", "Steel Trex","Thunder Trex"] #placeholder intro cards, to be replaced by live update
	c2 += 2
	if c2 >= 0 and c2 <= 4:
		cmod = c2 * 100
		pygame.draw.rect(screen,dat['color2'],(25,25 + cmod,200,50))
	for i in range(0,4):#max card spots is 4
		ymod = i*100
		if cmod == ymod: #non selected card changes text color to white
			cardlshow = font.render(cardl[i], True, dat['color1'])
		else:
			cardlshow = font.render(cardl[i], True, dat['color2'])
		screen.blit(cardlshow,(25,ymod + 25))
#basic loading stuff
with open("cardlistpc.txt","r") as file:
	for line in file:
		cardl.append(line.strip('\n'))
with open("fmonth1.csv","r") as file:
	csvr = csv.DictReader(file)
	for line in csvr:
		fullstrline.append(f"{line['Date']} {line['TransactionName']} {line['Cost']}")
		curr.append(line['Cost'])
		runtot += int(line['Cost'])
with open("tmonth1.csv","r") as file:
	csvr = csv.DictReader(file)
	for line in csvr:
		fullstrlinet.append(f"{line['Date']} {line['TransactionName']} {line['Cost']}")
		runtot += int(line['Cost'])
with open("mstack.csv","r") as file:
	csvr = csv.DictReader(file)
	for line in csvr:
		cost = int(line['TFull']) + dat['0']
		fcost = int(line['FCost'])
		profit = dat['1'] - cost
		mtfull.append(cost)
		mfcost.append(fcost)
		mprofit.append(profit)
		mstacklen += 1
	if mstacklen > 1:
		mstacklstmonth += int(line['Month'][-1])
#automatic exporting at the beginning of the next month
if currmonth - mstacklstmonth == 2:
	exports2port(dat)
elif currmonth - mstacklstmonth == -10:
	if currmonth == 1 and mstacklstmonth == 11:
		exports2port(dat)
	if currmonth == 2 and mstacklstmonth == 12:
		exports2port(dat)
elif currmonth - mstacklstmonth == 1:
	print("Export will be automatically conducted at the beginning of the next month")
else:
	print("Invalid export scenario")
#basic loading stuff end
run = True	
while run:
	mx,my = pygame.mouse.get_pos()
	screen.fill(dat['color1'])
	click1 = pygame.Rect(25,30,225,225)
	click2 = pygame.Rect(275,25,225,225)
	click3 = pygame.Rect(30,275,225,225)
	click4 = pygame.Rect(275,275,225,225)
	if menuvar == 0:
		menu(dat['color2'], dat['color1'])
	elif menuvar == 1:
		if c == 0:
			runny(fullstrline,f, textwrite)
		if c == 1:
			runny(fullstrlinet,f, textwrite)
		slider(misc,c)
		scar = True #little system for exiting out of this space
	elif menuvar == 2:
		if scrollv == 0:
			reports(mprofit, scrollh, scrollv)
		if scrollv == 1:
			reports(mtfull, scrollh, scrollv)
		if scrollv == 2:
			reports(mfcost, scrollh, scrollv)
	elif menuvar == 3:
		screen.fill(dat['color1'])
		cardz(c2,c4)
	elif menuvar == 4:
		data(runtot, tme, monthincome, monthrecur, c3)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.TEXTINPUT:
			if menuvar == 1:
				textwrite += event.text
		if event.type == pygame.KEYDOWN:
			if menuvar == 1:
				if event.key == pygame.K_BACKSPACE:
					textwrite = textwrite[:-1]
				if event.key == pygame.K_RETURN:
					exportm(textwrite)
					adder(textwrite,c)
					print(c)
					textwrite = ""
					rewrite()
		if event.type == pygame.MOUSEBUTTONDOWN:
			#main menu options
			if click1.collidepoint(mx,my) and menuvar == 0:
				menuvar += 1 
				#print(menuvar)
				if scar:
					scar = False
			if click2.collidepoint(mx,my) and menuvar == 0:
				menuvar += 2
				#print(menuvar)
			if click3.collidepoint(mx,my) and menuvar == 0:
				menuvar += 3
				#print(menuvar)
			if click4.collidepoint(mx,my) and menuvar == 0:
				menuvar += 4
				#print(menuvar)
			if click1.collidepoint(mx,my) and scar:
				menuvar -= menuvar
			#View section options
			if not click1.collidepoint(mx,my) and menuvar == 1:
				if c == (len(misc)-1):
					c -= (len(misc)-1)
				else:
					c += 1
			#Report section options
			if click4.collidepoint(mx,my) and menuvar == 2:
				if scrollh < (mstacklen-6):#(mstacklen - 6) when we have more lines than 6, so next month (needs to be tested for 12 months)
					scrollh += 1
				else:
					scrollh -= scrollh
			if click3.collidepoint(mx,my) and menuvar == 2:
				if scrollv < 2:
					scrollv += 1
				else:
					scrollv -= scrollv
			if click1.collidepoint(mx,my) and menuvar >= 2:
				menuvar -= menuvar
			#Cardz section options
			if click4.collidepoint(mx,my) and menuvar == 3:
				if c2 < 1:
					c2 += 1
			if click3.collidepoint(mx,my) and menuvar == 3: #c2 is bounds of white rectangle, c4 being list scroll
				if c2 > -2:
					c2-=1
			#Data section options
			if click4.collidepoint(mx,my) and menuvar == 4:
				if c3 >= 2:
					c3 -= 1
				else:
					c3 += 1
			if click3.collidepoint(mx,my) and menuvar == 4:
				if c3 <= 1:
					c3 += 1
				else:
					c3 -= 1
	pygame.display.update()
pygame.quit()
'''the plan
click on date, edit date?
two very powerful techniques shown above for sure
'''
