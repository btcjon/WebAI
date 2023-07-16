import os
from postgrest_py import PostgrestClient

os.environ['SUPABASE_URL'] = 'https://lmdwtkxrksgskmwpbjzs.supabase.co'
os.environ['SUPABASE_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxtZHd0a3hya3Nnc2ttd3BianpzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4ODMyMTA3MywiZXhwIjoyMDAzODk3MDczfQ.AY1XHVE3E4qAOHq57g9up7b_vHU-AN2ANYS0eq3zaDY'

from memory_manager import store_message, get_conversation

def test_memory_manager():
    # Test store_message
    print("Testing store_message...")
    store_message('test_user', 'test_session', 'Hello', 'Hi there')
    print("Stored a message. Please manually check the database to confirm.")

    # Test get_conversation
    print("Testing get_conversation...")
    conversation = get_conversation('test_user', 'test_session')
    print("Retrieved conversation:")
    print(conversation)

if __name__ == "__main__":
    test_memory_manager()
