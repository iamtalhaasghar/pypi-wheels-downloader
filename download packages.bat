@echo collecting packages listed in links.txt
for /f "tokens=* delims= " %%i in (links.txt) do start %%i
pause