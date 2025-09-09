from pydantic import BaseModel, Field, field_validator
from enum import Enum
from typing import Optional

class OraganisationModel(BaseModel): 
      uid            : str                    # Μοναδικός κωδικός που ταυτοποιεί τον φορέα
      label          : str                    # "Επωνυμία φορέα"
      abbreviation   : Optional[str] = None     # "Συντομογραφία φορέα"
      latinName      : str                      # "Λατινική ονομασία φορέα"
      category       : str            # "Κατηγορία φορέα"
      supervisorId   : Optional[str] = None  # "Κωδικός εποπτεύοντος φορέα"
      website        : Optional[str] = None  # "Ιστοσελίδα φορέα"
      odeManagerEmail: Optional[str] = None           # "Email φορέα"
      vatNumber      : str            # "ΑΦΜ φορέα"
      fekNumber      : str            # "ΦΕΚ ίδρυσης φορέα"
      fekIssue       : Optional[str] = None            # "Κωδικός τεύχους ΦΕΚ ίδρυσης φορέα"
      fekYear        : str            # "Έτος ΦΕΚ ίδρυσης φορέα"

