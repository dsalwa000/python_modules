#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""
This program demonstrate subtype polymorphism in action.

"""


class StreamError(Exception):
    def __init__(self, message="Stream error") -> None:
        super().__init__(message)


class DataStream(ABC):
    """Abstract class for all types of streams"""

    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type

        self.filtered_data: list[any] = []

        print(f"Stream ID: {stream_id}, Type: {stream_type}")

    @abstractmethod
    def process_batch(self, data_batch: list[any]) -> str:
        """Method which displays which data will be processed"""
        pass

    @abstractmethod
    def get_stats(self) -> dict[str, str | int | float]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type
        }

    @abstractmethod
    def filter_data(
        self,
        data_batch: list[any],
        criteria: str | None = None
    ) -> list[any]:
        """Class which filters specyfic data to display"""
        return []


class SensorStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch: list[str]) -> str:
        return f"Processing sensor batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[str],
        criteria: str | None = None
    ) -> list[int | str]:
        """
        The method counts how many readings we did and trying to find
        an average temperature.

        Args:
            data_batch: list of our reading containg an average temperature
            reading

        Raises:
            When we didn't find an average temperature or a criteria is None
            we raise StreamError

        Returns:
            List with two arguments: readings and average temperature

        """

        if criteria is None:
            raise StreamError("No criteria provided")

        readings: int = 0
        avr_temperature: int | None = None

        for value in data_batch:
            splitted = value.split(":")
            readings += 1

            if splitted[0] == criteria:
                avr_temperature = splitted[1]

        if avr_temperature is None:
            raise StreamError("No average temperature data found")

        self.filtered_data = [readings, avr_temperature]
        return self.filtered_data

    def get_stats(self):
        return super().get_stats()


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch) -> str:
        return f"Processing transaction batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: str | None = None
    ) -> list[int]:
        """
        The method counts how many operations we did and calculate new flow.

        Args:
            data_batch: list which contains out of two categories,
            buy - how much we spent on somthing,
            sell - how much we earn by selling things

        Raises:
            When criteria is None we raise StreamError

        Returns:
            List returns amout of operations and total flow of money

        """

        if criteria is None:
            raise StreamError("No criteria provided")

        operations: int = 0
        flow: int = 0

        for value in data_batch:
            splitted = value.split(":")
            operations += 1

            if splitted[0] == "buy":
                flow += int(splitted[1])

            if splitted[0] == "sell":
                flow -= int(splitted[1])

        self.filtered_data: list[int] = [operations, flow]
        return self.filtered_data

    def get_stats(self):
        return super().get_stats()


class EventStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str):
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch) -> str:
        return f"Processing event batch: {data_batch}"

    def filter_data(
        self,
        data_batch: list[any],
        criteria: str | None = None
    ) -> list[int]:
        """
        The method counts how many events we did and count errors.

        Args:
            data_batch: list of operations (login, logout or error)

        Raises:
            When criteria is None we raise StreamError

        Returns:
            List returns amout of events and total amout of errors

        """

        if criteria is None:
            raise StreamError("No criteria provided")

        events: int = 0
        errors: int = 0

        for value in data_batch:
            events += 1

            if value == "error":
                errors += 1

        self.filtered_data: list[int] = [events, errors]
        return self.filtered_data

    def get_stats(self):
        return super().get_stats()


class StreamProcessor:
    """Class which shows polymorphism using DataStream abstract class"""

    def __init__(self) -> None:
        self.streams: DataStream = []

    def addStream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def displayStream(self) -> None:
        print("Batch results")

        for stream in self.streams:
            events, _ = stream.filtered_data

            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {events} readings processed")

            if isinstance(stream, TransactionStream):
                print(f"- Transaction data: {events} operations processed")

            if isinstance(stream, EventStream):
                print(f"- Event data: {events} events processed")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    try:
        print("Initializing Sensor Stream...")

        sensor_stream = SensorStream("SENSOR_001", "Environmental Data")
        sensor_data: list[str] = ["temp:22.5", "humidity:65", "pressure:1013"]

        print(sensor_stream.process_batch(sensor_data))
        filtered_data = sensor_stream.filter_data(sensor_data, criteria="temp")

        readings, avr_temp = filtered_data

        print(
            f"Sensor analysis: {readings} readings processed, "
            f"avg temp: {avr_temp}°C"
        )

        print()

        transaction_stream = TransactionStream("TRANS_001", "Financial Data")
        transaction_data: list[str] = ["buy:100", "sell:150", "buy:75"]

        print(transaction_stream.process_batch(transaction_data))
        filtered_data: list[str] = transaction_stream.filter_data(
            transaction_data,
            criteria="flow"
        )

        operations, flow = filtered_data

        print(
            f"Transaction analysis: {operations} operations, "
            f"net flow: {flow}"
        )

        print()

        event_stream = EventStream("EVENT_001", "System Events")
        event_data: list[str] = ["login", "error", "logout"]

        print(event_stream.process_batch(event_data))
        filtered_data: list[str] = event_stream.filter_data(
            event_data,
            criteria="flow"
        )

        events, errors = filtered_data

        print(
            f"Event analysis: {events} events, "
            f"{errors} error detected"
        )

    except StreamError as e:
        print(f"StreamError: {e}")

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    try:
        streamProcessor = StreamProcessor()
        streamProcessor.addStream(sensor_stream)
        streamProcessor.addStream(transaction_stream)
        streamProcessor.addStream(event_stream)

        streamProcessor.displayStream()

        print(
            "\nAll streams processed successfully. "
            "Nexus throughput optimal."
        )

    except NameError as e:
        print(e)


if __name__ == "__main__":
    main()
