# 📊 Google Sheets Integration Setup Guide

This guide will help you set up Google Sheets as the data storage backend for your Streamlit app.

## 🎯 Overview

Your app now stores user data in Google Sheets instead of a local CSV file. This is perfect for Streamlit Cloud deployment because:
- ✅ Data persists across app restarts
- ✅ Accessible from anywhere
- ✅ Easy to view and export
- ✅ Free for personal use

## 📝 Step-by-Step Setup

### Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **"Create Project"** or select an existing one
3. Name it something like: `streamlit-app-data`
4. Click **"Create"**

### Step 2: Enable Google Sheets API

1. In your project, go to **"APIs & Services"** → **"Library"**
2. Search for **"Google Sheets API"**
3. Click on it and press **"Enable"**
4. Also enable **"Google Drive API"** (search and enable it too)

### Step 3: Create Service Account Credentials

1. Go to **"APIs & Services"** → **"Credentials"**
2. Click **"Create Credentials"** → **"Service Account"**
3. Fill in:
   - **Service account name**: `streamlit-sheets-connector`
   - **Service account ID**: (auto-filled)
4. Click **"Create and Continue"**
5. For role, select: **"Editor"** (or "Basic" → "Editor")
6. Click **"Continue"** → **"Done"**

### Step 4: Generate JSON Key

1. In the **"Credentials"** page, find your service account
2. Click on the service account email
3. Go to the **"Keys"** tab
4. Click **"Add Key"** → **"Create new key"**
5. Choose **"JSON"** format
6. Click **"Create"**
7. A JSON file will download automatically - **KEEP IT SAFE!**

### Step 5: Configure Streamlit Secrets (Local Testing)

For **local development**, create a `.streamlit/secrets.toml` file:

1. Create the `.streamlit` directory in your project root:
```bash
mkdir .streamlit
```

2. Create `secrets.toml` file inside it:
```bash
# .streamlit/secrets.toml
```

3. Add your credentials (from the downloaded JSON file):
```toml
# Sheet name (optional, default: streamlit_user_data)
sheet_name = "streamlit_user_data"

[gcp_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR-PRIVATE-KEY-HERE\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
```

⚠️ **IMPORTANT**: The `.streamlit/secrets.toml` file is already in `.gitignore` - never commit it to Git!

### Step 6: Configure Streamlit Cloud Secrets

For **production deployment on Streamlit Cloud**:

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click on your deployed app
3. Go to **"Settings"** → **"Secrets"**
4. Paste the same content from your `secrets.toml` file
5. Click **"Save"**

### Step 7: Test Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

If configured correctly, the app will:
- Create a Google Sheet named "streamlit_user_data" (or your custom name)
- Save user submissions to the sheet
- Display statistics in the sidebar

## 🔍 How to View Your Data

### Option 1: Google Sheets Interface
1. Go to [Google Sheets](https://docs.google.com/spreadsheets/)
2. Find your sheet (e.g., "streamlit_user_data")
3. Open it to view all collected data

### Option 2: In the App
- Expand the **"🔍 View All Collected Data (Admin)"** section at the bottom
- See real-time data, charts, and download options

## 🎨 Customization

### Change Sheet Name

In `.streamlit/secrets.toml` (and Streamlit Cloud secrets):
```toml
sheet_name = "my_custom_sheet_name"
```

### Share Access to the Sheet

The app automatically makes sheets readable by anyone with the link. To share edit access:

1. Open the Google Sheet
2. Click **"Share"**
3. Add the service account email: `your-service-account@your-project.iam.gserviceaccount.com`
4. Give it "Editor" permissions

## 🐛 Troubleshooting

### "Error connecting to Google Sheets"
- ✅ Verify Google Sheets API is enabled
- ✅ Verify Google Drive API is enabled
- ✅ Check that `secrets.toml` is in `.streamlit/` folder
- ✅ Verify JSON credentials are correct

### "SpreadsheetNotFound"
- The app should auto-create the sheet
- Make sure the service account has Drive permissions
- Check the sheet name in secrets matches

### "Insufficient permissions"
- Ensure the service account has "Editor" role
- Re-download the JSON key if needed

### "Local works, but Streamlit Cloud doesn't"
- Make sure you've added secrets in Streamlit Cloud settings
- Verify the format matches exactly (especially the private_key with `\n`)

## 📚 Additional Resources

- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
- [gspread Documentation](https://docs.gspread.org/)
- [Google Sheets API](https://developers.google.com/sheets/api)

## 🔐 Security Best Practices

1. ✅ Never commit `secrets.toml` to Git
2. ✅ Never share your JSON key file publicly
3. ✅ Use environment-specific service accounts
4. ✅ Regularly rotate credentials
5. ✅ Limit service account permissions to only what's needed

---

## 🚀 Quick Start Checklist

- [ ] Created Google Cloud Project
- [ ] Enabled Google Sheets API
- [ ] Enabled Google Drive API
- [ ] Created Service Account
- [ ] Downloaded JSON key
- [ ] Created `.streamlit/secrets.toml`
- [ ] Added credentials to `secrets.toml`
- [ ] Tested locally with `streamlit run app.py`
- [ ] Added secrets to Streamlit Cloud
- [ ] Deployed and tested on Streamlit Cloud

Once all steps are complete, your app will store data in Google Sheets! 🎉

