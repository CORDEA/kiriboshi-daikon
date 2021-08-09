import rumps

TIMER_INTERVAL_TYPE = [
    15,
    20,
    25,
]


class App(rumps.App):
    def __init__(self):
        super(App, self).__init__("Kiriboshi Daikon")
        interval = TIMER_INTERVAL_TYPE[0]
        self.menu = [rumps.MenuItem("{} minutes".format(interval), self._interval_menu_callback), "Start timer",
                     "Stop timer"]
        self.timer = rumps.Timer(self._timer_callback, interval * 60)

    def _timer_callback(self, sender):
        print(sender)

    def _interval_menu_callback(self, sender):
        index = TIMER_INTERVAL_TYPE.index(self.timer.interval / 60)
        interval = TIMER_INTERVAL_TYPE[0 if index >= len(TIMER_INTERVAL_TYPE) - 1 else index + 1]
        self.timer.interval = interval * 60
        sender.title = '{} minutes'.format(interval)

    @rumps.clicked("Start timer")
    def start_timer(self, _):
        print(self.timer)
        self.timer.start()

    @rumps.clicked("Stop timer")
    def stop_timer(self, _):
        self.timer.stop()


def main():
    App().run()


if __name__ == "__main__":
    main()
