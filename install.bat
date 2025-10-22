@echo off
echo.
echo ========================================
echo   KeepAlive - Installation Script
echo ========================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo ✅ Installation completed successfully!
    echo.
    echo To run KeepAlive:
    echo   run.bat [delay_in_seconds]
    echo.
    echo Examples:
    echo   run.bat          ^(60 second default^)
    echo   run.bat 30       ^(30 second interval^)
    echo   run.bat 120      ^(2 minute interval^)
    echo.
) else (
    echo.
    echo ❌ Installation failed!
    echo Please make sure Python and pip are installed.
    echo.
)

pause
