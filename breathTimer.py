#!env/bin/python
"""
breathTimer: is a breath session timer.

- [X] tqdm progress bar for breathing and breath out
- [X] counter for cycles
- [X] way to changes number of cycles
- [X] timer after cycles with stop
"""
import argparse
import sys
import time
import os

from itertools import chain, cycle
from tqdm import tqdm
from threading import Thread


def get_args():
    my_parser = argparse.ArgumentParser(description="Breathing session timer")
    my_parser.add_argument(
        "-s",
        "--speed",
        action="store",
        default=3,
        help="Speed of timer, default if 3 seconds"
    )
    my_parser.add_argument(
        "-b",
        "--n-breaths",
        action="store",
        default=35,
        help="N breaths per cycle. default is 35"
    )
    my_parser.add_argument(
        "-c",
        "--n-cycles",
        action="store",
        default=4,
        help="N cycles. default is 4"
    )
    my_parser.add_argument(
        "-t",
        "--hold-time",
        action="store",
        default=17,
        help="Hold time after breath round. default is 17"
    )
    my_parser.add_argument(
        "--pbar-size",
        action="store",
        default=100,
        help="Progress bar size. Default is 100"
    )
    args = my_parser.parse_args()
    return args


class Timer:
    def __init__(self, speed, breath_count, cycle_count, hold_time, pbar_size):
        self.stats_list = []
        self.answer = False
        self.speed = int(speed)
        self.breath_count = int(breath_count)
        self.cycle_count = int(cycle_count)
        self.hold_time = int(hold_time)
        self.pbar_size = int(pbar_size)

    def start(self):
        self.breath_cycle()
        self.print_stats()

    def breath_cycle(self):
        for i in range(1, self.cycle_count + 1):
            self.answer = False
            self.breath_round(rnd=i)
            self.hold_breath()
            self.inhale_and_hold()

    def hold_breath(self):

        def time_convert(sec):
            mins = sec // 60
            sec = sec % 60
            hours = mins // 60
            mins = mins % 60
            msg = f"Time Lapsed = min {mins:0.0f} sec {sec:0.0f}"
            self.stats_list.append(msg)
            print(msg)

        def get_input():
            os.system('clear')
            while not self.answer:
                time.sleep(1)
                sys.stdout.write("\r")
                t = int(time.time() - start_time)
                sys.stdout.write("{:2d} seconds.".format(t))
                if t % 60 == 0:
                    # os.system("play -q /System/Library/Sounds/Submarine.aiff")
                    os.system(f'say "{t // 60} minute{"s" if (t // 60) > 1 else ""}. Keep going."')
                sys.stdout.flush()
            return False

        start_time = time.time()
        input_thread = Thread(target=get_input)
        input_thread.start()
        input("Press Enter to stop")
        self.answer = True

        end_time = time.time()
        time_lapsed = end_time - start_time
        time_convert(time_lapsed)

    def breath_round(self, rnd):
        turns = self.cycle_up_and_down(1, 100)
        for bcnt in range(1, self.breath_count + 1):
            self.do_tqdm(bcnt, turns, rnd)

    def do_tqdm(self, bcnt, turns, rnd):
        with tqdm(total=100, bar_format=f"Round {rnd} - Breath {bcnt}: {{bar:{self.pbar_size}}}", position=0, leave=False) as pbar:
            for n in range(200):
                time.sleep(self.speed / 200)
                pbar.n = next(turns)
                pbar.refresh()

    def inhale_and_hold(self):
        print('INHALE AND HOLD!')
        for remaining in range(self.hold_time, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        os.system('clear')

    @staticmethod
    def cycle_up_and_down(first, last):
        up = range(first, last + 1, 1)
        down = range(last, first - 1, -1)
        return cycle(chain(up, down))

    def print_stats(self):
        os.system('clear')
        print("="*80)
        print("ROUND STATS")
        print("=" * 80)
        for i, x in enumerate(self.stats_list):
            print(f"Round {i+1}: {x}")


def main():
    args = get_args()
    timer = Timer(
        speed=args.speed,
        breath_count=args.n_breaths,
        cycle_count=args.n_cycles,
        hold_time=args.hold_time,
        pbar_size=args.pbar_size,
    )
    timer.start()


if __name__ == "__main__":
    main()
