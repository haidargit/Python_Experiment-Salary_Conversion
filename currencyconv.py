import requests
import json
import unittest
from requests.exceptions import ConnectionError
from fnmatch import fnmatch

# Notes 
# i am currently using API service from https://www.currencyconverterapi.com/ 

def currency_converter(origin_currency,target_currency):
    # ~ ~ the function will return currency conversion per '1' value of IDR. 
    # ~ ~ the API call will be done just ONCE to get the reference value for conversion.
    api_key = "6b240d754ef7c9a85233"
    convert_value = float(format(float(requests.get("https://free.currconv.com/api/v7/convert?q="+origin_currency+"_"+target_currency+"&compact=ultra&apiKey="+api_key).json()[origin_currency+"_"+target_currency]),'f'))
    return convert_value

def get_api_and_combine_dollar(obj):
    open_external_json = open('salary_data.json','r')
    data = json.load(open_external_json)
    array_convert_idr_to_usd = []
    conversion_value = 0.0
    conversion_value = currency_converter("IDR","USD")
    
    # converting IDR to USD
    for i in range(len(data['array'])):
        array_convert_idr_to_usd.append(float(format(float(data['array'][i]['salaryInIDR']),'f'))*conversion_value) 
    
    for i in range(len(obj)):
        # Output from the endpoint should be: id, name, username, email, address, phone, salary in IDR, and salary in USD
        obj[i]["salary_in_IDR"] = data['array'][i]['salaryInIDR']
        obj[i]["salary_in_USD"] = array_convert_idr_to_usd[i]
        del obj[i]['website']
        del obj[i]['company']
        
    open_external_json.close
    return obj


# ________________________________________* UNIT TESTING AREA *________________________________________

class CurrencyConverterUnitTest(unittest.TestCase):
    # 1. the Biodata url is VALID and the user get the json response. (SUCCESS case)
    def test_biodata_url_valid(self):
        test_response = requests.get("http://jsonplaceholder.typicode.com/users").status_code
        test_response_json = requests.get("http://jsonplaceholder.typicode.com/users")
        self.assertEqual(test_response, 200)
        self.assertTrue(isinstance(test_response_json.json(), list))
    
    # 2. the url is VALID and the user don't get the Biodata's json response. Because the path '/users' is undefined. (PARTIAL case)
    def test_biodata_url_partial_invalid(self):
        test_response = requests.get("http://jsonplaceholder.typicode.com/").status_code
        self.assertEqual(test_response, 200)
        with self.assertRaises(ValueError):
            requests.get("http://jsonplaceholder.typicode.com/").json()

    # 3. the url is VALID and the path is INVALID. The user dont get the json response. (PARTIAL case)
    def test_biodata_urlpath_invalid(self):
        test_response = requests.get("http://jsonplaceholder.typicode.com/usersfailedtestfailedtestfailedtestfailedtestfailedtest").status_code
        self.assertEqual(test_response, 404)
    
    # 4. the whole Biodata url is pure INVALID. (FAILED Case)
    def test_biodata_url_invalid(self):
        with self.assertRaises(ConnectionError):
            requests.get("http://jsonfailed.failedtestfailedtestfailedtestfailedtest.com/usersfailedtestfailedtest").status_code

    # 5. the API service for currency coverter is SUCCESSFUL. Both parameters and API Key are correct/verified.
    def test_api_call(self):
        test_response_json = requests.get("https://free.currconv.com/api/v7/convert?q=IDR_USD&compact=ultra&apiKey=6b240d754ef7c9a85233").json()
        self.assertTrue(isinstance(test_response_json, dict))

    # 6. the API address for currency coverter is INVALID. Because the API key is incorrect. (Bad Request = 400)
    def test_api_call_invalid_apikey(self):
        test_response_json = requests.get("https://free.currconv.com/api/v7/convert?q=IDR_USD&compact=ultra&apiKey=6b240d754ef7c9a85233x76").json()
        self.assertEqual(test_response_json['status'],400)

    # 7. the API address for currency coverter is INVALID. Because the Currency Pairs are incorrect. (Bad Request = 400)
    def test_api_call_invalid_currency_pairs(self):
        test_response_json = requests.get("https://free.currconv.com/api/v7/convert?q=AAAAAA_BBBBBB&compact=ultra&apiKey=6b240d754ef7c9a85233").json()
        test_response_json_2 = requests.get("https://free.currconv.com/api/v7/convert?q=ABC_DEF&compact=ultra&apiKey=6b240d754ef7c9a85233").json()
        self.assertFalse(bool(test_response_json))
        self.assertFalse(bool(test_response_json_2))

    # 8. Get Endpoint result as a whole (SUCCESS case). 
    #    Test case must also check the string occurence of IDR and USD as a new field. 
    #    Also check the KEY of 'website' and 'company' must be non exist on the final endpoint.
    def api_conversion_result(self):
        self.assertEqual(len(get_api_and_combine_dollar(take_response.json())), 10)
        self.assertTrue('website' not in get_api_and_combine_dollar(take_response.json())[0])
        self.assertTrue('company' not in get_api_and_combine_dollar(take_response.json())[0])
        self.assertTrue(fnmatch(' '.join(list(get_api_and_combine_dollar(take_response.json())[0].keys())),'*IDR*'))
        self.assertTrue(fnmatch(' '.join(list(get_api_and_combine_dollar(take_response.json())[0].keys())),'*USD*'))


# _________________________________________* MAIN/DRIVER CODE *________________________________________
if __name__ == '__main__':
    # Begin Unit Test
    unittest.main(exit=False)

    # Then Show Final Endpoint Result after unit test is done
    print("# # # # # #FINAL RESULT# # # # # #")
    take_response = requests.get("http://jsonplaceholder.typicode.com/users")
    print(json.dumps(get_api_and_combine_dollar(take_response.json()), sort_keys=False, indent= 4))
