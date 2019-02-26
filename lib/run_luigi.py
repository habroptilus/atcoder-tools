import luigi
from luigi.util import requires


class ScrapeTask(luigi.Task):
    def output(self):
        return luigi.LocalTarget()

    def run(self):


@requires(ScrapeTask)
class ExecuteTask(luigi.Task):
    def output(self):
        return luigi.LocalTarget()

    def run(self):


@requires(ExecuteTask)
class TestTask(luigi.Task):
    def output(self):
        return luigi.LocalTarget()

    def run(self):


@requires(TestTask)
class SubmitTask(luigi.Task):

    def output(self):
        return luigi.LocalTarget()

    def run(self):
