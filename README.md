# net-doktor

## Starting the frontend server
1. Go to the frontend folder  
```sh 
cd net-docktor-frontend
```
2. Compile 
```sh 
npm run build  
```
3. Start the application
```sh 
npm run dev  
```


## Starting the frontend server
1. Go to the backend folder  
```sh 
cd net-docktor-backend
```

2. Activate up env.
```sh 
source env/bin/activate 
```

3. Go to backendService folder
```sh 
cd backendService
```

4. Install the requirements
```sh 
pip install requirements.text
```

5. Start the server. 
Note: The port number used by frontend is 8081 to access the api
```sh 
python manage.py runserver <port-number>   
python manage.py runserver 8081   
```
