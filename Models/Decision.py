from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime


class Attachment(BaseModel):
    filename: Optional[str]
    url: Optional[str]
    description: Optional[str]


class ExtraFieldValues(BaseModel):
    eidosYpMetavolis: Optional[str] = Field(None, description="Είδος υπηρεσιακής μεταβολής")
    relatedDecisions: Optional[List[str]] = Field(None, description="Λίστα σχετικών πράξεων")


class DecisionModel(BaseModel): 
    ada                     : str # "Αριθμός Διαδικτυακής Ανάρτησης"
    protocolNumber          : str # "Αριθμός Πρωτοκόλλου"
    subject                 : str # "Θέμα πράξης"
    issueDate               : datetime.date # "Ημερομηνία έκδοσης"
    decisionTypeId          : str # "Κωδικός τύπου πράξης"
    organizationId          : int # "Κωδικός Φορέας"
    # unitIds                 : Optional[List[str]] = Field(default_factory=list, description="Κωδικοί μονάδων")
    # signerIds               : Optional[List[str]] = Field(default_factory=list, description="Κωδικοί υπογραφόντων")
    # thematicCategoryIds     : Optional[List[str]] = Field(default_factory=list, description="Κωδικοί θεματικών κατηγοριών")
    # privateData             : Optional[bool] = Field(None, description="Περιλαμβάνει προσωπικά δεδομένα")
    # submissionTimestamp     : Optional[int] = Field(None, description="Ημερομηνία τελευταίας τροποποίησης (Unix Timestamp ms)")
    # status                  : Optional[str] = Field(None, description="Κατάσταση πράξης: PUBLISHED, PENDING_REVOCATION, REVOKED, SUBMITTED")
    # versionId               : Optional[int] = Field(None, description="Αριθμός έκδοσης")
    # documentChecksum        : Optional[str] = Field(None, description="SHA-1 του εγγράφου")
    # attachments             : Optional[List[Attachment]] = Field(default_factory=list, description="Συνημμένα έγγραφα")
    # extraFieldValues        : Optional[ExtraFieldValues] = Field(None, description="Ειδικά πεδία ανά τύπο πράξης")
    # correctedVersionId      : Optional[int] = Field(None, description="Αριθμός πρωτότυπης έκδοσης πράξης")

    @field_validator("size", mode="before")
    def convert_unix_ms_to_date(cls, value):
        if isinstance(value, int):
            # Convert milliseconds to seconds, then to date
            return datetime.fromtimestamp(value / 1000).date()
        return value

    class Config:
        schema_extra = {
            "example": {
                "ada": "ΨΕΡ123456ΑΒΓ",
                "protocolNumber": "12345",
                "subject": "Ανάθεση έργου",
                "issueDate": 1691097600000,
                "decisionTypeId": "Γ.3.5",
                "organizationId": "123456",
                "unitIds": ["unit1", "unit2"],
                "signerIds": ["signer1"],
                "thematicCategoryIds": ["category1"],
                "privateData": False,
                "submissionTimestamp": 1691101200000,
                "status": "PUBLISHED",
                "versionId": 2,
                "documentChecksum": "d3b07384d113edec49eaa6238ad5ff00",
                "attachments": [
                    {
                        "filename": "document.pdf",
                        "url": "https://example.com/doc.pdf",
                        "description": "Κύριο έγγραφο"
                    }
                ],
                "extraFieldValues": {
                    "eidosYpMetavolis": "Μετάθεση",
                    "relatedDecisions": ["ADA123", "ADA456"]
                },
                "correctedVersionId": 1
            }
        }