import requests

base_url = 'https://api-fxpractice.oanda.com'
header_data = {'Content-Type': 'application/json', 'Authorization': 'Bearer 8f46dc882fe2a2500612be3e94abb7d6-fbe8d2e0d101bad62069e441852444c4'}

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

def call_request(endpoint_url, header_data, query_data):
    resp = requests.get(base_url + endpoint_url, headers = header_data, params=query_data)
    if resp.status_code != 200:
    #Change to raising an exception later
        print('Error')
    return resp.json()

print(get_bid_price('AUD_USD'))
print(get_ask_price('AUD_USD'))