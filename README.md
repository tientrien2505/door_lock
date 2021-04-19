# Door Lock Module
## Usage

 - clone code:

> `git clone https://github.com/tientrien2505/door_lock.git`

 - config .env file:

> BUTTON_PIN=11 # pin connected to push button
> 
> BOLT_PIN=15 # pin connected to lock bolt
>
> DURATION_PRESS_OF_BUTTON=40 # an integer bounctime in milliseconds
> 
> LOG_FILE_PATH=./log.log # log file path
- code example:
```python
# import module
from door_lock import DoorLock

# initial door lock system
dl = DoorLock()

# deactivate button
dl.deactivate()

# activate button
dl.activate()

# open door function
dl.open_door()

# keep door opening
dl.keep_door_opening()

# close door
dl.close_door()
```
