"""mainスクリプト."""
from lib import CodeGenerateTask, SubmitTask, TestTask
from args import get_args
import argparse
import logging as lg
from config import USERNAME, PASSWORD
import luigi

# set args
parser = argparse.ArgumentParser(
    description='For execution main')
get_args(parser)
args = parser.parse_args()

if args.verbose:
    lg.getLogger().setLevel(lg.INFO)
    lg.info("Verbose mode activated")

luigi.configuration.LuigiConfigParser.add_config_path('lib/tasks/luigi.cfg')

if args.mkdir:
    luigi.build([CodeGenerateTask(lang=args.lang, level=args.level,
                                  rnd=args.rnd, src_dir=args.src_dir)], workers=1, local_scheduler=True)

elif args.submit:
    luigi.build([SubmitTask(lang=args.lang, level=args.level, rnd=args.rnd, src_dir=args.src_dir, prob=args.prob,
                            username=USERNAME, password=PASSWORD)], workers=1, local_scheduler=True)
else:
    luigi.build([TestTask(lang=args.lang, level=args.level, rnd=args.rnd, src_dir=args.src_dir, prob=args.prob,
                          username=USERNAME, password=PASSWORD)], workers=1, local_scheduler=True)
