@echo off
REM Docker run script for Windows

setlocal enabledelayedexpansion

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not installed. Please install Docker Desktop first.
    exit /b 1
)

REM Default action
set ACTION=%1
if "%ACTION%"=="" set ACTION=build-and-run

if "%ACTION%"=="build" (
    echo [INFO] Building OCS Docker image...
    docker build -t ocs-landing-page-builder .
    echo [INFO] Build complete!
) else if "%ACTION%"=="run" (
    echo [INFO] Running OCS container...
    docker run -it --rm ^
        --name ocs-app ^
        -v "%CD%\outputs:/app/outputs" ^
        -v "%CD%\logs:/app/logs" ^
        -e GEMINI_API_KEY=%GEMINI_API_KEY% ^
        ocs-landing-page-builder
) else if "%ACTION%"=="build-and-run" (
    echo [INFO] Building and running OCS...
    docker build -t ocs-landing-page-builder .
    docker run -it --rm ^
        --name ocs-app ^
        -v "%CD%\outputs:/app/outputs" ^
        -v "%CD%\logs:/app/logs" ^
        -e GEMINI_API_KEY=%GEMINI_API_KEY% ^
        ocs-landing-page-builder
) else if "%ACTION%"=="compose-up" (
    echo [INFO] Starting services with Docker Compose...
    if not exist .env (
        echo [WARNING] No .env file found. Creating one from .env.example...
        copy .env.example .env
    )
    docker-compose up -d
    echo [INFO] Services started! Check 'docker-compose logs' for output.
) else if "%ACTION%"=="compose-down" (
    echo [INFO] Stopping Docker Compose services...
    docker-compose down
) else if "%ACTION%"=="compose-logs" (
    echo [INFO] Showing Docker Compose logs...
    docker-compose logs -f
) else if "%ACTION%"=="shell" (
    echo [INFO] Opening shell in OCS container...
    docker run -it --rm ^
        --name ocs-shell ^
        -v "%CD%\outputs:/app/outputs" ^
        -v "%CD%\logs:/app/logs" ^
        -e GEMINI_API_KEY=%GEMINI_API_KEY% ^
        ocs-landing-page-builder /bin/bash
) else if "%ACTION%"=="clean" (
    echo [INFO] Cleaning up Docker resources...
    docker system prune -f
    echo [INFO] Cleanup complete!
) else (
    echo OCS Docker Management Script
    echo.
    echo Usage: %0 [ACTION]
    echo.
    echo Actions:
    echo   build          - Build Docker image only
    echo   run            - Run container with current directory mounted
    echo   build-and-run  - Build and run ^(default^)
    echo   compose-up     - Start with Docker Compose
    echo   compose-down   - Stop Docker Compose services
    echo   compose-logs   - Show Docker Compose logs
    echo   shell          - Open shell in container
    echo   clean          - Clean up Docker resources
    echo   help           - Show this help
    echo.
    echo Environment Variables:
    echo   GEMINI_API_KEY - Your Gemini AI API key
    echo.
    echo Examples:
    echo   %0 build
    echo   set GEMINI_API_KEY=your-key ^&^& %0 run
    echo   %0 compose-up
)