# Configuration file for the application

DATABASE_URL = "postgres://user:password@localhost:5432/mydatabase"
API_KEY = "sk_test_51JxBsjG6ZyF0RrXcV1aI2X00abcdef123456"

def connect_to_db():
    print("Connecting to database...")

if __name__ == "__main__":
    connect_to_db()
