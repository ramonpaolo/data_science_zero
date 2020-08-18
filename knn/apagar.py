import wget, requests
ulr = "http://sionpyksir7vwqdr3hdw72qclureghhwj4o37mcatiym6lyndprwckid.onion:8080/video/sxKOtcavbvXtAPHQ43CLqQ/1595738293/3408549/0k5/0k5rb0b5b2xf8z3maq5zb.webm"
url = "http://bhtcqlsl7gjhlcty.onion/index.php?option=com_hwdvideoshare&task=viewvideo&Itemid=2&video_id=18690"
req = requests.get(url)
down = wget.download(url)