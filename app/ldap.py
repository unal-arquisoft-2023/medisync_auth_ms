from ldap3 import Server, Connection, SAFE_SYNC, ALL, NTLM
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path('.env'))
LDAP_URI = os.getenv("LDAP_URI")

server = Server(LDAP_URI or '0.0.0.0',  get_info=ALL)


def request_role(role: str):
    try:
        conn = Connection(server, f"cn={role},cn=user,dc=arqsoft,dc=unal,dc=edu,dc=co", role, auto_bind=True)
        conn_string = conn.extend.standard.who_am_i().split(',')[0].split('=')[1]
        return conn_string
    except:
        return None