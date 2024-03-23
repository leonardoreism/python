from .swap_api_consumer import SwapiApiConsumer

def test_get_starships():
    ''' Testing get_startships method '''
    
    # requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={ 'some':  'thing'})
    
    swapi_api_consumer = SwapiApiConsumer()
    page = 1
    get_star_ship_response = swapi_api_consumer.get_starships(page=page)
    
    assert get_star_ship_response.request.method == 'GET'
    assert get_star_ship_response.request.url == 'https://swapi.dev/api/starships/'
    assert get_star_ship_response.request.params == {"page": page }
    
    assert get_star_ship_response.status_code == 200
    assert isinstance(get_star_ship_response.response["results"], list)