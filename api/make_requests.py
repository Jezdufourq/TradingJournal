import requests

class api:
    base_url = 'https://api-fxpractice.oanda.com'
    header_data = {'Content-Type': 'application/json', 'Authorization': ''}
    account_id = None
    instrument_data = None

    def __init__(self, url, token):
        self.base_url = url
        self.header_data['Authorization'] = 'Bearer ' + token
        self.get_account_id()
        self.get_instrument_data()

    def get_instrument_data(self):
        """
        Returns dictionary containing all instruments, margin and type.
        :return:
        """
        if self.account_id is None:
            self.get_account_id()

        endpoint_url = '/v3/accounts/' + self.account_id + '/instruments'

        data = self.call_request(endpoint_url, self.header_data, {})
        filtered_data = data['instruments']
        result_data = {}
        for instrument in filtered_data:
            result_data[instrument['name']] = {'margin_rate': instrument['marginRate'], 'type': instrument['type']}

        self.instrument_data =  result_data


    def get_account_id(self):
        endpoint_url = '/v3/accounts'
        data = self.call_request(endpoint_url, self.header_data, {})
        self.account_id = data['accounts'][0]['id']
        return self.account_id


    def get_price_and_spread(self, instrument_code):
        query_data = {'granularity': 'S5', 'count': '1', 'price': 'AB'}
        endpoint_url = '/v3/instruments/' + instrument_code + '/candles'
        data = self.call_request(endpoint_url, self.header_data, query_data)

        bid = data['candles'][0]['bid']['c']
        ask = data['candles'][0]['ask']['c']

        spread = round(float(ask) - float(bid), 5)
        return [bid, ask, spread]

    def get_bid_price(self, instrument_code):
        query_data = {'granularity': 'S5', 'count': '1', 'price': 'B'}
        endpoint_url = '/v3/instruments/' + instrument_code + '/candles'

        data = self.call_request(endpoint_url, self.header_data, query_data)
        price = data['candles'][0]['bid']['c']

        return price

    def get_ask_price(self, instrument_code):
        query_data = {'granularity': 'S5', 'count': '1', 'price': 'A'}
        endpoint_url = '/v3/instruments/' + instrument_code + '/candles'

        data = self.call_request(endpoint_url, self.header_data, query_data)
        price = data['candles'][0]['ask']['c']

        return price


    def get_account_value(self):
        global account_id

        if account_id is None:
            account_id = self.get_account_id()

        endpoint_url = '/v3/accounts/' + account_id + '/summary'

        data = self.call_request(endpoint_url, self.header_data, {})
        value = data['account']['balance']

        return round(float(value), 2)

    def get_all_pricing(self):
        endpoint_url = '/v3/accounts/' + self.account_id + '/pricing'

        if self.instrument_data is None:
            self.get_instrument_data()

        query_data = {'instruments': ','.join(self.instrument_data.keys())}
        data = self.call_request(endpoint_url, self.header_data, query_data)
        data = data['prices']

        result = {}

        for instrument in data:
            bid_price = instrument['closeoutBid']
            ask_price = instrument['closeoutAsk']
            spread = round(float(ask_price) - float(bid_price), 5)
            result[instrument['instrument']] = {'bid_price': bid_price, 'ask_price': ask_price, 'spread': spread}

        return result

    def call_request(self, endpoint_url, header_data, query_data):
        resp = requests.get(self.base_url + endpoint_url, headers = header_data, params=query_data)
        if resp.status_code != 200:
        #Change to raising an exception later
            print('Error')
        return resp.json()

    #instrument_data = get_instrument_data()
    #get_all_pricing()