import sys
import time
import traceback
import uuid
from itertools import chain, cycle

from PyQt6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    QTime,
    pyqtSignal,
    pyqtSlot
)
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from interface import Ui_MainWindow


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.

    progress: int progress complete, from 0-100
    """
    progress = pyqtSignal(str, int)
    count = pyqtSignal(int)
    help_label = pyqtSignal(str)


class Worker(QRunnable):
    """
    Worker Thread

    Inherites from QRunnable to handle worker thread setup, signals
    and wrap-up.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.job_id = uuid.uuid4().hex
        self.stopped = False

    @pyqtSlot()
    def run(self):
        turns = self.cycle_up_and_down(1, 100)
        for breath in range(self.kwargs["n_breaths"]):
            for _ in range(200):
                self.signals.progress.emit(self.job_id, next(turns))
                self.signals.count.emit(breath + 1)
                self.signals.help_label.emit("Breath")
                time.sleep(2 / 200)
            self.signals.count.emit(0)

        start_time = time.time()
        while not self.stopped:
            time.sleep(1)
            self.signals.help_label.emit("Hold breath")
            self.signals.count.emit(int(time.time() - start_time))

    def stop(self):
        self.stopped = True

    @staticmethod
    def cycle_up_and_down(first, last):
        up = range(first, last + 1, 1)
        down = range(last, first - 1, -1)
        return cycle(chain(up, down))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.lcd.setDigitCount(5)
        self.lcd.display("00:00")
        self.clicked = False

        self.n_breaths = 2

        self.worker = Worker(n_breaths=self.n_breaths)
        self.worker.signals.progress.connect(self.update_progress)
        self.worker.signals.count.connect(self.update_count)
        self.worker.signals.help_label.connect(self.update_help_label)

        self.startBtn.pressed.connect(self.execute if not self.clicked else self.worker.stop)

        # Dictionary holds the progress of current workers.
        self.worker_progress = {}

        self.threadpool = QThreadPool()
        print(
            f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads"
        )

    def execute(self):
        self.clicked = True
        # Execute
        self.threadpool.start(self.worker)

    def update_progress(self, job_id, progress):
        self.worker_progress[job_id] = progress
        self.progressBar.setValue(progress)

    def update_help_label(self, label):
        self.helpLabel.setText(label)

    def update_count(self, count):
        sec = count
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        self.lcd.display(f"{mins:02d}:{sec:02d}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
