import os

s = os.popen("nmcli radio wifi").read()
print("Current wifi status: "+str(s))
print("Available network (May require root to run)")
print(os.system("nmcli dev wifi list"))
SSID = input("Enter the SSID of the network you want to connect (Don't forget the quotes):\n")
while True:
  if SSID != "":
      os.system("sudo nmcli --ask dev wifi connect "+SSID)
      break
  else:
      print("Try again.")
