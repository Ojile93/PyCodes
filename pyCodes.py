import numpy as np
import pandas as pd
import os

# Start of Jss2A variable declaration
js3A = np.array(["Abah Serah","Ademu Emmanuel","Agada Rose","Agada Destiny","Agada Serah","Agbo Happiness","Agbo Ruth","Agbo ThankGod","Ameh Anthony","Anthony Precious","Damion Donatus","David James","Dele Friday","Eibo Lucia","Elias Ladi","Eze Faith","Emmanuel Peace","Fredrick Oscar","Friday Samson","Innocent Angela","Itodo Joy","James Bridget Ene","John Gabriel","John peace","Lawrence Peter","Mathew Victor","Onuh Emmanuel","Onyeke MaryJoy","Ogwuche Patience","Ozor Maryann","Ogwuche Victory","Ogwuche Daniel","Onuh Agnes","Okpe John","Ocheka Daniel","Onoja Sunday","Onuh Michael","Onah Amarachi Grace","Paul Friday","Samuel Donatus","Ugwoke Emmanuel","Ubasi Godday","Victor Praise","Adama Blessed"])
js3B =np.array(["Abraham Bassey","Adache Joel","Ameh Cynthia","Ameh Janet","Attah James","Adikwu Angela","Benjamin David","Bernard Emmanuel O.","Daniel Ene Elizabeth","Daniel Linus","Dio Deborah","Daniel Mathew","Agada Ene Queen","Emmanuel Ameh","Elachi Peter","Emmanuel Gabriel","Emmanuel Wonder","Eneche Victory","Enemari Francis","Gabriel Peter","Gabriel Fredrick","Gabriel Margareth","Itodo David","Idoko Patrick","Itodo Suzan","Itodo Faith Ada","John Gift Enewa","John Daniel","John Stephen","John Esther","Kingley Christian","Kenneth Friday O","Godwin Ladi Joy","Gabriel Eleojo Fedilia","Kenneth Oloja","Michael Joshua","Odugbo Adeyi Ezekiel","Ogbe Kingsley","Okpe Favour","Onche Bright Sylvanus","Onoja Success","Sunday Favour","Ugwu Emmanuel","Itodo Ehi Joy","Sunday Williams","James Oche Godwin","John Isaiah","Olofu Godwin","Agada Destiny","Mathias Anthony","Simon Anthonia"])

