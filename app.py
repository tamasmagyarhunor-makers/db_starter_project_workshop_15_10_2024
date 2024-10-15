from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.artist import Artist


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

artist = Artist(3, "Celldweller", "rock")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artist_repository.create(artist)

artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

    # we expect Celldweller to show up last.
