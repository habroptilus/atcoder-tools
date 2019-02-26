"""mainスクリプト."""
from tools import execute_main
from args import get_args
import argparse
import logging as lg
from config import USERNAME, PASSWORD

# set args
parser = argparse.ArgumentParser(
    description='For execution main')
get_args(parser)
args = parser.parse_args()

if args.verbose:
    lg.getLogger().setLevel(lg.INFO)
    lg.info("Verbose mode activated")

params = vars(args)
del params["verbose"]
execute_main(**params, data_dir=data_dir, real_data_filebases=real_data_filebases,
             experiment_flag_to_models=experiment_flag_to_models, result_dir=result_dir)
