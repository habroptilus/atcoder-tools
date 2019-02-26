"""出力した結果と正解の比較を行う."""
import logging as lg


class Tester:
    def __init__(self):
        return

    def run(self, outputs, answers):
        corrects = 0
        if len(outputs) != len(answers):
            raise Exception("The numbers of Outputs and answers don't match.")
        for i in range(len(outputs)):
            if outputs[i] == answers[i]:
                corrects += 1
                lg.info(f"[{i+1}/{len(outputs)}] Passed.")
            else:
                lg.info(f"[{i+1}/{len(outputs)}] Failed.")
        lg.info(f"{corrects}/{len(outputs)} samples are passed.")
        return True if corrects == len(outputs) else False
