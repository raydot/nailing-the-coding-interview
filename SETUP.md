# Development Setup

## Conda Environment

This project uses Anaconda for Python environment management.

### First Time Setup

```bash
# Create the environment from the environment.yml file
conda env create -f environment.yml

# Activate the environment
conda activate coding-interview-book
```

### Daily Usage

```bash
# Activate the environment
conda activate coding-interview-book

# Build the book locally
jupyter-book build .

# Open the built book
open _build/html/index.html
```

### Updating Dependencies

```bash
# Activate environment
conda activate coding-interview-book

# Update all packages
conda env update -f environment.yml --prune

# Or add new packages
conda install package-name
# Then update environment.yml manually
```

### Deactivate

```bash
conda deactivate
```

## Quick Reference

| Command | Purpose |
|---------|---------|
| `conda activate coding-interview-book` | Start working |
| `jupyter-book build .` | Build the website |
| `jupyter-book clean .` | Clean build files |
| `jupyter lab` | Launch Jupyter for editing notebooks |
| `conda deactivate` | Stop working |

## Troubleshooting

**Environment not found?**
```bash
conda env list  # Check if it exists
conda env create -f environment.yml  # Create if missing
```

**Build errors?**
```bash
jupyter-book clean .  # Clean old builds
jupyter-book build . --all  # Rebuild everything
```
