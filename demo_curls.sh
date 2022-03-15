# Base
curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json'


# Get user
curl -X 'GET' \
  'http://127.0.0.1:8000/users/1' \
  -H 'accept: application/json'

# Create user
curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"name": "test user","title": "dummy","email": "test@techradar.com","age": 12}'

# Create async user
curl -X 'POST' \
  'http://127.0.0.1:8000/users/async' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"name": "test user","title": "dummy","email": "test@techradar.com","age": 12}'