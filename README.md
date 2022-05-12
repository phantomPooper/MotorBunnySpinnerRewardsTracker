# MotorBunnySpinnerRewardsTracker
A simple proof-of-concept script which can record MotorBunny Rewards from a spinner *solely to run statistical analysis on*. . I denounce any responsibilty for misuse of the system, nor do I advise running it.

## Dependencies
This project requires [Python 3](https://www.python.org/downloads/) installed as well as [GeckoDriver](https://github.com/mozilla/geckodriver/releases) installed and setup. It also requires an adjustment to the `LOOP_COUNT` and `FULLY_QUALIFIED_FILE_PATH` variable values on lines 17 and 19 of main.py. The `PHONE_NUMBER` value on line 21 can also be changed. As it is, it would use a random 10 digit string, but this can fail often due to validation. In theory, changing it to a valid phone number will lessen a run time.

## Example Stats:

A file like [motorbunny_codes.txt](Resources/motorbunny_codes.txt) would be generated. This information could then be used to generate charts for statistical analysis, like so:

<img src="Resources/MotorBunny.png"/>