js2B =np.array(["Anawo Helen","Micheal Rita","Pius Gabriel","Akogwu Godwin","Akogwu Godwin Isaiah","Isaiah Ene First","Christopher Rita","Emmanuel Ogbene Mary","Friday Peace","Micheal James Aduma","Ogbada Peter","Moses Precious","Ogbe Paulina","Adeshino Joshua","Jacob Samson","Idoko Juliana","Odoh Joy","Abah Favour","Johnson Patience","Agada Alice","John Esther","Raphael Veronica","Mathias Patrick","Okpe Agatha","Oche Agnes O","Okoko Faith","Oche Frank","Sunday Destiny","Robert Victor","Agbo Emmanuel","Onaji Joshua","Damion Glory","Anthony Bright","Abarike Charity","Bernard Grace Ihotu","Moses Esther","Idoko Destiny","Agbaje David","Onoja Dominion","Edoka Bright E","Adejo Prince","Abdul Maimuna","Monday Micheal"])
js2B.sort()
js2A = np.array(["Adikwu Susan","Agada Ben","Agada Oche Abraham","Agbo peace Ochanya","Ayebe Alex","Ameh Destiny","Enenche Jennifer","Egili Maryann","Ejeh peace","Eze Perpetual","Gabriel Samuel","Idoko Grace","Igba Esther","Gabriel Judith","Jonah Susan","Joseph Deborah","Ochigbo Dominion ","Ocheme Ehi Favour","Enenche Peter","Innocent Juliet","Ameh ThankGod Wisdom","Ejema Favour","Emmanuel Peace","Ojile Prince","Itodo Peter","Orokpo Apeh Isaac","Ogwuche Destiny","Onche Annointed","Ojoh Okpeka","Gabriel Christian","Monday Destiny","Onuh Emmanuel","Ogoyi Happiness","Sunday Elizabeth","Micheal Lilian","Sunday Comfort","Sunday Ihotu Deborah","Ogwuoke Esther","Nnadi Ben","Udeh Veronica","Ugwu Blessing","Okoko Favour","David Blessing J","Ameh Daniel Enenche"])
js1A = np.array(["Wilfred Uchenna","Udeh God'swill","Athony Serah","Eze Chiemere","Dele Kehinde","Agbo Emmanuel","Oche Nathaniel Michael","Jonathan Peace","Abutu Favour","Sunday Innocent","Peter Sonia","Ameh Adaofoyi E","Michael Comfort","James Peter","Emmanuel Veronica","Adoyi Perculiar","Henry Anthony","Gabriel Valentina","Bernard Victor","John Ochanya Divine","Agbo Goodluck","Ogwuche Ijewanu M","Oche Onoja J","Ojile Jessica","Dele Taiwo","Mathias Gabriel","James Deborah","John Ikayi V","Godwin Oloche","Idoko Gift","Ameh Stephen","Onoja Emmanuella","Joseph Glory","Clement Mathew"])
js1B = np.array(["Abah Jenifer","Adole Jerusha","Adah Frieda","Agbo Kingley","Audu Marvelous","Akor Godfrey","Adukwu Rita","Ajunwa Anna","Agada Covenant","Bernard Faith","David Mary","Ejeh Rebecca","Emmanuel Anthonia","God's Power Oche Sule","Goodluck Samuel Okpe","Godwin Favout","Isaiah Jecinta","Innocent Daniel","Ojile Godwin Joseph","Job Destiny","John Alex","Nnadi John","Ohemu Jecinta","Onuh Zachariah","Okoh Peter","Oliver Rejoice","Pius Alice","Philip Jonathan","Samuel Favour","Simon Jonathan","Ugwu Ebube","Audu Elizabeth","Odugbo Destiny","Oche Jacob Linus"])

test1 =["Ojile","Naomi"]

def welcome():
    print("Welcome to Students Grading Machine! \n \n")
#print(len(js2B))
df = pd.read_csv("js2bfinal.csv")
dt = df[["S/N","Marks Obtained","Position"]]
dt.set_index("S/N",inplace = True)
print(dt)
cont=0
for index,row in dt.iterrows():
    if row["Grades"]=="E":
        cont=cont+1
    #print(cont)
#print("\n"+str(cont)+" number of students failed")
welcome()
def options():
	
	choice = input('Choose from the options the task you wish to perform: \n1: Compute Junior session  Score sheet \n2: Compute other class Score sheet \n3: Compile Grades and Position for already Compiled Results:\n4: Form Mistress/Master Corner \n5: Exit the Grading Machine\n \nEnter your preference:  ')
	if choice == "1":
			os.system("clear")
			js2A_sheet()
			inj = input("Do you wish to perform another task 'y' or 'no' ")
			if inj == 'y':
				options()
			exit()
	elif choice == "2":
					os.system("clear")
					stdData()
					inj2 = input("Do you wish to perform another task? 'y' or 'n' ")
					if inj2 == "y":
						options()
					exit()
	elif choice == "3":
		os.system("clear")
		computation()
	elif choice == "4":
		os.system("clear")
		classPosition()
	elif choice == "5":
			exit()
	else:
			print("\nWRONG INPUT!\n")
			options()
	

