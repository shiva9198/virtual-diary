import pandas as pd
import os
from datetime import datetime

FILE_NAME = "diary_entries.xlsx"
hourly_columns = [f"{hour}:00" for hour in range(24)]

def initialize_diary_file(file_path="diary_entries.xlsx"):
    global FILE_NAME
    FILE_NAME = file_path
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Date"] + hourly_columns)
        df.to_excel(FILE_NAME, index=False)

def add_entry(content):
    now = datetime.now()
    save_entry(now.strftime("%Y-%m-%d"), now.strftime("%H:00"), content, append=True)

def save_entry(date, hour, content, append=False):
    df = pd.read_excel(FILE_NAME)

    if date in df["Date"].values:
        row_index = df[df["Date"] == date].index[0]
        if append and pd.notna(df.at[row_index, hour]):
            df.at[row_index, hour] += f"\n{content}"
        else:
            df.at[row_index, hour] = content
    else:
        new_entry = pd.DataFrame([[date] + ["" for _ in range(24)]], columns=["Date"] + hourly_columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        row_index = df[df["Date"] == date].index[0]
        df.at[row_index, hour] = content

    df.to_excel(FILE_NAME, index=False)

def get_entries(date):
    """Returns a dict of all entries for the given date."""
    df = pd.read_excel(FILE_NAME)
    if date in df["Date"].values:
        row = df[df["Date"] == date].iloc[0]
        return {hour: row[hour] for hour in hourly_columns if pd.notna(row[hour])}
    return {}