from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from prosanearinfo.config import get_config

db = create_engine(get_config()['database_uri'])
Session = sessionmaker(db)
