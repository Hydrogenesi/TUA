# Changelog

## Unreleased

### Changed
- Full type hints on `matriun` and `matriun_cli`; new `Matrix` / `Number` aliases.
- Docstrings now state shape rules, error conditions, and an example per function.
- CLI demo matrix A is asymmetric (`A[i][j] = i*N + j`) so the transpose is visibly different.
- README rewritten to match the code; added `docs/API_REFERENCE.md`,
  `docs/ARCHITECTURE.md`, `docs/DEVELOPMENT.md`.
- Plate71 and 71-Order documents are explicitly labelled **planned**.

### Added
- `add_matrices` raises `ValueError` on shape mismatch (previously `IndexError`).
- `create_zero_matrix` / `create_identity_matrix` raise `ValueError` on negative sizes.
- Tests for the above and for CLI exit code `2` on `--size 0`.
- `[project.optional-dependencies] dev = ["pytest"]`.

### Removed
- `INDEX.md`, `CEREMONIAL_INSCRIPTION.md`, `DynamoSuite-Framework.md` — described
  ~25 files that never existed in this repository.
- Empty `docs/README.md`; `msal`/`requests` from `requirements.txt` (unused).

## 0.1.0

- Initial release: eight matrix helpers and the `matriun demo` CLI.
