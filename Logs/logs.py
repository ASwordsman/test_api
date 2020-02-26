import logging
import datetime

now_time = datetime.datetime.now()

time_str = datetime.datetime.now().strftime('%Y-%m-%d')

fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'

logging.basicConfig(level=logging.ERROR,

                    format=fmt,

                    filename=r'C:\Users\lingshi\Desktop\testapi\test_api\Logs\{}'.format(time_str),

                    filemode='a',

                    datefmt='%a, %d %b %Y %H:%M:%S'

                    )
