# ai_google_gemini
Projects with google gemini




### Set up a Python virtual environment
```
python3 -m venv gemini-streamlit

source gemini-streamlit/bin/activate
```


### Install dependencies
```
pip install -r requirements.txt
```

### Run the app in local server
```
streamlit run app.py \
--browser.serverAddress=localhost \
--server.enableCORS=false \
--server.enableXsrfProtection=false \
--server.port 8080
```