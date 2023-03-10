import logging
logging.basicConfig(filename='testlog.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s %(levelname)s')
logging.debug('这是debug信息')
logging.info('这是info信息')
logging.warning('这是warning信息')
logging.error('这是error信息')
