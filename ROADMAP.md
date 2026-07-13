[project]
name = "movie-rating-analysis"
version = "1.0.0"
description = "CODTECH internship project: Movie Rating Analysis pipeline"
authors = [{ name = "Sumit Kumar" }]
requires-python = ">=3.10"
readme = "README.md"
license = { text = "MIT" }

[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
