@echo off
:: DevOps Portfolio - GitHub Pages Deployment Script for Windows
:: This script helps you deploy your portfolio website to GitHub Pages

echo.
echo 🚀 DevOps Portfolio Deployment Script (Windows)
echo ===============================================
echo.

:: Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed. Please install Git first.
    pause
    exit /b 1
)

:: Check if we're in a git repository
if not exist ".git" (
    echo [STEP] Initializing Git repository...
    git init
    echo [INFO] Git repository initialized
) else (
    echo [INFO] Git repository already exists
)

:: Check if required files exist
set "missing_files="
if not exist "index.html" set "missing_files=%missing_files% index.html"
if not exist "style.css" set "missing_files=%missing_files% style.css"
if not exist "script.js" set "missing_files=%missing_files% script.js"

if not "%missing_files%"=="" (
    echo [ERROR] Missing required files:%missing_files%
    echo [ERROR] Please ensure all files are in the current directory
    pause
    exit /b 1
)

echo [INFO] All required files found

:: Get repository information
echo.
echo [STEP] Repository Configuration
echo Please provide your GitHub repository information:
echo.

set /p github_username="Enter your GitHub username: "
set /p repo_name="Enter your repository name (e.g., 'portfolio' or '%github_username%.github.io'): "

:: Validate inputs
if "%github_username%"=="" (
    echo [ERROR] Username is required
    pause
    exit /b 1
)

if "%repo_name%"=="" (
    echo [ERROR] Repository name is required
    pause
    exit /b 1
)

:: Set up remote origin
set "repo_url=https://github.com/%github_username%/%repo_name%.git"
echo [INFO] Repository URL: %repo_url%

:: Check if remote origin exists and set it
git remote get-url origin >nul 2>&1
if %errorlevel% equ 0 (
    echo [WARNING] Remote origin already exists. Updating...
    git remote set-url origin "%repo_url%"
) else (
    echo [INFO] Adding remote origin...
    git remote add origin "%repo_url%"
)

:: Add all files to staging
echo [STEP] Preparing files for deployment...
git add .

:: Check if there are changes to commit
git diff --cached --quiet >nul 2>&1
if %errorlevel% neq 0 (
    :: Commit changes
    set "commit_message=Deploy portfolio website - %date% %time%"
    echo [INFO] Committing changes: %commit_message%
    git commit -m "%commit_message%"
) else (
    echo [WARNING] No changes to commit
)

:: Push to GitHub
echo [STEP] Deploying to GitHub...
echo [INFO] Pushing to main branch...

git push -u origin main
if %errorlevel% equ 0 (
    echo [INFO] Successfully pushed to GitHub!
) else (
    echo [ERROR] Failed to push to GitHub. Please check your credentials and repository permissions.
    pause
    exit /b 1
)

:: Instructions for enabling GitHub Pages
echo.
echo [STEP] Enable GitHub Pages
echo To complete the deployment, follow these steps:
echo 1. Go to https://github.com/%github_username%/%repo_name%/settings/pages
echo 2. Under 'Source', select 'Deploy from a branch'
echo 3. Choose 'main' branch and '/ (root)' folder
echo 4. Click 'Save'
echo.
echo Your website will be available at:
if "%repo_name%"=="%github_username%.github.io" (
    echo 🌐 https://%github_username%.github.io
) else (
    echo 🌐 https://%github_username%.github.io/%repo_name%
)

echo.
echo [INFO] Deployment completed successfully! 🎉
echo [INFO] It may take a few minutes for GitHub Pages to build and deploy your site.

:: Optional: Open GitHub Pages settings
echo.
set /p open_browser="Would you like to open GitHub Pages settings in your browser? (y/n): "
if /i "%open_browser%"=="y" (
    start https://github.com/%github_username%/%repo_name%/settings/pages
)

echo.
echo 🚀 Happy coding and best of luck with your DevOps career!
echo.
pause
