import unittest
import sys
from io import StringIO
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        """Runs before each test — creates a fresh TaskPool."""
        self.pool = TaskPool()

    def test_add_task(self):
        """Tests that add_task() correctly adds a Task to the pool."""
        task = Task("New feature implementation")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        """Tests that get_open_tasks() returns only 'ToDo' tasks."""
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        open_titles = [t.title for t in open_tasks]
        self.assertIn("Implement login feature", open_titles)
        self.assertIn("Deploy to staging", open_titles)
        self.assertIn("Code review", open_titles)
        self.assertNotIn("Design database schema", open_titles)

    def test_get_done_tasks(self):
        """Tests that get_done_tasks() returns only 'Done' tasks."""
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        done_titles = [t.title for t in done_tasks]
        self.assertIn("Design database schema", done_titles)
        self.assertIn("Set up CI/CD pipeline", done_titles)
        self.assertIn("Write unit tests", done_titles)
        self.assertNotIn("Implement login feature", done_titles)


if __name__ == "__main__":
    # Load and run tests with cleaner output
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTaskPool)

    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)

    output = stream.getvalue()
    lines = output.splitlines()

    for line in lines:
        if "... ok" in line or "... FAIL" in line or "... ERROR" in line:
            test_name = line.split(" (")[0].strip()
            status = "ok" if "ok" in line else ("FAIL" if "FAIL" in line else "ERROR")
            print(f"{test_name} ... {status}")

    if result.wasSuccessful():
        print("\nAll tests passed!")
    else:
        print(f"\n{len(result.failures)} test(s) failed.")
        sys.exit(1)
