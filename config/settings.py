from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', 9999))

# TODO: configuration settings
