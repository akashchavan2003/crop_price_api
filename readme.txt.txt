API Endpoints
Crop Endpoints
1. List All Crops
URL: /api/crops/
Method: GET
Description: Retrieve all crops with their details and prices in multiple units
Response:
json

Verify

Open In Editor
Run
Copy code
[
  {
    "id": 1,
    "name": "Wheat",
    "base_price": 100.00,
    "prices": {
      "kg": 100.00,
      "g": 0.1,
      "ton": 100000.00,
      "lb": 220.462,
      "quintal": 10000.00
    }
  }
]
2. Create a Crop
URL: /api/crops/
Method: POST
Permissions: Admin only
Request Body:
json

Verify

Open In Editor
Run
Copy code
{
  "name": "Rice",
  "base_price": 150.00
}
3. Get Specific Crop
URL: /api/crops/{id}/
Method: GET
Description: Retrieve details of a specific crop
4. Price Conversion
URL: /api/crops/{id}/convert_price/
Method: GET
Query Params: unit (optional: kg, g, tons, lb, quintal)
Example: /api/crops/1/convert_price/?unit=lb
Response:
json

Verify

Open In Editor
Run
Copy code
{
  "price": 220.462
}
5. Bulk Delete Crops
URL: /api/crops/bulk_delete/
Method: DELETE
Permissions: Admin only
Request Body:
json

Verify

Open In Editor
Run
Copy code
{
  "ids": [1, 2, 3]
}
6. Bulk Update Crops
URL: /api/crops/bulk_update/
Method: PUT
Permissions: Admin only
Request Body:
json

Verify

Open In Editor
Run
Copy code
[
  {
    "id": 1,
    "name": "Updated Wheat",
    "base_price": 120.00
  }
]
Search Functionality
URL: /api/crops/?search=wheat
Description: Search crops by name




Admin Endpoints (JWT Authentication Required):

POST /api/crops/
PUT /api/crops/{id}/
PATCH /api/crops/{id}/
DELETE /api/crops/{id}/
DELETE /api/crops/bulk_delete/
PUT /api/crops/bulk_update/