from datetime import timedelta

import rumps

TIMER_INTERVAL_TYPE = [
    15,
    20,
    25,
]


class App(rumps.App):
    def __init__(self):
        super(App, self).__init__("Kiriboshi Daikon")
        self.interval = TIMER_INTERVAL_TYPE[0]
        self.time_left = 0
        self.menu = [rumps.MenuItem("{} minutes".format(self.interval), self._interval_menu_callback), "Start timer",
                     "Stop timer"]
        self.timer = rumps.Timer(self._timer_callback, 1)

    def _timer_callback(self, sender):
        if not sender.is_alive:
            return
        self.time_left -= 1
        if self.time_left <= 0:
            self.title = "Kiriboshi Daikon"
            self.timer.stop()

        self.title = str(timedelta(seconds=self.time_left))

    def _interval_menu_callback(self, sender):
        index = TIMER_INTERVAL_TYPE.index(self.interval)
        self.interval = TIMER_INTERVAL_TYPE[0 if index >= len(TIMER_INTERVAL_TYPE) - 1 else index + 1]
        sender.title = "{} minutes".format(self.interval)
        self.title = "Kiriboshi Daikon"
        self.timer.stop()

    @rumps.clicked("Start timer")
    def start_timer(self, _):
        self.time_left = self.interval * 60
        self.timer.start()

    @rumps.clicked("Stop timer")
    def stop_timer(self, _):
        self.title = "Kiriboshi Daikon"
        self.timer.stop()


def main():
    App().run()


if __name__ == "__main__":
    main()
