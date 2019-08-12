Doc provides the high level view on Address Management Site.

DB Schema: 
Refer SQL dump to see the detailed schema structure
address_state : (id, name)
address_city : (id, name, state_id)
address_locality : (id, name, city_id)
address_address : (id, company_name, building_number, postal_code, locality_id)


APIs designed:
1. Company addresses - CRUD (http://127.0.0.1:8000/api/v1/addresses/):

    "company_name": "Test",
    "building_number": "245",
    "postal_code": "543",
    "locality": {
        "id": 1,
        "name": "Test",
        "city": {
            "id": 1,
            "name": "Test",
            "state": {
                "id": 1,
                "name": "Test"
            }
        }
    }
}

2. To retrieve address of a company by providing company name. 
URL : http://127.0.0.1:8000/api/v1/addresses/?company_name=bbb
Response : 
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "company_name": "bbb",
            "building_number": "245",
            "postal_code": "543",
            "locality": {
                "id": 1,
                "name": "MED",
                "city": {
                    "id": 1,
                    "name": "Chennai",
                    "state": {
                        "id": 1,
                        "name": "Tamilnadu"
                    }
                }
            }
        }
    ]
}

3. To list all the companies in a certain city. 
URL : http://127.0.0.1:8000/api/v1/addresses/?city=chennai
Response :

{
    "count": 5,
    "next": "http://127.0.0.1:8000/api/v1/addresses/?city=chennai&page=2",
    "previous": null,
    "results": [
        {
            "company_name": "Test1"
        },
        {
            "company_name": "Test2"
        },
        {
            "company_name": "Test3"
        },
        {
            "company_name": "Test4"
        },
        {
            "company_name": "Test5"
        }
    ]
}

4. To retrieve all the Postal Codes which has more than X number of companies. 
X to be supplied to the API as URL parameter. 

URL : http://127.0.0.1:8000/api/v1/addresses/?companies_more_than=5
Response :
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "postal_code": "543"
        }
    ]
}


API Documentation : https://documenter.getpostman.com/view/7691096/SVYurHYg?version=latest


