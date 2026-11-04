@echo off
title Starting BucketMedia Homelab
echo ========================================================
echo        Starting BucketMedia Master Homelab Stack        
echo ========================================================
docker compose -f "D:\BucketMedia\Homelab\docker-compose.yml" up -d
echo.
echo [OK] Homelab Services are Live!
echo.
echo   Master Dashboard    : http://localhost:7575
echo   Navidrome (Music)   : http://localhost:4533
echo   EmulatorJS (Arcade) : http://localhost:4000
echo   Kiwix (Knowledge)   : http://localhost:8085
echo   Kavita (Manga/Books): http://localhost:5000
echo   Audiobookshelf      : http://localhost:13378
echo   Jellyfin (Movies/TV): http://localhost:8096
echo   Sunshine Streaming  : https://localhost:47990
echo.
echo Access on any device on your Wi-Fi at: http://192.168.1.70:7575
echo ========================================================
pause
