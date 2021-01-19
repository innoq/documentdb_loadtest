import pprint
import statistics
from datetime import datetime

from config import DURATION, N_THREADS


class Stopwatch:
    measurements = {}

    def __init__(self):
        self.start = datetime.now()

    def measure(self, tag):
        dt = datetime.now() - self.start
        if tag in Stopwatch.measurements:
            Stopwatch.measurements[tag].append(round(dt.microseconds/1000))
        else:
            Stopwatch.measurements[tag] = [round(dt.microseconds/1000)]

    @staticmethod
    def get_results():
        results = []
        for tag, measurements in Stopwatch.measurements.items():
            percentiles = statistics.quantiles(measurements, n=100)
            results.append({
                "tag": tag,
                "count": len(measurements),
                "mean": statistics.mean(measurements),
                "median": statistics.median(measurements),
                "min": min(measurements),
                "max": max(measurements),
                "p90": percentiles[89],
                "p95": percentiles[94],
                "p99": percentiles[98]
            })
        return {
            "N_THREADS": N_THREADS,
            "DURATION": DURATION,
            "RESULTS": results,
        }

    @staticmethod
    def save_report(file_name):
        with open(file_name, "w") as f:
            f.write(Stopwatch.get_report())


    @staticmethod
    def print_report():
        print(Stopwatch.get_formatted_report())

    @staticmethod
    def get_formatted_report():
        result_data = Stopwatch.get_results()
        f = f"DATE: {datetime.now().isoformat()}\nN_THREADS: {N_THREADS}\nDURATION: {DURATION}s\n\n"
        for result in result_data["RESULTS"]:
            f += f"\n*** {result['tag']} ***\n"
            for [key, val] in result.items():
                if key != "tag":
                    f += f"\t{key}: {str(val)}\n"
        return f


    @staticmethod
    def get_report():
        printer = pprint.PrettyPrinter(indent=2)
        results = Stopwatch.get_results()
        if len(results) == 0:
            print("ERROR: no test results. Please check the database connection.")
        return printer.pformat(results)

