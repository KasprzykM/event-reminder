@echo off
set WAIT_TIME=%1
set DEADLINE=%2
@echo on
python main.py "../test_data/test_data.json" %WAIT_TIME% %DEADLINE%