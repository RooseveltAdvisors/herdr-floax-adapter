# Repository Guidelines

`herdr-floax` is a manifest-and-script adapter for Herdr core's retained scratch API. It follows
the omerxx/tmux-floax UX lineage but must never implement a competing terminal multiplexer or
floating-pane backend.

## Project shape

- `herdr-plugin.toml`: id `RooseveltAdvisors.herdr-floax`, permissioned `toggle` action, no pane.
- `scripts/toggle-floax`: validates Herdr action context and calls `plugin scratch toggle`.
- `tests/test_manifest.py`: manifest ownership, permission, and launcher contract.
- `README.md`: authoritative core dependency and activation gate.

Keep lineage credit to `omerxx/tmux-floax` in README, LICENSE notes, and manifest metadata. Keep the
exact core dependency current until the retained scratch API lands in a public Herdr release.

## Development

```bash
python3 -m unittest discover -s tests -v
```

## Maintaining this file

Update this file only for durable repository-wide guidance. Prefer pointers to authoritative files
and commands over duplicated implementation details, and remove stale guidance when behavior moves.
