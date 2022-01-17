from django import template
from datetime import datetime, timedelta
import pytz
import time

from datetime import datetime
from django.utils import timezone


register = template.Library()



@register.filter(name='convert_only_dateYear')
def convert_date(given_time):
    d = str(given_time)
    final_result = datetime.fromtimestamp(int(d)).strftime('%b %d, %Y')
    return final_result


@register.filter(name='convert_only_time')
def convert_time(given_time):
    # d = str(given_time)
    # timestamp = datetime.fromtimestamp(int(d))
    # final_result = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    # return final_result
    
    # unix_timestamp = int("1640911219")
    # utc_time = time.gmtime(unix_timestamp)
    # local_time = time.localtime(unix_timestamp)
    # final_result = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    # print(final_result)
    # return final_result
    
    unix_timestamp = int("1640911219")
    local_time = time.localtime(unix_timestamp)
    print(time.strftime("%Y-%m-%d %H:%M:%S %p", local_time))
    result = time.strftime("%Y-%m-%d %H:%M:%S %p", local_time)
    return result

@register.filter(name='unix_to_datetime')
def unix_to_datetime(value):
    a = datetime(value)
    result = a.strftime("%H:%M:%S %Z")
    return result
    



@register.filter
def to_and(value):
    return value.replace("en/", "")