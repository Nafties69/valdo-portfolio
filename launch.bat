@echo off

echo Installing dependencies...
pip install -r requirements.txt

echo Launching Piculator...
streamlit run C:\dev\Piculator\streamlit_app.py
