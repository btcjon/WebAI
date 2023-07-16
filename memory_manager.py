import os
postgrest_py import PostgrestPy

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

supabase = PostgrestClient(supabase_url, headers={
    "apikey": supabase_key,
    "Authorization": f"Bearer {supabase_key}"
})

def ensure_table_exists():
    result = supabase.rpc('create_conversations_table')
    if result.error:
        print(f"Error when creating table: {result.error}")
    else:
        print("Table 'conversations' created successfully.")

def store_message(user_id, session_id, message, response):
    ensure_table_exists()
    result = supabase.table('conversations').insert({
        'user_id': user_id,
        'session_id': session_id,
        'message': message,
        'response': response
    }).execute()
    if result.error:
        print(f"Error when storing message: {result.error}")
    else:
        print(f"Message stored successfully for user {user_id} in session {session_id}.")

def get_conversation(user_id, session_id):
    ensure_table_exists()
    result = supabase.table('conversations').select().eq('user_id', user_id).eq('session_id', session_id).execute()
    if result.error:
        print(f"Error when executing query: {result.error}")
        return None
    else:
        return result.data
