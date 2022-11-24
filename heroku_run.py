import app

import logging
logging.basicConfig(level=logging.INFO)

alchemy_logger = logging.getLogger('sqlalchemy.engine')
alchemy_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run()
