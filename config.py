import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26305247")

API_HASH = os.environ.get("API_HASH", "20ca7e6687c281e11782856c7efd0ff7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6132391938:AAEPDCNePTVGl-3UGz3lb4vsVZ6fRDiH9Bs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Film_Update_Official") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ae8701b26c6cf0db98c0b.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5791145987').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
