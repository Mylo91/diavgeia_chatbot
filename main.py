from Clients.OpendataClient import OpendataClient

from Models.Organisation import OraganisationModel
import json

# SqlAlchemy imports
from sqlalchemy import create_engine
from SqlModels.BaseSql import Base
from sqlalchemy.orm import sessionmaker

from SqlModels.OrganisationSql import OrganisationSql

diavgea_client = OpendataClient(root="https://diavgeia.gov.gr/opendata")

configuration_file = "config.json"
with open(configuration_file) as f:
    config = json.load(f)

tmp = diavgea_client.get_organizations()
# Example usage
#response = diavgea_client.get_decision("6Π5Μ46Ψ8ΒΠ-ΕΨΟ")
organization = OraganisationModel(**tmp["organizations"][0])

org_db = OrganisationSql(**organization.model_dump())

# Create engine for diavgeia.db SQLite database
engine = create_engine(f'mysql+mysqlconnector://{config["Sql"]["username"]}:{config["Sql"]["password"]}@{config["Sql"]["host"]}:{config["Sql"]["port"]}/diavgeia')

# Create tables if not exist
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Save to database
session.add(org_db)
session.commit()

print("stop")