"""Luigi tasks"""
import luigi
from luigi.util import requires
from tools import Scraper, Submitter, Tester
import json
from lang_params import params


class ScrapeTask(luigi.Task):
    level = luigi.Parameter()
    rnd = luigi.IntParameter()
    prob = luigi.Parameter()
    src_dir = luigi.Parameter()
    username = luigi.Parameter()
    password = luigi.Parameter()

    def requires(self):
        return

    def output(self):
        return luigi.LocalTarget(f"{self.src_dir}/{self.level}/{self.rnd}/sample_{self.prob}.json")

    def run(self):
        s = Scraper(self.username, self.password)
        samples = s.scrape(self.level, self.rnd, self.prob)
        with self.output().open("w") as f:
            json.dump(samples, f, indent=4)


@requires(ScrapeTask)
class TestTask(luigi.Task):
    is_done = False
    lang = luigi.Parameter()

    def run(self):
        extension = params[self.lang]["extension"]
        source_path = f"{self.src_dir}/{self.level}/{self.rnd}/code_{self.prob}.{extension}"
        with self.input().open("r") as f:
            samples = json.load(f)
        inputs = [sample["input"] for sample in samples]
        answers = [sample["answer"] for sample in samples]
        executor = params[self.lang]["executor"]
        outputs = executor.run(source_path, inputs)
        tester = Tester()
        all_passed = tester.run(outputs, answers)
        if all_passed:
            self.is_done = True
        else:
            raise Exception("There exists some samples which doesn't pass.")

    def complete(self):
        return self.is_done


@requires(TestTask)
class SubmitTask(luigi.Task):
    is_done = False

    def run(self):
        extension = params[self.lang]["extension"]
        lang_id = params[self.lang]["id"]
        submitter = Submitter(self.username, self.password)
        submitter.submit(self.level, self.rnd, self.prob, extension, lang_id)
        self.is_done = True

    def complete(self):
        return self.is_done


class CodeGenerateTask(luigi.Task):
    is_done = False
    lang = luigi.Parameter()
    level = luigi.Parameter()
    rnd = luigi.IntParameter()
    src_dir = luigi.Parameter()

    def requires(self):
        return

    def run(self):
        generator = params[self.lang]["generator"]
        generator.run(self.src_dir, self.level, self.rnd)
        self.is_done = True

    def complete(self):
        return self.is_done
