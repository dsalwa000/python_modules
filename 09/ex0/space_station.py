from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(description="DataTime Field")
    is_operational: bool = Field(default=True, strict=True)
    notes: str | None = Field(default=None, max_length=200)

    def display_station(self) -> None:
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print(f"Status: {self.is_operational}")
        print(f"Last maintenance: {self.last_maintenance}")

        if self.notes is not None:
            print(f"Notes: {self.notes}")


def main() -> None:
    print("Space Station Data Validation\n")
    print("======================================")

    print("Valid station created:")
    correctSpaceStation = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-04-24",
        is_operational=True,
        notes="Some notes"
    )
    correctSpaceStation.display_station()

    try:
        print("\nExpected validation error:")
        correctSpaceStation = SpaceStation(
            station_id="ISS001",
            name=2,
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-0-24",
            is_operational="True",
            notes="Some notes"
        )

    except ValidationError as e:
        print(e)

    print("\n The end!")


if __name__ == "__main__":
    main()
