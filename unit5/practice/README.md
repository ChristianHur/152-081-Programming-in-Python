## Description

Write a function **getTimeName(hours, minutes, period)** that returns the English name for a point in time.  If the minutes are exactly 15, 30, or 45, then it should read `a quarter after ...`, `half past ...`, or `a quarter to ...` respectively.  If the minutes is 0 then it should read `... o'clock`.  Assume that hours is between 1 and 12.

Examples:
```python
getTimeName(8,0,AM)                # 8 o'clock am
getTimeName(8,15,PM)               # a quarter after 8 pm
getTimeName(8,30,AM)               # half past 8 am
getTimeName(8,45,PM)               # a quater to 9 am
getTimeName(8,12,AM)               # 12 minutes past 8 am
```

### Version Information
Two versions showing different implemenations.
|File|Description|
|---|---|
|timename1.py|Using minutes as a string and word constants for minutes
|timename2.py|Using minutes as integer and lists to store word constants for minutes
