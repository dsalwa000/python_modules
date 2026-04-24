from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(description="DateTime field")
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field(default=ContactType.radio)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=True, strict=True)

    @model_validator(mode='after')
    def contact_check(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID doesn't start with AC")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified!")

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact needs at least 3 people!")

        if self.message_received is None and self.signal_strength < 7.0:
            raise ValueError("Strong signals (>= 7.0) must have a message!")

        return self

    def display_contact(self) -> None:
        print(f"ID: {self.contact_id}")
        print(f"Time: {self.timestamp}")
        print(f"Location: {self.location}")
        print(f"Contact: {self.contact_type.value}")
        print(f"Signal strength: {self.signal_strength}")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witness count: {self.witness_count} people")
        print(f"Is Verified: {self.is_verified}")

        if self.message_received is not None:
            print(f"Message received: {self.message_received}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================\n")

    validAlienContact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2026-04-24",
        location="Piaseczno",
        contact_type=ContactType.physical,
        signal_strength=9.8,
        duration_minutes=1440,
        witness_count=100,
        message_received="Pierogi",
        is_verified=True
    )

    validAlienContact.display_contact()

    print("\nExpected validation error:")
    print("======================================")

    try:
        errorAlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-04-24",
            location="Krakow",
            contact_type=ContactType.physical,
            signal_strength=1.9,
            duration_minutes=1440,
            witness_count=4,
            message_received="Obwarzanek",
            is_verified=True
        )

        errorAlienContact.display_contact()

    except ValueError as e:
        print("ValueError:")
        print(e)
    except ValidationError as e:
        print("ValidationError:")
        print(e)

    print("\nThe end!")


if __name__ == "__main__":
    main()
