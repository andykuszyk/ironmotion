from ironmotion.listeners import RecordListener, ListenListener
from ironmotion.sdk import Leap
import pickle
import subprocess
from pynput.keyboard import Key, Controller
import json
import distance as dist


def record(args):
    listener = RecordListener()
    controller = Leap.Controller(listener)
    print 'Recording, perform a gesture aboove your Leap device...'
    while listener.is_recording != False:
        pass
    print 'Recording complete, captured {} frames of motion...'.format(len(listener.translations))
    controller.remove_listener(listener)
    with open(args.gesture_file, 'wb') as file:
        pickle.dump([(t.x, t.y, t.z) for t in listener.translations], file)
    print '...frames saved to {}'.format(args.gesture_file)


def distance(args):
    print 'Please wait, loading gesture file...'
    with open(args.gesture_file, 'rb') as file:
        recorded_translations = pickle.load(file)
    listener = RecordListener()
    controller = Leap.Controller(listener)
    print '...file loaded. Perform a gesture above your Leap device to distance the recording...'
    while listener.is_recording != False:
        pass
    listened_translations = [(t.x, t.y, t.z) for t in listener.translations]

    mse = dist.simple(recorded_translations, listened_translations)

    print 'The MSE is: {}'.format(mse)


class Action:
    def __init__(self, action_value, action_type):
        self._value = action_value
        self._type = action_type

    def invoke(self):
        keyboard = Controller()
        if self._type == 'cmd':
            subprocess.call(self._value.split(' '))
        elif self._type == 'key':
            if ' ' not in self._value:
                keyboard.press(get_key(self._value))
                keyboard.release(get_key(self._value))
            else:
                keys = [get_key(k) for k in self._value.split(' ')]
                for key in keys:
                    keyboard.press(key)
                for key in keys.reverse():
                    keyboard.release(key)
        else:
            raise Exception('Unrecognised action type: {}'.format(self._type))


def listen(args):
    try:
        with open(args.config_file, 'r') as config_file:
            config = json.loads(config_file.read())
    except Exception as e:
        raise Exception('Error reading config file: {}'.format(e))

    if type(config) is not type([]):
        raise Exception('Config file should be a JSON array')

    gestures = []
    for element in config:
        if u'file' not in element or u'name' not in element or u'action' not in element or u'threshold' not in element:
            raise Exception('Malformed element: missing file, name, threshold or action')
        if u'type' not in element['action'] or u'value' not in element['action']:
            raise Exception('Malformed config: action missing type or value')

        gesture = {}
        gestures.append(gesture)
        try:
            with open(str(element[u'file']), 'rb') as file:
                gesture['translations'] = pickle.load(file)
        except Exception as e:
            raise Exception('Error loading gesture file ({}): {}'.format(element['file'], e))

        gesture['name'] = element[u'name']
        gesture['threshold'] = element[u'threshold']
        gesture['action'] = Action(element[u'action'][u'value'], element[u'action'][u'type'])
        
    listener = ListenListener()
    listener.set_gestures(gestures)
    controller = Leap.Controller(listener)
    input('')


def get_key(key):
    if key == 'alt': return Key.alt
    if key == 'alt_gr': return Key.alt_gr
    if key == 'alt_l': return Key.alt_l
    if key == 'alt_r': return Key.alt_r
    if key == 'backspace': return Key.backspace
    if key == 'caps_lock': return Key.caps_lock
    if key == 'cmd': return Key.cmd
    if key == 'cmd_l': return Key.cmd_l
    if key == 'cmd_r': return Key.cmd_r
    if key == 'ctrl': return Key.ctrl
    if key == 'ctrl_l': return Key.ctrl_l
    if key == 'ctrl_r': return Key.ctrl_r
    if key == 'delete': return Key.delete
    if key == 'down': return Key.down
    if key == 'end': return Key.end
    if key == 'enter': return Key.enter
    if key == 'esc': return Key.esc
    if key == 'f1': return Key.f1
    if key == 'home': return Key.home
    if key == 'insert': return Key.insert
    if key == 'left': return Key.left
    if key == 'menu': return Key.menu
    if key == 'num_lock': return Key.num_lock
    if key == 'page_down': return Key.page_down
    if key == 'page_up': return Key.page_up
    if key == 'pause': return Key.pause
    if key == 'print_screen': return Key.print_screen
    if key == 'right': return Key.right
    if key == 'scroll_lock': return Key.scroll_lock
    if key == 'shift': return Key.shift
    if key == 'shift_l': return Key.shift_l
    if key == 'shift_r': return Key.shift_r
    if key == 'space': return Key.space
    if key == 'tab': return Key.tab
    if key == 'up': return Key.up
    return key
