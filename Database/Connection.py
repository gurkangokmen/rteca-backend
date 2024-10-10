from databases import Database

class Connection:
    DATABASE_URL = "postgresql://root:12345@localhost/rteca-db"
    database = Database(DATABASE_URL)

# Expose the database object
database = Connection.database