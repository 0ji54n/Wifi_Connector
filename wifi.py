import speedtest
import math

threads = None

s = speedtest.Speedtest()
upload = s.upload(threads = threads )
download = s.download(threads = threads)
try:
    print(str(math.floor(upload/(1024**2)))+" Mb/s"+", "+str(math.floor(download/(1024**2)))+" Mb/s" )
except:
  print("Disconnected")
