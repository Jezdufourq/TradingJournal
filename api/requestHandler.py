import sys
import os
import api.make_requests as api
import json
from collections import namedtuple

data = api.get_instrument_data()

buyPrice = api.get_price_and_spread()

print()






