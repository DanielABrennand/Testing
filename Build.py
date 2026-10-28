import os

RELEASE_VERSION = os.environ.get('RELEASE_VERSION')
BUILD_DIR = os.environ.get('BUILD_DIR')
IS_MAIN = os.environ.get('IS_MAIN') == 'true'
CURRENT_VERSION = os.environ.get('CURRENT_VERSION', '')

MSG = "Dev"
if IS_MAIN:
    MSG = "Main"
    
if not os.path.exists(BUILD_DIR):
    os.mkdir(BUILD_DIR)
Path = os.path.join(BUILD_DIR, 'page.html')
with open(Path,'w') as f:

    message = f"""<html>
    <head></head>
    <body><p>{MSG}!</p></body>
    </html>"""

    f.write(message)
