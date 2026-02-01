# Running the Project Guide

This guide provides detailed instructions on how to run the documentation server, perform linting, and execute tests using `uv`.

## ⚡️ Poe Task Runner (Recommended)

We have integrated `poethepoet` to streamline project tasks. You can run these commands easily through `uv`.

### Available Tasks
| Task | Command | Description |
| :--- | :--- | :--- |
| `serve` | `uv run poe serve` | Start the MkDocs development server |
| `build` | `uv run poe build` | Build the static site into `site/` |
| `test` | `uv run poe test` | Run all unit tests with `pytest` |
| `lint` | `uv run poe lint` | Run `ruff` linter checks |
| `format`| `uv run poe format`| Auto-format code with `ruff` |

---

## 🛠 Troubleshooting: "poe: command not found"

If you try to run `poe serve` and see `zsh: command not found: poe`, it is because Poe is installed as a project dependency, not a global system command. 

### Solution 1: Use `uv run` (Standard)
Always prefix the command with `uv run`. This tells `uv` to look for the command inside your project's virtual environment.
```bash
uv run poe serve
```

### Solution 2: Global Installation (Optional)
If you want to be able to use `poe` directly without the `uv run` prefix, install it as a global tool using `uv`:
```bash
uv tool install poethepoet
```

> [!NOTE]
> `uv tool install` safely manages the tool in an isolated environment while making the `poe` command available globally on your system.

---

## 🏗 Legacy Project Commands (Manual uv)

If you prefer not to use the task runner, you can still use the direct commands:
- **MKDocs**: `uv run mkdocs serve`
- **Linting**: `uv run ruff check .`
- **Testing**: `uv run pytest`

---

## 🎨 Theming Notes
The project uses a custom **VSCode Dark Modern** theme. 
- **Style location**: `docs/stylesheets/extra.css`
- **Configuration**: `mkdocs.yml`

If you need to adjust colors or layout, modify `extra.css`.
