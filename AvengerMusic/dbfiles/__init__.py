from async_pymongo import AsyncClient
import config

DBNAME = "avengermusicdb"

mongo = AsyncClient(config.MONGO_DB_URI)
dbname = mongo[DBNAME]
