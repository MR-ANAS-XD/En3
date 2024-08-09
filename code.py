import os, sys
os.system("git pull")
try:
    __import__("Marshal_enc").an6()
except Exception as e:
    exit(str(e))