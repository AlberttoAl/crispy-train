# push_to_github.ps1
# Usage:
# 1. Edit $RemoteUrl to your GitHub repo HTTPS URL (e.g. https://github.com/YourUsername/socket-scanner-midterm.git)
# 2. Open PowerShell in the project folder (Socket_Scanner)
# 3. Run: .\push_to_github.ps1
# If prompted for credentials, use your GitHub username and a Personal Access Token (PAT) as password when required.

param(
    [string]$RemoteUrl = "https://github.com/AlberttoAl/Ultimate_Socket_Scanner.git",
    [string]$CommitMessage = "Initial Commit: Server, Client, Port Scanner, README, Screenshots"
)

if ($RemoteUrl -eq "notepad .\push_to_github.ps1
") {
    Write-Host "Please edit this script and set the variable \$RemoteUrl to your repository HTTPS URL before running." -ForegroundColor Yellow
    exit 1
}

Write-Host "Starting automated git push..." -ForegroundColor Cyan
# Ensure inside project folder
$pwdPath = Get-Location
Write-Host "Working directory: $pwdPath"

# Configure git user if not set
if (-not (git config --global user.name)) {
    git config --global user.name "Your Name"
    Write-Host "Set global git user.name (replace with your name)"
} else {
    Write-Host "Global git user.name already set to: $(git config --global user.name)"
}

if (-not (git config --global user.email)) {
    git config --global user.email "you@example.com"
    Write-Host "Set global git user.email (replace with your email)"
} else {
    Write-Host "Global git user.email already set to: $(git config --global user.email)"
}

# Initialize repo if needed
if (-not (Test-Path ".git")) {
    git init
    Write-Host "Initialized new git repository."
} else {
    Write-Host "Git repository already initialized."
}

# Add remote (remove existing origin if present)
$remotes = git remote
if ($remotes -contains "origin") {
    Write-Host "Remote 'origin' already exists. Removing it first..." -ForegroundColor Yellow
    git remote remove origin
}

git remote add origin $RemoteUrl
Write-Host "Added remote origin -> $RemoteUrl"

# Add and commit
git add .
git commit -m $CommitMessage

# Ensure main branch and push
git branch -M main
git push -u origin main

Write-Host "Push complete. Check your GitHub repository to verify files were uploaded." -ForegroundColor Green
