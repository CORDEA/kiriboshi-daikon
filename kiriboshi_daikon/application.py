import rumps


class App(rumps.App):
    def __init__(self):
        super(App, self).__init__("Kiriboshi Daikon")
        self.menu = ["Start timer", "Stop timer"]
        self.timer = rumps.Timer(self._timer_callback, 3)

    def _timer_callback(self, sender):
        print(sender)

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
