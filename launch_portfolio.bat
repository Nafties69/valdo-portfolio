@echo off
REM Launch the local portfolio website in the default browser
start "" "C:\dev\valdo-portfolio\docs\index.html"

REM Launch the Streamlit App in a new window
start "StockAuto Streamlit App" cmd /k "cd C:\dev\stockauto && python -m streamlit run streamlit_app.py"
