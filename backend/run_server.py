import os
import subprocess
import sys

os.makedirs('data', exist_ok=True)
os.makedirs('data/jobs', exist_ok=True)

try:
    subprocess.run([sys.executable, '-m', 'alembic', 'upgrade', 'head'], check=False)
except Exception as e:
    print('Migration notice:', e)

import uvicorn
port = int(os.environ.get('PORT', 8000))
uvicorn.run('ledgertrace.api.main:app', host='0.0.0.0', port=port)