def classPosition():
	subjects = ["Math", "Eng", "SOS","CRS", "Civic Edu.", "B.Science","B.Tech","Bus. Std","Agric","Computer ","History","H. MGT","PHE"]
	print("Select Class you wish to Compute grade for")
	def selClass():
		classSel = input("1. JSS1A\n2. JSS1B\n3. JSS2A\n4. JSS2B\n5. JSS3A\n6. JSS3B ")

		if classSel == "1":
			global names
			names = test1
			global classNam
			classNam = "JSS 1A"
		elif classSel == "2":
			names = js1B
			classNam = "JSS 1B"
		elif classSel == "3":
			names = js2A
			classNam = "JSS 2A"
		elif classSel == "4":
			names = js2B
			classNam = "JSS 2B"
		elif classSel == "5":
		    names = js3A
		    classNam = "JSS 3A"
		elif classSel =="6":
		    names = js3B
		    classNam = "JSS 3B"
		else:
			print("WRONG! input")
			selClass()
	selClass()
	
	
	sn = [x for x in range(1,len(names)+1)]
	
	mCAT = []
	mEXM =[]
	mTOT = []
	eCAT = []
	eEXM =[]
	eTOT =[]
	sCAT=[]
	sEXM=[]
	sTOT=[]
	crCAT =[]
	crEXM =[]
	crTOT =[]
	cCAT =[]
	cEXM =[]
	cTOT =[]
	bCAT=[]
	bEXM=[]
	bTOT = []
	btCAT =[]
	btEXM =[]
	btTOT =[]
	bsCAT =[]
	bsEXM =[]
	bsTOT =[]
	aCAT =[]
	aEXM =[]
	aTOT =[]
	coCAT =[]
	coEXM =[]
	coTOT =[]
	hCAT =[]
	hEXM =[]
	hTOT =[]
	hmCAT =[]
	hmEXM =[]
	hmTOT =[]
	pCAT =[]
	pEXM =[]
	pTOT =[]
	ccCAT=[]
	ccEXM=[]
	ccTOT=[]
	nwNam =[]
	nwSn = []
	
	
	subdic ={("Names",""):nwNam,("Math", "CAT"):mCAT,("Math","Exams"):mEXM,("Math","Total"):mTOT,("Eng","CAT"):eCAT,("Eng","Exams"):eEXM,("Eng","Total"):eTOT, ("SOS","CAT"):sCAT, ("SOS","Exams"):sEXM,("SOS","Total"):sTOT,("Civic","CAT"):cCAT,("Civic","Exams"):cEXM,("Civic","Total"):cTOT,("CRS","CAT"):crCAT, ("CRS","Exams"):crEXM, ("CRS","Total"):crTOT, ("B.sci","CAT"):bCAT,("B.sci","Exams"):bEXM,("B.sci","Total"):bTOT,("B.tech","CAT"):btCAT,("B.tech","Exams"):btEXM,("B.tech","Total"):btTOT,("B.std","CAT"):bsCAT,("B.std","Exams"):bsEXM,("B.std","Total"):bsTOT,("Agric","CAT"):aCAT,("Agric","Exam"):aEXM,("Agric","Total"):aTOT,("Comp","CAT"):coCAT,("Comp","Exams"):coEXM,("Comp","Total"):coTOT,("History","CAT"):hCAT,("History","Exams"):hEXM,("History","Total"):hTOT,("H.MGT","CAT"):hmCAT,("H.MGt","Exams"):hmEXM,("H.MGT","Total"):hmTOT,("CCA","CAT"):ccCAT,("CCA","Exams"):ccEXM,("CCA","Total"):ccTOT}
	
	dic1 = {("Math"):mTOT,("Eng"):eTOT,("SOS"):sTOT,("Civic"):cTOT,("B. science"):bTOT,("B. tech"):btTOT,("CRS"):crTOT,("Agric"):aTOT,("B. std"):bsTOT,("COMP"):coTOT,("History"):hTOT,("H. mgt"):hmTOT,("CCA"):ccTOT,("PHE"):pTOT}
	
	dic2 = {"S/N":sn,"Names":names}
	
	tab = pd.DataFrame(dic2)
	
	"""for index,row in tab.iterrows():
					def getScr():
						try:
							print("Enter score details for, Name: ",row["Names"],"\nReg no: ",row["S/N"])
							global mCa
							mCa = float(input("Enter Math  Total CA scores: "))
							global mEx
							mEx = float(input("Enter Math Exam score: "))
							global mTo
							mTo = mCa + mEx
							global eCa
							eCa = float(input("Enter English Total CA Score: "))
							global eEx
							eEx = float(input("Enter English Exam score: "))
							global eTo
							eTo = eCa + eEx
							global cSo
							cSo = float(input("Enter Social Studies Total CA score: "))
							global eSo
							eSo = float(input("Enter Social Studies Exam Score: "))
							global sTo
							sTo = cSo + eSo
							global cCr
							cCr = float(input("Enter CRS Total CA score: "))
							global eCr
							eCr = float(input("Enter CRS Exam Score: "))
							global crTo
							crTo = cCr + eCr
							global cCi
							cCi = float(input("Enter Civic Edu. Total CA Score: "))
							global eCi
							eCi = float(input("Enter Civic Edu. Exam score: "))
							global cTo
							cTo = cCi + eCi
							global cBs
							cBs = float(input("Enter Basic Science Total CA Score: "))
							global eBs
							eBs = float(input("Enter Basic Science Exam Score: "))
							global bTo
							bTo = cBs + eBs
							global cBt
							cBt = float(input("Enter Basic Tech Total CA Score: "))
							global eBt
							eBt = float(input("Enter Basic Tech Exam Score: "))
							global btTo
							btTo = cBt + eBt
							global cBst
							cBst = float(input("Enter Business Studies Total CA scores: "))
							global eBst
							eBst = float(input("Enter Business Studies Exam Scores: "))
							global bsTo
							bsTo = cBst + eBst
							global cAg
							cAg = float(input("Enter Agric Total CA scores: "))
							global eAg
							eAg = float(input("Enter Agric Exam scores: "))
							global aTo
							aTo = cAg + eAg
							global cCo
							cCo = float(input("Enter Computer Total CA scores: "))
							global eCo
							eCo = float(input("Enter Computer Exam scores: "))
							global coTo
							coTo = cCo + eCo
							global cHi
							cHi = float(input("Enter History Total CA scores: "))
							global eHi
							eHi = float(input("Enter History Exam scores: "))
							global hiTo
							hiTo = cHi + eHi
							global cHm
							cHm = float(input("Enter Home Management Total CA scores: "))
							global eHm
							eHm = float(input("Enter Home Management Exam scores: "))
							global hmTo
							hmTo = eHm + cHm
							global cPh
							cPh = float(input("Enter PHE Total CA scores: "))
							global ePh
							ePh = float(input("Enter PHE Exam scores: "))
							global phTo
							phTo = cPh + ePh
							global cCA
							cCA = float(input("Enter CCA Total CA scores: "))
							global eCA
							eCA = float(input("Enter CCA Exam scores: "))
							global tCA
							tCA = cCA+eCA
							global newNa
							newNa = row["Names"]
							global newSn
							newSn = row["S/N"]
						except:
							print("\nWRONG! Input! input should be number\n")
							getScr()
					getScr()
					nwNam.append(newNa)
					nwSn.append(newSn)
					mCAT.append(mCa)
					mEXM.append(mEx)
					mTOT.append(mTo)
					eCAT.append(eCa)
					eEXM.append(eEx)
					eTOT.append(eTo)
					sCAT.append(cSo)
					sEXM.append(eSo)
					sTOT.append(sTo)
					crCAT.append(cCr)
					crEXM.append(eCr)
					crTOT.append(crTo)
					cCAT.append(cCi)
					cEXM.append(eCi)
					cTOT.append(cTo)
					bCAT.append(cBs)
					bEXM.append(eBs)
					bTOT.append(bTo)
					btCAT.append(cBt)
					btEXM.append(eBt)
					btTOT.append(btTo)
					bsCAT.append(cBst)
					bsEXM.append(eBst)
					bsTOT.append(bsTo)
					aCAT.append(cAg)
					aEXM.append(eAg)
					aTOT.append(aTo)
					coCAT.append(cCo)
					coEXM.append(eCo)
					coTOT.append(coTo)
					hCAT.append(cHi)
					hEXM.append(eHi)
					hTOT.append(hiTo)
					hmCAT.append(cHm)
					hmEXM.append(eHm)
					hmTOT.append(hmTo)
					pCAT.append(cPh)
					pEXM.append(ePh)
					pTOT.append(phTo)
					ccCAT.append(cCA)
					ccEXM.append(eCA)
					ccTOT.append(tCA)
					agTab = pd.DataFrame(subdic,index = nwSn)
					print(agTab)"""
	exTOT = []
	newAr = []
	def getTot():
		for a, b, c,d,e,f,g,h,i,j,k,l,m,n in zip(mTOT, eTOT,sTOT,crTOT,cTOT,bTOT,btTOT,bsTOT,aTOT,coTOT,hTOT,hmTOT,pTOT,ccTOT):
			tots = a+b+c+d+e+f+g+h+i+j+k+l+m+n
			exTOT.append(tots)
		avArr = [x/14 for x in exTOT]
		agTab[("Marks Obtained")] = exTOT
		agTab[("Average")] = avArr
		for index, row in agTab.iterrows():
			x = row[("Marks Obtained")]
			newAr.append(x)
		newAr.sort(reverse = True)
		count = 0
		newAr2 =[]
		newPos = []
		for x in newAr:
			count = count + 1
			if x not in newAr2:
				newAr2.append(x)
				newPos.append(count)
		posDic = dict(zip(newAr2,newPos))
		def posMap(value):
			for score, pos in posDic.items():
				if value == score:
					return pos
		tabl = agTab[("Marks Obtained")].map(posMap)
		agTab[("Position")] = tabl
		print(agTab)
	#getTot()
			
	def savTab():
	    savTable = input("\nEnter 'y' to save this this Table to your local device storage and 'n' to exit without saving\n")
	    if savTable == "y":
	        try:
	            tabNam = input("\n Please enter your preferred Table name: ")
	            agTab.to_csv(tabNam + ".csv")
	            print("Your table has been saved successfuly as "+ tabNam +".csv")
	        except:
	            print("Table not saved")
	            savTab()
	    elif savTable == "n":
	        options()
	    else:
		    options()
	def sim():
	    for index, row in tab.iterrows():
	        def getot():
	            try:
	                 print("Enter score details for ",row["Names"]," with Reg no.",row["S/N"])
	                 global Eto
	                 Eto = float(input("Enter English Total scores: "))
	                 global Mto
	                 Mto = float(input("Enter Math Total scores: "))
	                 global Cto
	                 Cto = float(input("Enter Civic Education Total Scores: "))
	                 global Sto
	                 Sto = float(input("Enter Social Studies Scores: "))
	                 global Bto
	                 Bto = float(input("Enter Basic Science Total Scores: "))
	                 global BTto
	                 BTto = float(input("Enter Basic Tech Total scores: "))
	                 global Ato
	                 Ato = float(input("Enter Agric Total scores: "))
	                 global Hto
	                 Hto = float(input("Enter Home mgt. Total scores: "))
	                 global HIto
	                 Hto = float(input("Enter History Total scores: "))
	                 global CRto
	                 CRto = float(input("Enter CRSTotal scores: "))
	                 global Pto
	                 Pto = float(input("Enter PHE Total scores: "))
	                 global CCto
	                 CCto = float(input("Enter CCA total scores: "))
	                 global COto
	                 COto = float(input("Enter Computer Total scores: "))
	                 global BUto
	                 BUto = float(input("Enter Business Studies total scores: "))
	                 os.system("clear")
	            except:
	                 print("WRONG INPUT!!")
	                 getot()
	        getot()
	        eTOT.append(Eto)
	        mTOT.append(Mto)
	        sTOT.append(Sto)
	        cTOT.append(Cto)
	        crTOT.append(CRto)
	        bTOT.append(Bto)
	        btTOT.append(BTto)
	        bsTOT.append(BUto)
	        aTOT.append(Ato)
	        coTOT.append(COto)
	        hmTOT.append(Hto)
	        hTOT.append(HIto)
	        ccTOT.append(CCto)
	        pTOT.append(Pto)
	        global agTab
	        agTab=pd.DataFrame(dic1)
	        print(agTab)
	    getTot()
	    savTab()
	sim()
	              
	            
	
