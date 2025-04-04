import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import streamlit as st
import os
from gspread.exceptions import SpreadsheetNotFound
from dotenv import load_dotenv

load_dotenv()

def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    credentials_dict = {
        "type": "service_account",
        "project_id": os.getenv("GOOGLE_PROJECT_ID"),
        "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.getenv("GOOGLE_CERT_URL"),
    }

    creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
    client = gspread.authorize(creds)
    return client

def log_entry(sheet_name, entry):
    client = authenticate_google_sheets()
    try:
        sheet = client.open(sheet_name).sheet1
    except SpreadsheetNotFound:
        # Create the spreadsheet if it doesn't exist
        spreadsheet = client.create(sheet_name)
        sheet = spreadsheet.sheet1
        st.info(f"Spreadsheet '{sheet_name}' was not found and has been created.")
    
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    hour = now.strftime("%H:00")
    
    data = sheet.get_all_values()
    headers = sheet.row_values(1)
    
    if "Date" not in headers:
        headers = ["Date"] + [f"{i}:00" for i in range(24)]
        sheet.insert_row(headers, 1)
    
    date_column = headers.index("Date") + 1
    hour_column = headers.index(hour) + 1 if hour in headers else len(headers) + 1
    
    row_index = next((i + 1 for i, row in enumerate(data) if row and row[0] == date_str), None)
    
    if row_index is None:
        sheet.append_row([date_str] + [""] * 24)
        row_index = len(data) + 1
    
    current_value = sheet.cell(row_index, hour_column).value
    new_value = f"{current_value} | {entry}" if current_value else entry
    sheet.update_cell(row_index, hour_column, new_value)
    
    return "Entry logged successfully!"

# Streamlit App
st.title("📖 Virtual Diary")
entry = st.text_area("Write your diary entry:")
if st.button("Save Entry"):
    if entry.strip():
        result = log_entry("Virtual Diary", entry)
        st.success(result)
    else:
        st.warning("Please enter some text before saving.")
