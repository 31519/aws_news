from datetime import datetime
from datetime import timedelta
adv_datetime_now = datetime.now()
def timeperiod():
    adv_datetime_now = datetime.now()
    now = adv_datetime_now
    data = now + timedelta(days=5)
    if (datetime.now() + timedelta(days=5)) >= data:
        print("True")
    else:
        print("False")
timeperiod()