def computation():
	grades ={70:"A",60:"B",50:"C",40:"D",0:"E"}

	wf = input("Enter file name: ")
	try:
		ipt = pd.read_csv(wf)
	except:
			print("File name is INCORRECT!")
			wf = input("Enter file name: ")
			ipt = pd.read_csv(wf)
	print(ipt)
	opt = input("Please to provide grade, column to map through is needed\nEnter column name to map through: ")
	def grade_map(value):
		for key, letter in grades.items():
			if value >= key:
				return letter
	ipt2 = ipt[opt].map(grade_map)
	ipt["Grades"] = pd.Categorical(ipt2, ordered = True)
	pTotal = []
	for index, row in ipt.iterrows():
		tot = row[opt]
		pTotal.append(tot)
	pTotal.sort(reverse = True)

	count = 0
	arTotal = []
	arPos = []
	for x in pTotal:
			count = count + 1
			if x not in arTotal:
				arTotal.append(x)
				arPos.append(count)
	posDic = dict(zip(arTotal,arPos))
	def mp(value):
				for score, pos in posDic.items():
					if value == score:
						return pos
	tab3 = ipt[opt].map(mp)
	#ipt["Grades"] = pd.Categorical(ipt2, ordered = True)
	ipt[("Position")] = tab3
	
	print(ipt)
	def sav():
	    print("To save this table enter 'y' and any other button to exit without saving? ")
	    sav = input()
	    if sav =="y":
	        na = input("Enter your prefered table name:\n ") 
	        ipt.to_csv(na+".csv")
	    else:
	        options()
	sav()
	        
