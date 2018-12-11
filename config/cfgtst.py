import sys, os
sys.path.append(os.path.curdir)
from config import config_handler as cfg

print cfg.get('MinWaterLevel', 'DEFAULT')