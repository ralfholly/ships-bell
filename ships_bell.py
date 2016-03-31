#!/usr/bin/env python3

import time
import threading
import subprocess

MP3_PLAYER_CALL = "mpg321 -q -g 10 {mp3_file}"

class ShipsBell(threading.Thread):
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HALF_HOUR = 30
    MAX_DOUBLE_STRIKES = 4

    def __init__(self, start=0, end=24):
        super().__init__()
        assert end >= start
        self.start_time = start
        self.end_time = end

    def run(self):
        while True:
            current_time = time.localtime()
            minutes = current_time.tm_min
            hours = current_time.tm_hour
            self.step(hours, minutes)
            time.sleep(self.compute_sleep_time(minutes))

    def step(self, hours, minutes):
        if (hours >= self.start_time and hours < self.end_time) or (hours == self.end_time and minutes == 0):
            # Strike bell at every half or full hour.
            if (minutes % ShipsBell.MINUTES_PER_HALF_HOUR) == 0:
                double_strikes, single_strikes = self.compute_strikes(hours, minutes)
                for _ in range(double_strikes):
                    self.play_double_strike()
                for _ in range(single_strikes):
                    self.play_single_strike()

    @staticmethod
    def compute_strikes(hours, minutes):
        # Single strike only on half hour.
        single_strikes = 1 if minutes == ShipsBell.MINUTES_PER_HALF_HOUR else 0
        double_strikes = hours % ShipsBell.MAX_DOUBLE_STRIKES
        if double_strikes == 0 and single_strikes == 0:
            double_strikes = ShipsBell.MAX_DOUBLE_STRIKES
        return (double_strikes, single_strikes)

    @staticmethod
    def compute_sleep_time(minutes):
        # Remaining minutes till half or full hour.
        delta_minutes = ShipsBell.MINUTES_PER_HALF_HOUR - minutes % ShipsBell.MINUTES_PER_HALF_HOUR
        # If enough time is left, sleep through half of it.
        if delta_minutes >= 2:
            return delta_minutes / 2.0 * ShipsBell.SECONDS_PER_MINUTE
        # During the last minute, check every second.
        return 1.0

    @staticmethod
    def play_double_strike():
        ShipsBell.play_mp3("res/DoubleStrike.mp3")

    @staticmethod
    def play_single_strike():
        ShipsBell.play_mp3("res/SingleStrike.mp3")

    @staticmethod
    def play_mp3(path):
        cmd = MP3_PLAYER_CALL.format(mp3_file=path).split()
        subprocess.call(cmd)

if __name__ == "__main__":
    SHIP_BELL = ShipsBell()
    SHIP_BELL.start()
    SHIP_BELL.join()
