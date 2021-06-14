@echo off
echo 1. Uruchom program
echo 2. koniec
:menu
echo Wybierz opcje:
set /p opcja=
 if %opcja% == 1 (goto :uruchom)
 if %opcja% == 2 (goto :koniec)
:uruchom
if exist projekt_pesel.py (
 ECHO Plik istnieje! Zaraz nastapi jego uruchomienie
 timeout /t 3 /nobreak > NUL
 start projekt_pesel.py    
) else (
  ECHO Plik nie istnieje!
)
:koniec
Exit