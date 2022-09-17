from zeep import Client
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    """
    Модель запроса, описывает структуру тела запроса в JSON.
    В теле запроса передается один параметр - ubiNum.
    """

    ubiNum: int


class Response(BaseModel):
    """Модель ответа, описывает структуру тела ответа в JSON.
    В теле ответа передается один параметр - result.
    """

    result: str


@app.post('/number_to_words', response_model=Response)
def number_to_words(request: Request):
    return Response(result=get_number_to_words_result(request.ubiNum))


def get_number_to_words_result(number: int) -> str:
    # вдруг что-то не так с WSDL-схемой, повесим попытку
    try: 
        client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')
        result = client.service.NumberToWords(ubiNum=number)
    except Exception:
        return ''

    # метод NumberToWords возвращает число текстом с лишним пробелом, удалим его
    return result.strip()