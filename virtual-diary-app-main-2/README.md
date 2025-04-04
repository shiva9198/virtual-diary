# virtual-diary-app

## Description
Virtual Diary App is a digital platform that allows users to maintain a personal diary. Users can securely write, edit, and manage their daily entries. The app integrates with Google Sheets to store diary entries, ensuring data persistence and accessibility. Each entry is timestamped and organized by date and hour for easy retrieval.

## Features
- **Google Sheets Integration**: Automatically logs diary entries into a Google Sheet, organized by date and hour.
- **Dynamic Sheet Creation**: Creates a new Google Sheet if the specified sheet does not exist.
- **Timestamped Entries**: Automatically timestamps entries with the current date and hour.
- **Multiple Entries per Hour**: Supports appending multiple entries for the same hour.
- **Streamlit Interface**: Provides a simple and interactive user interface for writing and saving diary entries.
- **Real-Time Feedback**: Displays success or warning messages based on user actions.
- **Environment Configuration**: Uses `.env` files to securely manage Google Service Account credentials.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/shiva9198/virtual-diary-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd virtual-diary-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add the following variables with your Google Service Account credentials:
     ```
     GOOGLE_PROJECT_ID=<your_project_id>
     GOOGLE_PRIVATE_KEY_ID=<your_private_key_id>
     GOOGLE_PRIVATE_KEY=<your_private_key>
     GOOGLE_CLIENT_EMAIL=<your_client_email>
     GOOGLE_CLIENT_ID=<your_client_id>
     GOOGLE_CERT_URL=<your_cert_url>
     ```
5. Run the application:
   ```bash
   streamlit run script.py
   ```
6. Open your browser and navigate to the Streamlit app URL provided in the terminal.

