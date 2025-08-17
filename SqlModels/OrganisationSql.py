from sqlalchemy import Column, Integer, String
from SqlModels.BaseSql import Base

class OrganisationSql(Base):
    __tablename__ = 'organisations'
    
    uid             = Column(String(255), primary_key=True)  # Μοναδικός κωδικός που ταυτοποιεί τον φορέα
    label           = Column(String(255))  # "Επωνυμία φορέα"
    abbreviation    = Column(String(255), nullable=True) # "Συντομογραφία φορέα"
    latinName       = Column(String(255))  # "Λατινική ονομασία φορέα"
    category        = Column(String(255))   # "Κατηγορία φορέα"
    supervisorId    = Column(String(255))  # "Κωδικός εποπτεύοντος φορέα"
    website         = Column(String(255))  # "Ιστοσελίδα φορέα"
    odeManagerEmail = Column(String(255))  # "Email φορέα"
    vatNumber       = Column(String(255))  # "ΑΦΜ φορέα"
    fekNumber       = Column(String(255))  # "ΦΕΚ ίδρυσης φορέα"
    fekIssue        = Column(String(255))  # "Κωδικός τεύχους ΦΕΚ ίδρυσης φορέα"
    fekYear         = Column(String(255))  # "Έτος ΦΕΚ ίδρυσης φορέα"