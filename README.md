# 🐍⚡ API with chatGPT to implement in any application

## ⚙ SETUP
----------
1) Create a virtual environment using the command
~~~
python -m venv venv 
~~~
2) Activate the virtual environment using the command
~~~
venv/Scripts/activate
~~~
3) Install dependencies using the command
~~~
pip install -r requirements.txt
~~~
4) Agregar al archivo de configuracion .env la apikey de openai previamente sacada de la pagina oficial de [openai](https://platform.openai.com/account/api-keys)

## 💨 Run the program
-----
![image](https://user-images.githubusercontent.com/76167482/230817118-fef843c5-9108-4934-b33f-34dcf7a7584d.png)

To run the program, open the command prompt and execute the following command:
~~~
uvicorn main:app --reload
~~~

With the previous command, the uvicorn server of FastAPI will be launched. Then we will have to go to the browser and enter the address that is shown in the console (usually localhost:8000).

Next, we will go to test the endpoint on the Swagger documentation interface using the following endpoint:

~~~
localhost:8000/docs
~~~

Once inside the endpoint chat, what we need to do is modify the value of "text" in the JSON. We should put the string with what we want to send to the OpenAI AI, so that it responds to us with the corresponding JSON format.
