import pandas
import numpy
import matplotlib.pyplot as pyplot
import requests
import importlib.metadata


def simulate_loading() -> None:
    """
    To download using pip you have to use: pip install -r requirements.txt

    To install using poetry use: poetry install
    After that run a program using: poetry run python3 loading.py
    """

    print("LOADING STATUS: Loading programs...\n")

    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }

    print("Checking dependencies:")
    for pkg, description in packages.items():
        try:
            version = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({version}) - {description}")

        except importlib.metadata.PackageNotFoundError:
            print(f"[ERROR] {pkg} is NOT installed!")

    """Generating 100 rows x 3 columns with random numbers"""
    raw_data = numpy.random.rand(100, 3)

    data_frame = pandas.DataFrame(
        raw_data,
        columns=['Speed', 'Stability', 'Security']
    )
    data_frame['Total_Score'] = (
        data_frame['Speed'] * 0.4 +
        data_frame['Stability'] * 0.3 +
        data_frame['Security'] * 0.3
    )

    """It shows only 5 first rows"""
    print("\n[PANDAS] Table:")
    print(data_frame.head())
    print()

    """Just a connection test"""
    try:
        """Downloading only requests headers"""
        r = requests.head("https://pypi.org", timeout=3)
        print(f"Server response: {r.status_code}")

    except Exception as e:
        print(f"Lack of connection: {e}")

    print("Show the pyplot:")
    pyplot.figure(figsize=(10, 6))
    pyplot.plot(data_frame["Total_Score"])
    pyplot.xlabel("Count")
    pyplot.ylabel("Total Score")

    pyplot.show()

    print("Analysis complete!")


if __name__ == "__main__":
    simulate_loading()
