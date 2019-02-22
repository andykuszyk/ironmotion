# ironmotion
A command line tool for recording, recognizing and (eventually, perhaps) invoking actions based on Leap Motion gestures.

## Pre-requisites
* Clone this repo;
* Make sure the Leap Motion system daemon is running, `sudo leapd`;
* `pip install -r requirements.txt`

> `ironmotion` is a Python 2 application, so be sure to run it in an appropriate environment.

## Usage
### Recording gestures
Record a gesture with:

```
./im record [output-file-name]
```

> For example: `./im record swipe-right.gest` would record the gesture you perform to the file `swipe-right.gest`.

### Evaluating the similarity of performed gestures
To evaluate the "distance" between a gesture you perform and a pre-recorded one, run:

```
./im distance [input-file-name]
```

> For example, `./im distance swipe-right.gest` would calculate the similarity of the gesture you perform to the pre-recorded gesture at `swipe-right.gest`

## General Idea
The general idea for this tool is to come up with an effective means of comparing performed gestures to pre-recorded ones, and allow actions (e.g. command executions) to be configured against pre-recorded gestures.
