import requests

base_url = 'https://api-fxpractice.oanda.com'
header_data = {'Content-Type': 'application/json', 'Authorization': 'Bearer 8f46dc882fe2a2500612be3e94abb7d6-fbe8d2e0d101bad62069e441852444c4'}

account_id = None

def get_price_and_spread(instrument_code):
    query_data = {'granularity': 'S5', 'count': '1', 'price': 'AB'}
    endpoint_url = '/v3/instruments/' + instrument_code + '/candles'

    data = call_request(endpoint_url, header_data, query_data)

    bid = data['candles'][0]['bid']['c']
    ask = data['candles'][0]['ask']['c']

    spread = round(float(ask) - float(bid), 5)

    return [bid, ask, spread]

def get_bid_price(instrument_code):
    query_data = {'granularity': 'S5', 'count': '1', 'price': 'B'}
    endpoint_url = '/v3/instruments/' + instrument_code + '/candles'

    data = call_request(endpoint_url, header_data, query_data)
    price = data['candles'][0]['bid']['c']

    return price

def get_ask_price(instrument_code):
    query_data = {'granularity': 'S5', 'count': '1', 'price': 'A'}
    endpoint_url = '/v3/instruments/' + instrument_code + '/candles'

    data = call_request(endpoint_url, header_data, query_data)
    price = data['candles'][0]['ask']['c']

    return price

def get_account_id():
    endpoint_url = '/v3/accounts'
    
    data = call_request(endpoint_url, header_data, {})
    id = data['accounts'][0]['id']

    return id

def get_account_value():
    global account_id

    if account_id is None:
        account_id = get_account_id()

    endpoint_url = '/v3/accounts/' + account_id + '/summary'
    
    data = call_request(endpoint_url, header_data, {})
    value = data['account']['balance']

    return round(float(value), 2)

def get_instrument_data():
    global account_id

    if account_id is None:
        account_id = get_account_id()

    endpoint_url = '/v3/accounts/' + account_id + '/instruments'

    data = call_request(endpoint_url, header_data, {})
    filtered_data = data['instruments']
    result_data = {}
    for instrument in filtered_data:
        result_data[instrument['name']] = {'margin_rate': instrument['marginRate'], 'type': instrument['type']}

    return result_data

def get_instrument_margin(instrument_code):
    return instrument_data[instrument_code]['margin_rate']

def get_instrument_type(instrument_code):
    return instrument_data[instrument_code]['type']

def get_all_pricing():
    keys = instrument_data.keys()
    
    result = {}

    for instrument_code in keys:
        result[instrument_code] = get_price_and_spread(instrument_code)

    return result

def call_request(endpoint_url, header_data, query_data):
    resp = requests.get(base_url + endpoint_url, headers = header_data, params=query_data)
    if resp.status_code != 200:
    #Change to raising an exception later
        print('Error')
    return resp.json()

instrument_data = get_instrument_data()
print(get_all_pricing())