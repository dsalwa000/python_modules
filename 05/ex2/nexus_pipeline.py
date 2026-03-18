"""
This project demonstrates inheritance, error handling, comprehensions,
data processing and duck typing.

"""
from abc import ABC, abstractmethod
from typing import Protocol
from enum import Enum
import json
import csv


class PipelineType(Enum):
    JSON = "JSON"
    CSV = "CSV"
    STREAM = "STREAM"


class PipelineError(Exception):
    pass


class ProcessingStage(Protocol):
    """Protocol class for our structure"""

    def process(self, data: any) -> any:
        ...


class InputStage():

    def process(self, data: any) -> dict:
        print(f"Output: {data}")
        return data


class TransformStage():

    def process(self, data: any, type: PipelineType) -> dict:

        if type is PipelineType.JSON:
            print("Transform: Enriched with metadata and validation")

        if type is PipelineType.CSV:
            print("Transform: Parsed and structured data")

        if type is PipelineType.STREAM:
            print("Transform: Aggregated and filtered")

        return data


class OutputStage():

    def process(self, data: any, type: PipelineType) -> str:

        if type is PipelineType.JSON:
            return (f"Output: Processed temperature reading: "
                    f"{data['value']}°C (Normal range)")

        if type is PipelineType.CSV:
            if isinstance(data, list):
                actions = sum(1 for row in data if "action" in row)
            else:
                actions = 1 if "action" in data else 0
            return f"Output: User activity logged: {actions} actions processed"

        if type is PipelineType.STREAM:
            count = len(data)
            avg = sum(i.get("temp", 0) for i in data) / count if count else 0
            return (f"Output: Stream summary: {count} readings, "
                    f"avg: {avg:.1f}°C")


class ProcessingPipeline(ABC):
    """Abstract base for adapters which contains stages"""

    def __init__(self, pipeline_id: PipelineType):
        self.pipeline_id = pipeline_id

        self.stages: list[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: any, type: PipelineType) -> any:
        """
        It handles differently Input, Transform and Output data
        for each type of Adapter.

        """
        pass


class JSONAdapter(ProcessingPipeline):

    def process(self, data: any, type: PipelineType) -> any:

        if type is not PipelineType.JSON:
            raise PipelineError("Wrong pipeline type, expected JSON")

        parsed_data = json.loads(data)

        # Processing Input
        input_result = self.stages[0].process(parsed_data)

        # Transform
        processed_data = self.stages[1].process(input_result, type)

        # Output
        our_result = self.stages[2].process(processed_data, type)

        return our_result


class CSVAdapter(ProcessingPipeline):

    def process(self, data: any, type: PipelineType) -> any:

        if type is not PipelineType.CSV:
            raise PipelineError("Wrong pipeline type, expected CSV")

        reader = csv.DictReader(data.splitlines())
        parsed_data = list(reader)

        # Processing Input
        input_result = self.stages[0].process(parsed_data)

        # Transform
        processed_data = self.stages[1].process(input_result, type)

        # Output
        our_result = self.stages[2].process(processed_data, type)

        return our_result


class StreamAdapter(ProcessingPipeline):

    def process(self, data: any, type: PipelineType) -> any:

        if type is not PipelineType.STREAM:
            raise PipelineError("Wrong pipeline type, expected STREAM")

        parsed_data = json.loads(data)

        # Processing Input
        input_result = self.stages[0].process(parsed_data)

        # Transform
        processed_data = self.stages[1].process(input_result, type)

        # Output
        our_result = self.stages[2].process(processed_data, type)

        return our_result


class NexusManager:
    def __init__(self) -> None:

        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second")

        self.pipelines: list[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """This function automatically adds stages for each added pipeline"""

        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())

        self.pipelines.append(pipeline)

    def process_data(
            self,
            type: PipelineType,
            raw_data: any
    ) -> None:

        for pipeline in self.pipelines:

            if pipeline.pipeline_id == type:
                print(pipeline.process(raw_data, type))


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    nexusManager = NexusManager()

    print("=== Multi-Format Data Processing ===\n")
    print(
        "Each pipeline has 3 stages by default:"
        "Input, Tranformation and Output"
    )

    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    json_adapter = JSONAdapter(PipelineType.JSON)
    csv_adapter = CSVAdapter(PipelineType.CSV)
    stream_adapter = StreamAdapter(PipelineType.STREAM)

    try:
        nexusManager.add_pipeline(json_adapter)
        nexusManager.add_pipeline(csv_adapter)
        nexusManager.add_pipeline(stream_adapter)

        print("\nProcessing JSON data through pipeline...")
        json_data = '{"sensor": "temp", "value": 23.5, "unit": "C"}'
        nexusManager.process_data(PipelineType.JSON, json_data)

        print("\nProcessing CSV data through same pipeline...")
        csv_data = "user,action\nadmin,login"
        nexusManager.process_data(PipelineType.CSV, csv_data)

        print("\nProcessing Stream data through same pipeline...")
        stream_data = '[{"temp": 22.0}, {"temp": 22.5}, {"temp": 23.0}]'
        nexusManager.process_data(PipelineType.STREAM, stream_data)

    except PipelineError as e:
        print(e)
