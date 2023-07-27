from dotenv import load_dotenv
from supabase import create_client
import os

# Load the environment variables from the .env file
load_dotenv()

# Get the Supabase URL and key from the environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Create the Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
