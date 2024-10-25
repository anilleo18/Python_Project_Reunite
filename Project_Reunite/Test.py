import logging
from concept_customLogger import getcustomLogger


class Test:

    def logtest(self):
        logger = getcustomLogger(logging.DEBUG)
        logger.debug('Debug Messages')
        logger.info('Info Messages')
        logger.warning('warning Message')
        logger.error('error Message')
        logger.critical('critical Message')


    def logtest_1(self):
        logger=getcustomLogger(logging.WARNING)
        logger.info('Information Message -1')
        logger.debug('Debug Message -1')
        logger.warning('Warning Message -1')
        logger.error('Error Message -1 ')
        logger.critical('critical Message -1')
t=Test()
#t.logtest()
t.logtest_1()