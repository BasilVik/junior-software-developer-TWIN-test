from zeep import Client


def get_number_to_words_result(number):
    client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')
    result = client.service.NumberToWords(ubiNum=number)

    return result


print(get_number_to_words_result(9))
