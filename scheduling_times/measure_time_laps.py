"""
.. module:: scheduling_times.measure_time_laps
   :synopsis: Use time module effectively
"""
import time

from loguru import logger


def track_lap_time():
    logger.info("Enter any character to continue with lap counter. CTRL + C for exit.")
    try:
        start_time = time.time()
        lap_num = 0
        while True:
            input()
            lap_num += 1
            logger.debug(f"Lap {lap_num}: {round(time.time() - start_time, 2)}")
    except KeyboardInterrupt:
        logger.exception("Goodbye ! ")


if __name__ == "__main__":
    track_lap_time()
