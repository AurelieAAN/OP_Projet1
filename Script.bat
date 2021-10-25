@echo off
set currentpath=%~dp0
cmd /k "cd /d currentpath & cd /d env\Scripts & activate & cd /d %cd%"