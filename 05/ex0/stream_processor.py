#!/usr/bin/env python3
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: any) -> str:
        pass

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: list[int]) -> str:
        return f"Processing data: {data}"

    def validate(self, data: list[int]) -> str:
        print("Validation: Numeric data verified")

        sum: int = 0
        length: int = 0

        for value in data:
            sum += value
            length += 1

        return {
            f"Output: Processed {length} numeric values, "
            f"sum={sum}, avg={sum / length}"
        }

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        return f"Processing data: {data}"

    def validate(self, data: str) -> str:
        print("Validation: Text data verified")

        splitted = data.split(" ")

        words_count: int = 0
        length: int = 0

        for _ in data:
            length += 1

        for _ in splitted:
            words_count += 1

        return {
            f"Output: Processed text: "
            f"{length} characters, {words_count} words"
        }

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        return f"Processing data: {data}"

    def validate(self, data: str) -> str:
        print("Validation: Text data verified")

        splitted = data.split(" ")

        words_count: int = 0
        length: int = 0

        for _ in data:
            length += 1

        for _ in splitted:
            words_count += 1

        return {
            f"Output: Processed text: "
            f"{length} characters, {words_count} words"
        }

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")


if __name__ == "__main__":
    main()
