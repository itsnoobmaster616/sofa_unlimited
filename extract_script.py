
import pyzipper
import os
import sys

def extract_protected_zip(zip_file, password):
    """Extracts a password-protected zip file using AES encryption."""
    try:
        with pyzipper.AESZipFile(zip_file, 'r') as zipf:
            zipf.setpassword(password.encode('utf-8'))
            zipf.extractall('.')
        print('✅ Successfully extracted protected script')
        return True
    except Exception as e:
        print(f'❌ Extraction failed: {e}')
        return False

if __name__ == "__main__":
    zip_file = "sports_scraper.zip"
    password = os.environ.get('ZIP_PASSWORD')

    if not password:
        print("❌ ZIP_PASSWORD environment variable not set")
        sys.exit(1)

    if not os.path.exists(zip_file):
        print(f"❌ Zip file not found: {zip_file}")
        sys.exit(1)

    if not extract_protected_zip(zip_file, password):
        sys.exit(1)
