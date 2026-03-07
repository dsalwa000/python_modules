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

        return (
            f"Processed {length} numeric values, "
            f"sum={sum}, avg={sum / length}"
        )

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        return f"Processing data: {data}"

    def validate(self, data: str) -> str:
        print("Validation: Text data verified")

        splitted: str = data.split(" ")

        words_count: int = 0
        length: int = 0

        for _ in data:
            length += 1

        for _ in splitted:
            words_count += 1

        return (
            f"Processed text: "
            f"{length} characters, {words_count} words"
        )

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        return f"Processing data: {data}"

    def validate(self, data: str) -> str:
        print("Validation: Log entry verified")
        if data == "ERROR: Connection timeout":
            return "[ALERT] ERROR level detected: Connection timeout"
        else:
            return "[INFO] INFO level detected: System ready"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numericData: list[int] = [1, 2, 3, 4, 5]
    numericProcessor: NumericProcessor = NumericProcessor()
    print(f"Processing data: {numericProcessor.process(numericData)}")
    numericValidated = numericProcessor.validate(numericData)
    print(numericProcessor.format_output(numericValidated))

    print()

    print("Initializing Text Processor...")
    text_data: str = "Hello Nexus World"
    textProcessor: TextProcessor = TextProcessor()
    print(f"Processing data: {textProcessor.process(text_data)}")
    textValidated = textProcessor.validate(text_data)
    print(textProcessor.format_output(textValidated))

    print()

    print("Initializing Log Processor...")
    log_error: str = "ERROR: Connection timeout"
    logProcessor: LogProcessor = LogProcessor()
    print(f"Processing data: {log_error}")
    logValidated = logProcessor.validate(log_error)
    print(logProcessor.format_output(logValidated))

    print()

    print("=== Polymorphic Processing Demo ===")

    data_one: list[int] = [1, 2, 3]
    data_two: str = "Nexus text"
    data_three: str = "INFO: System ready"

    try:
        numeric_result = numericProcessor.validate(data_one)
        text_result = textProcessor.validate(data_two)
        log_result = logProcessor.validate(data_three)
        print(f"Result 1: {numeric_result}")
        print(f"Result 2: {text_result}")
        print(f"Result 3: {log_result}")
    except (ValueError, TypeError):
        print("Error: Polymorphic processing failed")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
