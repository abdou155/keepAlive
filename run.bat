@echo off
if "%1"=="" (
    python keepalive.py
) else (
    python keepalive.py %1
)
