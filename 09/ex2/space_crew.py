from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator


VALID_MISSION = {
    'mission_id': 'M2024_TITAN',
    'mission_name': 'Solar Observatory Research Mission',
    'destination': 'Solar Observatory',
    'launch_date': '2024-03-30T00:00:00',
    'duration_days': 451,
    'crew': [
        {
            'member_id': 'CM001',
            'name': 'Sarah Williams',
            'rank': 'captain',
            'age': 43,
            'specialization': 'Mission Command',
            'years_experience': 19,
            'is_active': True
        },
        {
            'member_id': 'CM002',
            'name': 'James Hernandez',
            'rank': 'captain',
            'age': 43,
            'specialization': 'Pilot',
            'years_experience': 30,
            'is_active': True
        },
        {
            'member_id': 'CM003',
            'name': 'Anna Jones',
            'rank': 'cadet',
            'age': 35,
            'specialization': 'Communications',
            'years_experience': 15,
            'is_active': True
        },
        {
            'member_id': 'CM004',
            'name': 'David Smith',
            'rank': 'commander',
            'age': 27,
            'specialization': 'Security',
            'years_experience': 15,
            'is_active': True
        },
        {
            'member_id': 'CM005',
            'name': 'Maria Jones',
            'rank': 'cadet',
            'age': 55,
            'specialization': 'Research',
            'years_experience': 30,
            'is_active': True
        }
    ],
    'mission_status': 'planned',
    'budget_millions': 2208.1
}

INVALID_MISSION = {
    'mission_id': '2024_EAGLE',
    'mission_name': 'Cosmos',
    'destination': 'Probably Galapagos',
    'launch_date': '2024-01-30T00:00:00',
    'duration_days': 366,
    'crew': [
        {
            'member_id': 'CM001',
            'name': 'Sarah Williams',
            'rank': 'lieutenant',
            'age': 43,
            'specialization': 'Mission Command',
            'years_experience': 1,
            'is_active': False
        },
        {
            'member_id': 'CM001',
            'name': 'Sarah Williams',
            'rank': 'cadet',
            'age': 43,
            'specialization': 'Mission Command',
            'years_experience': 3,
            'is_active': True
        },
        {
            'member_id': 'CM001',
            'name': 'Sarah Williams',
            'rank': 'lieutenant',
            'age': 43,
            'specialization': 'Mission Command',
            'years_experience': 42,
            'is_active': True
        },
    ],
    'mission_status': 'not planned at all',
    'budget_millions': 1.0
}


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(default=Rank.cadet)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True, strict=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(description="DateTime field")
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def space_check(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID doesn't start with M")

        boss_counter: int = 0
        experienced_crew: int = 0

        for crew_member in self.crew:
            rank: Rank = crew_member.rank
            experience: int = crew_member.years_experience
            active: bool = crew_member.is_active

            if active is False:
                raise ValueError("All crew members must be active")

            if rank == Rank.captain or rank == Rank.commander:
                boss_counter += 1

            if experience >= 5:
                experienced_crew += 1

        if boss_counter == 0:
            raise ValueError("We need at least one Commander or Capitan!")

        if (
            self.duration_days > 365 and
            len(self.crew) * 0.5 > experienced_crew
        ):
            raise ValueError(
                "Not enough experienced crew! We need at least 50% !"
            )

        return self

    def display_mission(self) -> None:
        print(f"Mission ID: {self.mission_id}")
        print(f"Name: {self.mission_name}")
        print(f"Destination: {self.destination}")

        launch_value = (
            self.launch_date.isoformat()
            if isinstance(self.launch_date, datetime)
            else self.launch_date
        )
        print(f"Launch date: {launch_value}")
        print(f"Duration: {self.duration_days} days")
        print(f"Status: {self.mission_status}")
        print(f"Budget: {self.budget_millions} million")

        print(f"Crew ({len(self.crew)}):")
        for i, member in enumerate(self.crew, start=1):
            print(
                f"  {i}. {member.name} ({member.member_id}) | "
                f"{member.rank.value} | age {member.age} | "
                f"{member.specialization} | exp {member.years_experience}y | "
                f"active={member.is_active}"
            )


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================\n")

    validAlienContact = SpaceMission(
        **VALID_MISSION
    )

    validAlienContact.display_mission()

    try:
        print("\nExpected validation error:")
        print("======================================")

        invalidAlienContact = SpaceMission(
            **INVALID_MISSION
        )

        invalidAlienContact.display_mission()

    except ValueError as e:
        print("ValueError:")
        print(e)
    except ValidationError as e:
        print("ValidationError:")
        print(e)

    print("\nThe end!")


if __name__ == "__main__":
    main()
