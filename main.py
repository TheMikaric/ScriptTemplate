import scriptlibraries.myui as ui
import scriptlibraries.myio as io 
import scriptlibraries.mymainlogic as logic
import logging 

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('Main')
logger.level = logging.DEBUG

print('Hello, world from main!')
logger.debug('Hello, world from main!')
ui.test()
io.test()
print(io.load_config())
logic.test()