#computation()



def stdData():
	nam = []
	id = []
	arCa1 = []
	arCa2 = []
	arCa3 = []
	arCat = []
	arExm = []
	arTotal = []
	try:
		stdNo = int(input("Enter no. of Students: "))
		print("\nCompute  details for your students:\n")
	except:
		print("INVALID input!, Input should be number")
		stdNo = int(input("Enter no. of Students: "))
	for x in range(0,stdNo):
				def ipTak():
						try:
							global stdName
							stdName = input('Enter Student Name: ')
							global stdId
							stdId = float(input("Enter Student Reg no. "))
							global stdCa1
							stdCa1 = float(input('Enter First Test scores: '))
							global stdCa2
							stdCa2 = float(input('Enter Second Test Scores: '))
							global stdCa3
							stdCa3 = float(input('Enter Third Test Scores: '))
							global stdExam
							stdExam = float(input('Enter Exam Scores: '))
						except:
							print("Input should be number")
							ipTak()
				ipTak()
				nam.append(stdName)
				id.append(stdId)
				arCa1.append(stdCa1)
				arCa2.append(stdCa2)
				arCa3.append(stdCa3)
				arExm.append(stdExam)
				te1 = np.add(arCa1, arCa2)
				te2 = np.add(te1, arCa3)
				arCat.append(te2)
				tScores = np.add(te2, arExm)
				arTotal.append(tScores)
				stdTable = {"S/N":id, "Names":nam, "CA1":arCa1, "CA2":arCa2, "CA3":arCa3, "TCA":te2, "Exam":arExm, "Total Scores":tScores}
				table = pd.DataFrame(stdTable)
				tab = table.set_index(["S/N"])
				print(tab)
	
