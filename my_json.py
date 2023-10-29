import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

json_str = '{"items" : [{"id" :1, "name": "pen"}, {"id": 2, "name": "apple"}], "status": "sell"}'
dict_data = json.loads(json_str)

# ログメッセージを表示
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print(type(dict_data))

# json_str = json.dumps(dict_data)
# print(dict_data)

