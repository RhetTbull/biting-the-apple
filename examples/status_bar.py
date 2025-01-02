"""Simple status bar app using rumps """

import rumps


class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Check button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hello")
    def sayhello(self, _):
        rumps.alert("Hello", "Hello HSV.py!", "Goodbye")


if __name__ == "__main__":
    AwesomeStatusBarApp("Awesome App").run()
