import urllib2
import requests
import os
import sys
import time

GIALLO = "\033[1;33;1m"
GNORM = "\033[0;33;1m"
VERDE = "\033[1;32;1m"
RI = "\033[0;32;1m"
BIANCO = "\033[1;37;1m"
DOM = "\033[0;37;1m"
ROSSO = "\033[1;31;1m"
DEF = "\033[0m"
searchfd = 0

def banner():
	print """
%s                                        
 ,---.   |              |    o          
 |  _.   |---.,---.,---.|__/ .,---.,---.
 |   |---|   |,---||    |  \ ||   ||   |
 `---'   `   '`---^`---'`   ```   '`---|
                %sv. 1.0%s             `---'
               %sby Zanker
%s 
""" % (GNORM, VERDE, GNORM, VERDE, DEF)
def searchdork():
	downlink = 	"https://pastebin.com/raw/QWCmACjk"
	pag = requests.get(downlink)
	pagread = pag.text
	paglines = pagread.split("\n")
	urld = []
	nomelista = []
	print " "
	print "%s[*] %s google dorks lists were found:%s" % (BIANCO, len(paglines), DEF)
	cldorks = 1
	for i in paglines:
		line = i.split("-")
		urld.append(line[1])
		nomelista.append(line[0])
		print "(%s%s%s) %s%s%s" % (GIALLO, str(cldorks), DEF, BIANCO, line[0], DEF)
		cldorks = cldorks + 1
	print " "
	print "%s[?] Which list do you want to download? [Leave blank if you want to download them all]%s" % (DOM, DEF)
	sclistas = raw_input("> ")
	if sclistas == "":
		lak = 0
		while lak < len(urld):
			try:
				dfiledown = urllib2.urlopen(urld[lak])
				filedorks = open("gdorks/"+nomelista[lak], "w")
				filedorks.write(dfiledown.read())
				filedorks.close()
			except:
				print "%s[!] Error downloading %s%s" % (ROSSO, nomelista[lak], DEF)
			else:
				print "%s[+] File '%s' successfully downloaded to 'gdorks/%s'%s" % (VERDE, nomelista[lak], nomelista[lak], DEF)
			lak = lak + 1
	elif not int(sclistas) in range(1, len(paglines)+1):
		print "%s[!] Enter a valid answer%s" % (ROSSO, DEF)
		sys.exit()
	else:
		try:
			dfiledown = urllib2.urlopen(urld[int(sclistas)-1])
			filedorks = open("gdorks/"+nomelista[int(sclistas)-1], "w")
			filedorks.write(dfiledown.read())
			filedorks.close()
		except:
			print "%s[!] Error downloading %s%s" % (ROSSO, nomelista[int(sclistas)-1], DEF)
		else:
			print "%s[+] File '%s' successfully downloaded to 'gdorks/%s'%s" % (VERDE, nomelista[int(sclistas)-1], nomelista[int(sclistas)-1], DEF)
