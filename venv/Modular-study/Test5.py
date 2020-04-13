#coding=utf-8
#logging模块实例，它提供5种常用级别
#从低到高分别是DEBUG、INFO、WARNING、ERROR、CRITICAL
#设置DEBUG级别时，debug（）函数和其他级别的函数日志信息会输出
#设置ERROR级别，error（）和critical（）函数的日志信息会输出

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

logger.debug('这是DEBUG级别信息')
logger.info('这是INFO级别信息')
logger.warning('这是WARNING级别信息')
logger.error('这是ERROR级别信息')
logger.critical('这是CRITICAL级别信息')

