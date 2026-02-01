# GitHub Pages Integration Guide

This guide explains how the documentation for this project is automatically deployed using GitHub Pages and GitHub Actions.

## Automated Deployment Workflow

The project uses a GitHub Action defined in `.github/workflows/deploy.yml` to automate the deployment process.

### How it works
1. **Trigger**: Every time you push code to the `main` branch.
2. **Setup**: The action installs the `uv` package manager and Python.
3. **Build**: It installs all dependencies (like `mkdocs-material`).
4. **Deploy**: It runs `mkdocs gh-deploy` which pushes the built static site to the `gh-pages` branch.

## Manual Setup Steps (One-time)

To enable the site for the first time:

1. **Commit and Push the Workflow**:
   ```bash
   git add .github/workflows/deploy.yml
   git commit -m "Add GitHub Actions workflow for deployment"
   git push origin main
   ```

2. **Wait for the Workflow**:
   Go to your repository on GitHub.com and click the **Actions** tab. Verify that the `deploy-docs` workflow finishes successfully.

3. **Enable GitHub Pages**:
    - Go to **Settings** > **Pages**.
    - Under **Build and deployment**, set the source to **Deploy from a branch**.
    - Select the `gh-pages` branch and the `/ (root)` folder.
    - Click **Save**.

4. **Access your site**:
   The documentation will be live at `https://<your-username>.github.io/brass-code-vs-code/`.

## Local Preview
Before pushing, you can always preview your changes locally:
```bash
uv run mkdocs serve
```
This will start a local server, usually at `http://127.0.0.1:8000/`.
