from ironmotion.sdk import Leap

class RecordListener(Leap.Listener):
    def on_init(self, controller):
        self.is_recording = None
        self._last_frame = None
        self.translations = []

    def on_frame(self, controller):
        frame = controller.frame()
        if self._last_frame is None:
            self._last_frame = frame
            return

        translation = frame.translation(self._last_frame)
        if self.is_recording is None and (translation.x != 0 or translation.y != 0 or translation.z != 0):
            self.is_recording = True

        if self.is_recording:
            if translation.x == 0 and translation.y == 0 and translation.z == 0:
                self.is_recording = False
            else:
                self.translations.append(translation)

        self._last_frame = frame


