import scriptlibraries.myui as ui
import scriptlibraries.myio as io 
import scriptlibraries.mymainlogic as mainlogic
import logging 

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG

print('Hello, world from main!')
logger.debug('Hello, world from main!')
ui.test()
io.test()
mainlogic.test()