@echo off
set original_dir="%CD%"
cd "C:\Program Files\security-tools\hashcat-5.1.0"
hashcat64.exe %*
cd "%original_dir%"
REM for /f "tokens=1 delims=\\" %%G IN ("%original_dir%") DO %%G