def crawricerca():
	banner()
	def output():
		if len(urls) > 0:
			urldef = []
			ft = open(outfile, "w")

			for h in urls:
				k = h.split("&amp;")
				kparsed = urllib2.unquote(k[0]).decode('utf8')
				if not "https://accounts.google.com/" in kparsed and not "/search?q=" in kparsed:
					urldef.append(kparsed)
					ft.write(kparsed+"\n")
						
			ft.close()
			print " "
			print "%s[+] %s URLs were found, would you like to see the output? [y/N]%s" % (VERDE, str(len(urldef)), DEF)
			visout = raw_input("> ")
			if visout == "y" or visout == "yes":
				for shurl in urldef:
					print shurl
			elif visout == "n" or visout == "no" or visout == "N" or visout == "":
				pass
			else:
				print "%s[!] Enter a valid answer%s" % (ROSSO, DEF)
				sys.exit()
			print " "
			print "%s[*] URL correctly transcribed on %s%s" % (BIANCO, outfile, DEF)
			print " "
			sys.exit()
		else:
			print " "
			print "%s[*] No URLs found%s" % (BIANCO, DEF)
			print " "
			sys.exit()
	print " "
	print "%s[*] Search%s" % (DOM, DEF)
	pricerca = raw_input("> ")
	print "%s[+] Search ==> %s%s" % (VERDE, pricerca, DEF)
	print " "
	print "%s[?] Limit pages to search? [y/N]%s" % (DOM, DEF)
	limit = raw_input("> ")
	if limit == "y" or limit == "yes":
		print " "
		print "%s[*] Limit pages per search%s" % (DOM, DEF)
		plimit = raw_input("> ")
		if plimit <= str(0):
	 		print "%s[!] Enter a valid number of pages%s" % (ROSSO, DEF)
			sys.exit()
		else:
			print "%s[+] Limit ==> %s%s" % (VERDE, plimit, DEF)

	elif limit == "n" or limit == "no" or limit == "N" or limit == "":
		plimit = "no"
	else:
		print "%s[!] Enter a valid answer%s" % (ROSSO, DEF)
		sys.exit()
		
	urls = []
	print " "
	print "%s[*] Output file (default 'output.txt')%s" % (BIANCO, DEF)
	outfinput = raw_input("> ")
	if outfinput == "":
		outfile = "output.txt"
	else:
		outfile = outfinput
	print "%s[+] Output ==> %s%s" % (VERDE, outfile, DEF)
	print " "
	print "%s[?] Use proxy? [y/N]%s" % (DOM, DEF)
	proxysc = raw_input("> ")
	if proxysc == "y" or proxysc == "yes":
		print " "
		print "%s[*] Proxy list%s" % (BIANCO, DEF)
		proxylist = raw_input("> ")
		useproxy = 1
		proxyy = []
		try:
			listp = open(proxylist, "r")
		except:
			print "%s[!] Error opening '%s'%s" % (ROSSO, proxylist, DEF)
		else:
			print "%s[+] Proxy ==> %s%s" % (VERDE, proxylist, DEF)
			buffproxy = listp.readlines()
			for prox in buffproxy:
				proxpure = prox.replace("\n", "")
				proxyy.append(proxpure)
	elif proxysc == "n" or proxysc == "N" or proxysc == "no" or proxysc == "":
		useproxy = 0
	else:
		print "%s[!] Enter a valid answer%s" % (ROSSO, DEF)
		sys.exit()
	print " "
	parola = urllib2.quote(pricerca)
		
	ccont = 0
	limite = 0
	contpag = 1
	contproxy = 0
	print " "
	if plimit != "no":
		try:
			while ccont <= (int(plimit)-1)*10:
				if useproxy == 0:
					prepagina = requests.get("https://www.google.it/search?q="+parola+"&client=ubuntu&hl=en&hs=HRr&channel=fs&ei=nu4VXfutEvGgrgSy46XoDQ&start="+str(ccont))
				elif useproxy == 1:
					try:
						proxydict = {
							"http": "http://"+proxyy[contproxy],
							"https": "http://"+proxyy[contproxy]
						}
					except:
						pass
					try:
						print "%sProxy: %s%s" % (GIALLO, proxyy[contproxy], DEF)
					except:
						pass
					print " "
					try:
						prepagina = requests.get("https://www.google.it/search?q="+parola+"&client=ubuntu&hl=en&hs=HRr&channel=fs&ei=nu4VXfutEvGgrgSy46XoDQ&start="+str(ccont), proxies=proxydict)
					except:
						print "%s[!] Error opening URL%s" % (ROSSO, DEF)
				try:
					pagina = prepagina.text
					if "did not match any documents" in pagina:
						print "%s[*] There are no more search results%s" % (BIANCO, DEF)
						print " "
						limite = 1
					elif "Our systems have detected unusual traffic from your computer network" in pagina:
						sys.stdout.write("\033[F")
						sys.stdout.write("\033[K")
						print "%s[!] CAPTCHA detected%s" % (ROSSO, DEF)
						print " "
						limite = 1
					else:
						sys.stdout.write("\033[F")
						sys.stdout.write("\033[K")
						print "%s[+] %s page completed%s" % (VERDE, str(contpag), DEF)
						pagina = pagina.split("<a href=")

						for i in pagina:
							a = i.split('"')
							b = a[1].split("/url?q=")
							try:
								urls.append(b[1])
							except:
								pass
					ccont = ccont + 10
					contpag = contpag + 1
					if useproxy == 1:
						contproxy = contproxy + 1
				except:
					pass
		except KeyboardInterrupt:
			output()
	else:
		try:
			while limite == 0:
				if useproxy == 0:
					prepagina = requests.get("https://www.google.it/search?q="+parola+"&client=ubuntu&hl=en&hs=HRr&channel=fs&ei=nu4VXfutEvGgrgSy46XoDQ&start="+str(ccont))
				elif useproxy == 1:
					try:
						proxydict = {
							"http": "http://"+proxyy[contproxy],
							"https": "http://"+proxyy[contproxy]
						}
					except:
						pass
					try:
						print "%sProxy: %s%s" % (GIALLO, proxyy[contproxy], DEF)
					except:
						pass
					print " "
					try:
						prepagina = requests.get("https://www.google.it/search?q="+parola+"&client=ubuntu&hl=en&hs=HRr&channel=fs&ei=nu4VXfutEvGgrgSy46XoDQ&start="+str(ccont), proxies=proxydict)
					except:
						print "%s[!] Error opening URL%s" % (ROSSO, DEF)
				try:
					pagina = prepagina.text
					if "did not match any documents" in pagina:
						print "%s[*] There are no more search results%s" % (BIANCO, DEF)
						print " "
						limite = 1
					elif "Our systems have detected unusual traffic from your computer network" in pagina:
						sys.stdout.write("\033[F")
						sys.stdout.write("\033[K")
						print "%s[!] CAPTCHA detected%s" % (ROSSO, DEF)
						print " "
						limite = 1
					else:
						sys.stdout.write("\033[F")
						sys.stdout.write("\033[K")
						print "%s[+] %s page completed%s" % (VERDE, str(contpag), DEF)
						pagina = pagina.split("<a href=")
						for i in pagina:
							a = i.split('"')
							b = a[1].split("/url?q=")
							try:
								urls.append(b[1])
							except:
								pass
					ccont = ccont + 10
					contpag = contpag + 1
					if useproxy == 1:
						contproxy = contproxy + 1
				except:
					pass
		except KeyboardInterrupt:
			output()

	output()

