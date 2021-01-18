import pprint
import statistics
from datetime import datetime


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
        results = {}
        for tag, measurements in Stopwatch.measurements.items():
            results[tag] = Stopwatch._compute_statistics(measurements)
        return results

    @staticmethod
    def print_report():
        printer = pprint.PrettyPrinter(indent=2)
        items = Stopwatch.get_results().items()
        if len(items) == 0:
            print("ERROR: no test results. Please check the database connection.")
        for tag, results in items:
            print(f"\n{tag}")
            printer.pprint(results)

    @staticmethod
    def _compute_statistics(measurements):
        percentiles = statistics.quantiles(measurements, n=100)
        return {
            "count": len(measurements),
            "mean": statistics.mean(measurements),
            "median": statistics.median(measurements),
            "min": min(measurements),
            "max": max(measurements),
            "p90": percentiles[89],
            "p95": percentiles[94],
            "p99": percentiles[98]
        }

