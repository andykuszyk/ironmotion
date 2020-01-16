# ironmotion
A command line tool for recording, recognizing and (eventually, perhaps) invoking actions based on Leap Motion gestures.

## Pre-requisites
* Clone this repo;
* Go to [the Leap Motion website](https://developer.leapmotion.com/setup/desktop) and install the V2 desktop app for Linux;
* Make sure the Leap Motion system daemon is running, `sudo leapd`;
* `pip install -r requirements.txt`

> `ironmotion` is a Python 2 application, so be sure to run it in an appropriate environment. Note that it also only runs under Linux at present.

## Usage
## TL;DR
* `sudo leapd`;
* `make shell` - uses `pipenv` to start a Python 2 shell;
* `make listen` - listens for the sample gestures in `./sample`.

### Recording gestures
Record a gesture with:

```
python2 ironmotion.py record [output-file-name]
```

> For example: `python2 ironmotion.py record swipe-right.gest` would record the gesture you perform to the file `swipe-right.gest`.

### Evaluating the similarity of performed gestures
To evaluate the "distance" between a gesture you perform and a pre-recorded one, run:

```
python2 ironmotion.py distance [input-file-name]
```

> For example, `python2 ironmotion.py distance swipe-right.gest` would calculate the similarity of the gesture you perform to the pre-recorded gesture at `swipe-right.gest`

### Listening for new gestures
Listen for new gestures to be performed and matched against pre-recorded gestures with:

```
python2 ironmotion.py listen [gesture-config-file]
```

Where `gesture-config-file` is the filepath to a JSON config file similar to the example below:

```
[
    {
        "file": "swipe-up.gest",
        "name": "Swipe Up",
        "threshold": 300,
        "action": {
            "type": "key",
            "value": "page_down"
        }
    },
    {
        "file": "swipe-down.gest",
        "name": "Swipe Down",
        "threshold": 300,
        "action": {
            "type": "key",
            "value": "page_up"
        }
    }
]
```

> The `action` `type` can be either `key` or `cmd`. `cmd` should have a `value` which is a shell command to execute, whereas `key` should have a `value` which is a key from the keyboard, or a special key. A list of valid special key values can be seen [here](https://github.com/andykuszyk/ironmotion/blob/669a92d76f03f15def0ca8a2c1514c68457dc1a1/ironmotion/commands.py#L116) in the `get_keys()` function.

## General Idea
The general idea for this tool is to come up with an effective means of comparing performed gestures to pre-recorded ones, and allow actions (e.g. command executions) to be configured against pre-recorded gestures.
