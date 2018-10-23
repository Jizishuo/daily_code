'''import logging

logging.basicConfig(level=logging.INFO,
                    filename='./log.txt',
                    filemode='a',#w删除添加，a一直添加
                    format='%(asctime)s - %(filename)s[line:%(lineo)d] - %(levelname)s:%(message)s')

logging.debug("xxx")
logging.debug("xxx")'''


import logging

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)

handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")


