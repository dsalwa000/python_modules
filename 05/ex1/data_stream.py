#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""
This program demonstrate subtype polymorphism in action
"""


class StreamError(Exception):
    def __init__(self, message="Stream error"):
        super().__init__(message)


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        print(f"Stream ID: {self.stream_id}, Type: {stream_type}")

    @abstractmethod
    def process_batch(self, data_batch: list[any]) -> str:
        pass

    # Dodaj do tych 2 metod implementacje
    @abstractmethod
    def filter_data(
        self,
        data_batch: list[any],
        criteria: str | None = None
    ) -> list[any]:
        return []

    @abstractmethod
    def get_stats(self) -> dict[str, str | int | float]:
        return {}


class SensorStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str):
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch) -> str:
        return f"Processing sensor batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: str | None = None
    ) -> list[any]:

        readings = 0
        avr_temperature = None

        for value in data_batch:
            splitted = value.split(":")
            readings += 1

            if splitted[0] == criteria:
                avr_temperature = splitted[1]

        try:
            if avr_temperature is None:
                raise StreamError("No average temperature data")
        except StreamError as e:
            print(f"Stream error: {e}")

        return [readings, avr_temperature]

    def get_stats(self) -> dict[str, str | int | float]:
        return {}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str):
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch) -> str:
        return f"Processing transaction batch: {data_batch}"


class EventStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str):
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch) -> str:
        return f"Processing event batch: {data_batch}"


class StreamProcessor:
    def __init__(self):
        pass


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    

    print("Initializing Sensor Stream...")


if __name__ == "__main__":
    main()
