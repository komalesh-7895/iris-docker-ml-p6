import json
import subprocess
import sys
import unittest
from pathlib import Path


class TestIrisQualityGate(unittest.TestCase):

    def setUp(self):
        self.metrics_path = Path("metrics.json")
        self.original_metrics = None

        if self.metrics_path.exists():
            self.original_metrics = self.metrics_path.read_text()

    def tearDown(self):
        if self.original_metrics is not None:
            self.metrics_path.write_text(self.original_metrics)
        elif self.metrics_path.exists():
            self.metrics_path.unlink()

    def run_quality_gate(self, accuracy):
        self.metrics_path.write_text(
            json.dumps({"accuracy": accuracy})
        )

        return subprocess.run(
            [sys.executable, "quality_gate.py"],
            capture_output=True,
            text=True
        )

    def test_high_accuracy_passes(self):
        result = self.run_quality_gate(0.90)
        self.assertEqual(result.returncode, 0)

    def test_low_accuracy_fails(self):
        result = self.run_quality_gate(0.70)
        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
