import os
from pathlib import Path

RELEASE_VERSION = os.environ.get('RELEASE_VERSION')
BUILD_DIR = os.environ.get('BUILD_DIR')
IS_MAIN = os.environ.get('IS_MAIN') == 'true'
CURRENT_VERSION = os.environ.get('CURRENT_VERSION', '')

MSG = "Dev"
if IS_MAIN:
    MSG = "Main"

Path(BUILD_DIR).mkdir(parents=True, exist_ok=True)

with open(Path(BUILD_DIR, 'page.html'), 'w') as f:

    message = f"""<html>
    <head></head>
    <body><p>{MSG}!</p></body>
    </html>"""

    f.write(message)
