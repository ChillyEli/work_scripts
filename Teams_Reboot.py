import os
import sys
import shutil
import subprocess

#Kill the Teams Process and stop all instances from running
os.system("TASKKILL /F /IM Teams.exe")

#Delete the cache folder
#Error out if it cant find or delete the folder for whatever reason
try:
  shutil.rmtree("%appdata%\Microsoft\Teams\Cache")
except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror)

#Delete the blob_storage folder
#Error out if it cant find or delete the folder for whatever reason
try:
  shutil.rmtree("%appdata%\Microsoft\Teams\blob_storage")
except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror)

#Delete the databases
#Error out if it cant find or delete the folder for whatever reason
try:
  shutil.rmtree("%appdata%\Microsoft\Teams\databases")
except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror)

#Delete GPU Cache
#Error out if it cant find or delete the folder for whatever reason
try:
  shutil.rmtree("%appdata%\Microsoft\Teams\GPUCache")
except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror)

#Delete all the indexed Databases
#Error out if it cant find or delete the folder for whatever reason
try:
  shutil.rmtree("%appdata%\Microsoft\Teams\IndexedDB")
except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror)

#Delete the local storage
#Error out if it cant find or delete the folder for whatever reason
try:
  shutil.rmtree("%appdata%\Microsoft\Teams\Local Storage")
except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror)

#Finally delete the temporary folder
#Error out if it cant find or delete the folder for whatever reason
try:
  shutil.rmtree("%appdata%\Microsoft\Teams\tmp")
except OSError as e:
  print("Error: %s - %s." % (e.filename, e.strerror)

#Now restart the app and launch again
subprocess.call(["C:\Users\darien.taylor\AppData\Local\Microsoft\Teams\Update.exe --processStart Teams.exe"])