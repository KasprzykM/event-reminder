# Event Reminder

Ever forgot important event or someones birthday? Do you spend a lot of time on your computer? Well look no further than my ghetto event reminder!

## Requirements

This was written in python 3.7 so it is required to run it. 
Additionally you need to install [Dateutil](https://dateutil.readthedocs.io/en/stable/)

```
pip install python-dateutil
```

## How it works

Fill in json however you please by given example then simply run the program usying makefile with command
```
make run
```
or when you want to change parameters:
```
make run wait=5 deadline=7
```
* Wait - seconds before it closes.
* Deadline - days before event triggers reminder.

You can also clean any cache files usying makefile though it was written for Windows only:
```
make clean
```

## Okay but whats the point?

Well, as I've said its heavily personalized. I've got into trouble of not remembering someones birthday and I happen to turn on my computer daily. This was made specifically to run at system startup and either disappear before I notice it or remind me of something that I had to know. You can achieve it by simple batch file or adding it to task scheduler - its up to you to decide. 