def listdorks():
	banner()
	def output():
		if len(urls) > 0:
			urldef = []
			ft = open(outfile, "w")

			for h in urls:
				k = h.split("&amp;")
				kparsed = urllib2.unquote(k[0]).decode('utf8')
				if not "https://accounts.google.com/" in kparsed and not "/search?q=" in kparsed:
					urldef.append(kparsed)
					ft.write(kparsed+"\n")
						
			ft.close()
			print " "
			print "%s[+] %s URLs were found, would you like to see the output? [y/N]%s" % (VERDE, str(len(urldef)), DEF)
			visout = raw_input("> ")
			if visout == "y" or visout == "yes":
				for shurl in urldef:
					print shurl
			elif visout == "n" or visout == "no" or visout == "N" or visout == "":
				pass
			else:
				print "%s[!] Enter a valid answer%s" % (ROSSO, DEF)
				sys.exit()
			print " "
			print "%s[*] URL correctly transcribed on %s%s" % (BIANCO, outfile, DEF)
			print " "
			sys.exit()
		else:
			print " "
			print "%s[*] No URLs found%s" % (BIANCO, DEF)
			print " "
			sys.exit()

	print " "
	print "%s[?] Limit pages to search? [y/N]%s" % (DOM, DEF)
	limit = raw_input("> ")
	if limit == "y" or limit == "yes":
		print " "
		print "%s[*] Limit pages per search%s" % (DOM, DEF)
		plimit = raw_input("> ")
		if plimit <= str(0):
	 		print "%s[!] Enter a valid number of pages%s" % (ROSSO, DEF)
			sys.exit()
		else:
			print "%s[+] Limit ==> %s%s" % (VERDE, plimit, DEF)

	elif limit == "n" or limit == "no" or limit == "N" or limit == "":
		plimit = "no"
	else:
		print "%s[!] Enter a valid answer%s" % (ROSSO, DEF)
		sys.exit()
	global searchfd
	if searchfd == 0:
		print " "
		print "%s[?] Do you want to search for G-Dorks from internet? [y/N]%s" % (DOM, DEF)
		sdorks = raw_input("> ")
		if sdorks == "y" or sdorks == "yes":
			if (os.path.exists("gdorks")==False):
				try:
					os.system("mkdir gdorks")
				except:
					print "%s[!] Error creating directory 'gdorks'%s" % (ROSSO, DEF)
					sys.exit()
			searchdork()
		elif sdorks == "n" or sdorks == "N" or sdorks == "no" or sdorks == "":
			pass
		else:
			print "%s[!] Enter a valid answer%s" % (ROSSO, DEF)
			sys.exit()
		
	urls = []
	print " "
	print "%s[*] Dorks list%s" % (BIANCO, DEF)
	fidorks = raw_input("> ")
	try:
		f = open(fidorks, "r")
	except:
		print "%s[!] Error opening file %s%s" % (ROSSO, fidorks, DEF)
		sys.exit()
	print "%s[+] Dorks ==> %s%s" % (VERDE, fidorks, DEF)
	print " "
	print "%s[*] Output file (default 'output.txt')%s" % (BIANCO, DEF)
	outfinput = raw_input("> ")
	if outfinput == "":
		outfile = "output.txt"
	else:
		outfile = outfinput
	print "%s[+] Output ==> %s%s" % (VERDE, outfile, DEF)
	print " "
	print "%s[?] Use proxy? [y/N]%s" % (DOM, DEF)
	proxysc = raw_input("> ")
	if proxysc == "y" or proxysc == "yes":
		print " "
		print "%s[*] Proxy list%s" % (BIANCO, DEF)
		proxylist = raw_input("> ")
		useproxy = 1
		proxyy = []
		try:
			listp = open(proxylist, "r")
		except:
			print "%s[!] Error opening '%s'%s" % (ROSSO, proxylist, DEF)
		else:
			print "%s[+] Proxy ==> %s%s" % (VERDE, proxylist, DEF)
			buffproxy = listp.readlines()
			for prox in buffproxy:
				proxpure = prox.replace("\n", "")
				proxyy.append(proxpure)
	elif proxysc == "n" or proxysc == "N" or proxysc == "no" or proxysc == "":
		useproxy = 0
	else:
		print "%s[!] Enter a valid answer%s" % (ROSSO, DEF)
		sys.exit()
	for parola in f.readlines():
		print " "
		parola = parola.replace("\n", "")
		print "%sDork: %s%s" % (GIALLO, parola, DEF)
		print " "
		parola = urllib2.quote(parola)
				
		ccont = 0
		limite = 0
		contpag = 1
		contproxy = 0
		if plimit != "no":
			try:
				while ccont <= (int(plimit)-1)*10:
					if useproxy == 0:
						prepagina = requests.get("https://www.google.it/search?q="+parola+"&client=ubuntu&hl=en&hs=HRr&channel=fs&ei=nu4VXfutEvGgrgSy46XoDQ&start="+str(ccont))
					elif useproxy == 1:
						try:
							proxydict = {
								"http": "http://"+proxyy[contproxy],
								"https": "http://"+proxyy[contproxy]
							}
						except:
							pass
						try:
							print "%sProxy: %s%s" % (GIALLO, proxyy[contproxy], DEF)
						except:
							pass
						print " "
						try:
							prepagina = requests.get("https://www.google.it/search?q="+parola+"&client=ubuntu&hl=en&hs=HRr&channel=fs&ei=nu4VXfutEvGgrgSy46XoDQ&start="+str(ccont), proxies=proxydict)
						except:
							print "%s[!] Error opening URL%s" % (ROSSO, DEF)
					try:
						pagina = prepagina.text
						if "did not match any documents" in pagina:
							print "%s[*] There are no more search results%s" % (BIANCO, DEF)
							print " "
							limite = 1
						elif "Our systems have detected unusual traffic from your computer network" in pagina:
							sys.stdout.write("\033[F")
							sys.stdout.write("\033[K")
							print "%s[!] CAPTCHA detected%s" % (ROSSO, DEF)
							print " "
							limite = 1
						else:
							sys.stdout.write("\033[F")
							sys.stdout.write("\033[K")
							print "%s[+] %s page completed%s" % (VERDE, str(contpag), DEF)
							pagina = pagina.split("<a href=")

							for i in pagina:
								a = i.split('"')
								b = a[1].split("/url?q=")
								try:
									urls.append(b[1])
								except:
									pass
						ccont = ccont + 10
						contpag = contpag + 1
						if useproxy == 1:
							contproxy = contproxy + 1
					except:
						pass
			except KeyboardInterrupt:
				output()
		else:
			try:
				while limite == 0:
					if useproxy == 0:
						prepagina = requests.get("https://www.google.it/search?q="+parola+"&client=ubuntu&hl=en&hs=HRr&channel=fs&ei=nu4VXfutEvGgrgSy46XoDQ&start="+str(ccont))
					elif useproxy == 1:
						try:
							proxydict = {
								"http": "http://"+proxyy[contproxy],
								"https": "http://"+proxyy[contproxy]
							}
						except:
							pass
						try:
							print "%sProxy: %s%s" % (GIALLO, proxyy[contproxy], DEF)
						except:
							pass
						print " "
						try:
							prepagina = requests.get("https://www.google.it/search?q="+parola+"&client=ubuntu&hl=en&hs=HRr&channel=fs&ei=nu4VXfutEvGgrgSy46XoDQ&start="+str(ccont), proxies=proxydict)
						except:
							print "%s[!] Error opening URL%s" % (ROSSO, DEF)
					try:
						pagina = prepagina.text
						if "did not match any documents" in pagina:
							print "%s[*] There are no more search results%s" % (BIANCO, DEF)
							print " "
							limite = 1
						elif "Our systems have detected unusual traffic from your computer network" in pagina:
							sys.stdout.write("\033[F")
							sys.stdout.write("\033[K")
							print "%s[!] CAPTCHA detected%s" % (ROSSO, DEF)
							print " "
							limite = 1
						else:
							sys.stdout.write("\033[F")
							sys.stdout.write("\033[K")
							print "%s[+] %s page completed%s" % (VERDE, str(contpag), DEF)
							pagina = pagina.split("<a href=")

							for i in pagina:
								a = i.split('"')
								b = a[1].split("/url?q=")
								try:
									urls.append(b[1])
								except:
									pass
						ccont = ccont + 10
						contpag = contpag + 1
						if useproxy == 1:
							contproxy = contproxy + 1
					except:
						pass
			except KeyboardInterrupt:
				output()

	output()

def mainmenu():
	os.system("clear")
	banner()
	print """
[%s1%s] %sDorks link crawler%s
[%s2%s] %sLink crawler of a search%s
[%s3%s] %sSearch for dorks on internet%s

[%s99%s] %sExit%s
	""" % (GIALLO, DEF, BIANCO, DEF, GIALLO, DEF, BIANCO, DEF, GIALLO, DEF, BIANCO, DEF, GIALLO, DEF, BIANCO, DEF)
	deci = raw_input("> ")

	if deci == str(1):
		os.system("clear")
		listdorks()
	elif deci == str(2):
		os.system("clear")
		crawricerca()
	elif deci == str(3):
		os.system("clear")
		if (os.path.exists("gdorks")==False):
			try:
				os.system("mkdir gdorks")
			except:
				print "%s[!] Error creating directory 'gdorks'%s" % (ROSSO, DEF)
				sys.exit()
		global searchfd
		searchfd = 1
		searchdork()
		print " "
		print "%s[*] Return to the main menu....%s" % (BIANCO, DEF)
		time.sleep(1.5)
		mainmenu()
	elif deci == str(99):
		sys.exit()
	else:
		print "%s[!] Enter a valid option%s" % (ROSSO, DEF)
		sys.exit()

mainmenu()