#stdData()
def js2A_sheet():
	print("Select Class you wish to Compute grade for")
	def selClass():
		classSel = input("1. JSS1A\n2. JSS1B\n3. JSS2A\n4. JSS2B\n5. JSS3A\n6. JSS3B")

		if classSel == "1":
			global names
			names = js1A
			global classNam
			classNam = "JSS 1A"
		elif classSel == "2":
			names = js1B
			classNam = "JSS 1B"
		elif classSel == "3":
			names = js2A
			classNam = "JSS 2A"
		elif classSel == "4":
			names = js2B
			classNam = "JSS 2B"
		elif classSel =="5":
		    names = js3A
		    classNam = "JSS 3A"
		elif  classSel =="6":
		    names =js3B
		    classNam = "JSS 3B"
		else:
			print("WRONG! input")
			selClass()
	selClass()
	
	sn = [x for x in range(1, len(names)+1)]
	stdlist = {"S/N":sn, "Names":names}
	tab2a = pd.DataFrame(stdlist)
	#tab2a = tab2a.set_index("S/N")
	j2Aar1 = []
	j2Aar2 = []
	j2Aar3 = []
	j2Aar4 = []
	j2Aar5 = []
	print("\nWelcome to "+classNam+" grading page\n")
	inp = input("Enter 'y' to preview "+classNam+" list; Enter 'n' or any other input to continue working with the list ")
	if inp == "y":
		print(tab2a)
		inp2 = input("\nWould you want to proceed working with the above list?\nEnter 'y' for yes and 'n' or any other inputs to compute your own names: ")
		if inp2 != "y":
			stdData()
			inp3 = input("Would you want to do anything else?\nEnter 'y' for yes and 'n' or any other inputs to exit: ")
			if inp3 =="y":
				options()
			else:
				exit()
			
	for index, row in tab2a.iterrows():
						def takScore():
							try:
								print("Enter Scores details for:", row["Names"], "with Reg no:", row["S/N"])
								global yt1
								yt1=float(input("Enter First Test Scores: "))
								if yt1 > 10:
								    print("\nTest Scores cannot exceed 10\n")
								    yt1 = float(input("Enter First Test scores"))
								global yt2
								yt2 =float(input("Enter Second Test Score: "))
								if yt2 > 10:
								    	print("\nTest scores cannot exceed 10\n")
								    	yt2 =float(input("Enter Second Test Scores"))
								global yt3
								yt3= float(input("Enter Third Test Scores: "))
								if yt3 > 10:
								    	print("\nTest scores cannot exceed 10\n")
								    	yt3 = float(input("\nEnter Third Test scores\n"))
								global yt4
								yt4=float(input("\nEnter Exam Scores: "))
								if yt4 > 70:
								    	print("Exam scores cannot exceed 70")
								    	yt4 = float(input("Enter Exam scores"))
							except:
								   	print("\nINCORRECT INPUT! Input MUST be NUMBER \n")
								   	takScore()
						takScore()
						j2Aar1.append(yt1)
						j2Aar2.append(yt2)
						j2Aar3.append(yt3)
						j2Aar4.append(yt4)
						#print(j2Aar1)
						#print(j2Aar2)
						cat1 = np.add(j2Aar1, j2Aar2)
						cat2 = np.add(cat1, j2Aar3)
						tot = np.add(cat2,  j2Aar4)
	dic = {"S/N":sn, "Names":names, "CA1":j2Aar1, "CA2":j2Aar2, "CA3":j2Aar3,"CAT":cat2, "Exam":j2Aar4, "Total":tot}
	tab = pd.DataFrame(dic)
	tab1 = tab.set_index("S/N")
	print(tab1)
	def saveTab():
		print("Enter 'y' to save computed Table to your local device 'n' to exit without saving")
		inp1 = input("Enter your preference: ")
		if inp1 == "y":
			tabName = input("Enter how you wont your Table to be named: ")
			tab1.to_csv(tabName + '.csv')
			print("Table saved successfully as " + tabName + ".csv")
		elif inp1 == "n":
			print("Your table won't be saved,  would you like to continue ? \nEnter 'y' to exit 'n' to countinue the saving processes")
			inp2 = input("Enter your preference: ")
			if inp2 == "n":
				saveTab()
			options()
	saveTab()
			
