#!/usr/bin/python
'''
@author F.Paskali
'''
import time, datetime, argparse, os

def timer(timer_type, minutes, finish_line):
    seconds = datetime.timedelta(minutes=minutes).seconds
    if input(f"Start {timer_type}?[y/n]") == "n":
        return False
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        while seconds >= 0:
            print(f"\r{timer_type}: {datetime.timedelta(seconds=seconds)}", end='')
            seconds -= 1
            time.sleep(1)
        print(f"\r{finish_line}\a")
        return True

def pomodoro(work, short, long, repeats):
    while True:
        for i in range(1, repeats+1):
            if not timer(f'Pomodoro {i}', work, f'Pomodoro {i} DONE! {repeats-i} to go...'): return "Exit"
            if i < repeats:
                if not timer('Short break', short, 'Time for work'): return "Exit"
            else:
                if not timer('Long break', long, 'Time for work'): return "Exit"

def main():
    parser = argparse.ArgumentParser(description='Simple Pomodoro.')
    parser.add_argument("-pomodoro", type=int, help="Duration of working period in minutes. (default=25)", default=25)
    parser.add_argument("-short", type=int, help="Duration of short break in minutes. (default=5)", default=5)
    parser.add_argument("-long", type=int, help="Duration of long break in minutes. (default=15)", default=15)
    parser.add_argument("-repeats", type=int, help="Number of working periodes, before long break. (default=4)", default=4)

    args = parser.parse_args()

    pomodoro(args.pomodoro, args.short, args.long, args.repeats)

if __name__ == "__main__":
    main()
