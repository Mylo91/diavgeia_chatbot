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

# Fetch organizations
organizations = diavgea_client.get_organizations()
orgs_list = organizations.get("organizations", [])

org_db_list = []
for org_data in orgs_list:
    organization = OraganisationModel(**org_data)
    org_db = OrganisationSql(**organization.model_dump())
    org_db_list.append(org_db)

# Create engine for diavgeia.db SQLite database
engine = create_engine(f'mysql+mysqlconnector://{config["Sql"]["username"]}:{config["Sql"]["password"]}@{config["Sql"]["host"]}:{config["Sql"]["port"]}/diavgeia')

# Create tables if not exist
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

for org_db in org_db_list:
    # Save to database
    # Check if organisation already exists in the database
    existing_org = session.query(OrganisationSql).filter_by(uid=org_db.uid).first()
    if not existing_org:
        session.add(org_db)
        session.commit()

print("stop")