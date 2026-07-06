#!/bin/bash

PORT=3000
BASE_URL="http://localhost:$PORT"

echo "=== 1. Greet Customer (JSON) ==="
curl -s -H "Accept: application/json" "$BASE_URL/api/greet"
echo -e "\n"

echo "=== 2. List Products ==="
curl -s "$BASE_URL/api/products"
echo -e "\n"

echo "=== 3. Add a New Product ==="
NEW_PRODUCT=$(curl -s -X POST -H "Content-Type: application/json" \
  -d '{"name": "Ultra-Wide Gaming Monitor", "price": 449.99, "category": "Electronics", "stock": 5}' \
  "$BASE_URL/api/products")
echo "$NEW_PRODUCT"
echo -e "\n"

# Extract ID if possible
NEW_ID=$(echo "$NEW_PRODUCT" | grep -o '"id":[0-9]*' | cut -d: -f2)
if [ -z "$NEW_ID" ]; then
  NEW_ID=6
fi

echo "=== 4. Retrieve New Product (ID: $NEW_ID) ==="
curl -s "$BASE_URL/api/products/$NEW_ID"
echo -e "\n"

echo "=== 5. Update Product (Price & Stock) ==="
curl -s -X PUT -H "Content-Type: application/json" \
  -d '{"price": 429.99, "stock": 4}' \
  "$BASE_URL/api/products/$NEW_ID"
echo -e "\n"

echo "=== 6. Delete Product ==="
curl -s -X DELETE "$BASE_URL/api/products/$NEW_ID"
echo -e "\n"

echo "=== 7. Verify Deletion (Should return 404) ==="
curl -s "$BASE_URL/api/products/$NEW_ID"
echo -e "\n"
