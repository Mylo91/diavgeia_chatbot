from pydantic import BaseModel, Field, field_validator
from enum import Enum

class OraganisationModel(BaseModel): 
      uid                          : str  # Μοναδικός κωδικός που ταυτοποιεί τον φορέα
      label                        : str  # "Επωνυμία φορέα"
      abbreviation                 : str | None = None  # "Συντομογραφία φορέα"
      latinName                    : str  # "Λατινική ονομασία φορέα"
      category                     : str # "Κατηγορία φορέα"
      supervisorId                 : str  # "Κωδικός εποπτεύοντος φορέα"
      website                      : str  # "Ιστοσελίδα φορέα"
      odeManagerEmail              : str  # "Email φορέα"
      vatNumber                    : str  # "ΑΦΜ φορέα"
      fekNumber                    : str  # "ΦΕΚ ίδρυσης φορέα"
      fekIssue                     : str  # "Κωδικός τεύχους ΦΕΚ ίδρυσης φορέα"
      fekYear                      : str  # "Έτος ΦΕΚ ίδρυσης φορέα"

