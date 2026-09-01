import os 
import requests
from dotenv import load_dotenv

load_dotenv()

NETAPP_HOST = os.getenv("NETAPP_HOST")
NETAPP_USER = os.getenv("NETAPP_USER")
NETAPP_PASSWORD = os.getenv("NETAPP_PASSWORD")

if not NETAPP_HOST:
    raise ValueError ("Netapp host is not configured")

if not NETAPP_USER:
    raise ValueError ("Netapp_username is not configured")
    
if not NETAPP_PASSWORD:
    raise ValueError ("Netapp_Password is not configured")

url = f"https://10.10.10.50/api/cluster"

try :
    response = requests.get(
    url,
    auth=(NETAPP_USER,NETAPP_PASSWORD),
    verify=False,
    timeout=10

     )
    print ("HTTP Status:" , response.status_code)

    if response.ok:
     data= response.json()

     print("Netapp cluster health check" )
     print("___________________________")
     print("Cluster:", data.get("name"))

    else:
     print("Netapp api request failed")
     print("Response :", response.text)

except requests.exceptions.RequestException as error :
   print("connection failed")
   print(error)

   
   
