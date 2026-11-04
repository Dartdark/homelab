@echo off
title Stopping BucketMedia Homelab
echo Stopping Homelab containers...
docker compose -f "D:\BucketMedia\Homelab\docker-compose.yml" down
echo Homelab stopped.
pause
