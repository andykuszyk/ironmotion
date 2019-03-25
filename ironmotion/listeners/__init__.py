from ironmotion.sdk import Leap
from ironmotion import distance


class RecordListener(Leap.Listener):
    """
    Waits for a gesture to start and then records its frames.
    """
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


class ListenListener(Leap.Listener):
    """
    Waits for a gesture to start and then, upon it finishing, compares
    it to the list of gestures provided by `set_gestures()` and invokes the
    action of any that match.
    """
    def set_gestures(self, gestures):
        self.gestures = gestures

    def on_init(self, controller):
        self._last_frame = None
        self._is_listening = False
        self._translations = []

    def on_frame(self, controller):
        frame = controller.frame()
        if self._last_frame is None:
            self._last_frame = frame
            return

        translation = frame.translation(self._last_frame)
        if not self._is_listening and (translation.x != 0 or translation.y != 0 or translation.z != 0):
            self._is_listening = True

        if self._is_listening:
            if translation.x == 0 and translation.y == 0 and translation.z == 0:
                self._is_listening = False
                for gesture in self.gestures:
                    mse = distance.simple(gesture['translations'], [(t.x, t.y, t.z) for t in self._translations])
                    if mse < gesture['threshold']:
                        print 'Found match for gesture [{}], invoking action!'.format(gesture['name'])
                        gesture['action'].invoke()
                    else:
                        print 'MSE for gesture [{}] was {}, but threshold was {}, so not invoking action'.format(
                            mse, gesture['name'], gesture['threshold'])
                self._translations = []
            else:
                self._translations.append(translation)

        self._last_frame = frame
