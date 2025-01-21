Steps for Demo:
1. Execute the db_script file to create database tables.
2. Run the main server using command `uvicorn main:app --port 8000`
3. Run the thirt party server using command `uvicorn third_party:app --port 8001`
4. Run the simulate_users file with desired endpoint 


To run the main server in using gunicorn : 

for multiple workers
`uvicorn main:app --workers 4 --port 8000`