def snrScore():
    subSci = ["English","Mathematics","Civic","Chemistry","Physics","Biology","Agric","Economics","CRS","Computer"]
    subArt = ["English","Mathematics","Civic","Government","Agric","Commerce","Economics","Biology","CRS","Computer","Literature"]
    subGen =["English","Mathematics","Civic","Biology","Physics","Chemistry","Computer","Economics","Commerce","Agric","Literature","CRS","Government"]
    print("Select Class you wish to Compute grade for")
    cls = input("1. SS1A\n2. SS1B\n3. SS2A\n4. SS2B\n5. SS3A\n6. SS3B\n")
    def gen():
        sn = [x for x in range(1,len(name1)+1)]
        Ecat =[]
        Eexm=[]
        Etot =[]
        Mcat =[]
        Mexm =[]
        Mtot=[]
        Ccat =[]
        Cexm=[]
        Ctot =[]
        Bcat=[]
        Bexm=[]
        Btot=[]
        Pcat=[]
        Pexm=[]
        Ptot=[]
        CHcat=[]
        CHexm=[]
        CHtot=[]
        COcat =[]
        COexm =[]
        COtot=[]
        ECcat =[]
        ECexm=[]
        ECtot=[]
        COMcat=[]
        COMexm=[]
        COMtot=[]
        Acat=[]
        Aexm=[]
        Atot=[]
        Lcat=[]
        Lexm=[]
        Ltot=[]
        CRcat=[]
        CRexm=[]
        CRtot=[]
        Gcat=[]
        Gexm=[]
        Gtot=[]
        naTab ={"S/N":sn,"Names":name1}
        tab1 = pd.DataFrame(naTab)
        for index, row in tab1.iterrows():
            def inputTak():
                try:
                    print("Enter scores detail for "+row["Names"]+ " with Reg no. "+str(row["S/N"]))
                    global Eca
                    Eca = float(input("Enter Total English CA score: "))
                    global Eex
                    Eex = float(input("Enter English Exam scores: "))
                    global eT
                    eT = Eca+Eex
                    global Mca
                    Mca = float(input("Enter Total Maths CA scores: "))
                    global Mex
                    Mex =float(input("Enter Total Maths Exam scores: "))
                    global mT
                    mT = Mca +Mex
                    global Cca
                    Cca=float(input("Enter Total Civic Education scores: "))
                    global Cex
                    Cex =float(input("Enter Civic Education Exam scores: "))
                    global cT
                    cT = Cca+Cex
                    global Bca
                    Bca =float(input("Enter Total Biology CA scores: "))
                    global Bex
                    Bex=float(input("Enter Biology Exam scores: "))
                    global bT
                    bT = Bca + Bex
                    global CRca
                    CRca = float(input("Enter CRS Total CA scores: "))
                    global CRex
                    CRex = float(input("Enter CRS Exam scores: "))
                    global CRt
                    CRt = CRca+CRex
                    global ECca
                    ECca = float(input("Enter Total Economics CA Scores: "))
                    global ECex
                    ECex = float(input("Enter Economics Exam scores: "))
                    global ECt
                    ECt = ECca+ECex
                    if cls =="1":
                        global Pca
                        Pca =float(input("Enter Total physics CA scores: "))
                        global Pex
                        Pex = float(input("Enter Physics Exam scores: "))
                        global Pt
                        Pt = Pca+Pex
                        global CHca
                        CHca=float(input("Enter Total Chemistry CA scores: "))
                        global CHex
                        CHex = float(input("Enter Chemistry Exam scores: "))
                        global CHt
                        CHt = CHca+CHex
                        global Aca
                        Aca =float(input("Enter Total Agric CA scores: "))
                        global Aex
                        Aex = float(input("Enter Agric Exam scores: "))
                        global At
                        At = Aca+Aex
                        global COca
                        COca = float(input("Enter Total Computer CA scores: "))
                        COex = float(input("Enter Computer Exam scores: "))
                        global COt
                        COt = COca+COex
                    else:
                        print("Not science")
                    
                except:
                  print("Input not number!")
                  inputTak()
            inputTak()
            Ecat.append(Eca)
            Eexm.append(Eex)
            Etot.append(eT)
            Mcat.append(Mca)
            Mexm.append(Mex)
            Mtot.append(mT)
            Ccat.append(Cca)
            Cexm.append(Cex)
            Ctot.append(cT)
            Bcat.append(Bca)
            Bexm.append(Bex)
            Btot.append(bT)
            CRcat.append(CRca)
            CRexm.append(CRex)
            CRtot.append(CRt)
            ECcat.append(ECca)
            ECexm.append(ECex)
            ECtot.append(ECt)
            if cls=="1":
                Pcat.append(Pca)
                Pexm.append(Pex)
                Ptot.append(Pt)
                CHcat.append(CHca)
                CHexm.append(CHex)
                CHtot.append(CHt)
                Acat.append(Aca)
                Aexm.append(Aex)
                Atot.append(At)
            
            
            
            
        
        print(sub)
    def sel2():
    		if cls =="1":
    		    global sub
    		    sub = subGen
    		    global name1
    		    name1 = js2B
    		    gen()
    		elif cls =="2":
    		    sub = subGen
    		elif cls=="3":
    		    sub = subSci
    		elif cls =="4":
    		    sub = subGen
    		    name1=js2B
    		    gen()
    		elif cls =="5":
    		    sub = subSci
    		elif cls =="6":
    		    sub = subArt
    		else:
    		    print("\nWrong input!")
    		    sel2()
    
    sel2()
    names = js2B
    sn = [x for x in range(1, len(names)+1)]
#js2A_sheet()
#snrScore()
#options()
#stdData()
