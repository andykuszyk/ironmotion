import argparse
from ironmotion import commands


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    record_parser = subparsers.add_parser('record', help='Used to record a gesture to a file.')
    record_parser.add_argument('gesture_file', help='The path of the file to save the recorded gesture to.')
    record_parser.set_defaults(func=commands.record)

    distance_parser = subparsers.add_parser('distance', help='Used to evaluate the error between an existing recording with a new gesture.')
    distance_parser.add_argument('gesture_file', help='The path to a pre-recorded gesture file.')
    distance_parser.set_defaults(func=commands.distance)

    listen_parser = subparsers.add_parser('listen', help='Listens for gestures and tries to match them against those described in the config file.')
    listen_parser.add_argument('config_file', help='The path to the gesture config file.')
    listen_parser.set_defaults(func=commands.listen)

    args = parser.parse_args()
    args.func(args)
