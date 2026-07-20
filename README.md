# herdr-floax

A thin [Herdr](https://herdr.dev) plugin for a retained floating scratch shell, one per workspace.

## Lineage and credit

The workflow follows [omerxx/tmux-floax](https://github.com/omerxx/tmux-floax), “The missing
floating pane for Tmux.” This Herdr adaptation is not presented as an original UX invention. The
plugin delegates floating geometry, process lifetime, workspace ownership, focus, and cleanup to
Herdr core rather than reimplementing a multiplexer inside a plugin.

## Core dependency and activation gate

**This plugin is staged ahead of its core dependency. Do not activate it on stock Herdr 0.7.4 or
the live local-first core `7e1e356f8b1b4596ae345f68cf497dc618e7a243`.** Those builds do not
support retained scratch actions.

The current exact dependency is the in-flight Herdr commit
`0e080c3ec72060085b0daaef70d734c3ad2dde85` on branch
`fm/herdr-floax-retained-popup`. It adds:

- manifest action permission `retained_scratch = true`;
- `plugin.scratch.toggle` and `herdr plugin scratch toggle`;
- workspace/action-owned retained terminal state and floating rendering.

Activation is gated on that Herdr change passing review/no-mistakes, resolving its open focus/modal
product decisions, and receiving a supervised local-first core handoff. The plugin intentionally
does **not** invent a fallback floating implementation.

## Action

`RooseveltAdvisors.herdr-floax.toggle` asks core to show or hide an 80% × 80% scratch shell in the
active workspace. Hiding preserves the shell process and terminal state; toggling again restores
it. There is no plugin pane entrypoint and no plugin binary by design—the executable artifact is
the small `scripts/toggle-floax` action adapter.

Once a compatible core is active:

```bash
herdr plugin install RooseveltAdvisors/herdr-floax
herdr server reload-config
```

```toml
[[keys.command]]
key = "prefix+p"
type = "plugin_action"
command = "RooseveltAdvisors.herdr-floax.toggle"
description = "toggle retained scratch shell"
```

The launcher validates `HERDR_BIN_PATH` and falls back to `herdr` on `PATH`, covering a replaced
Linux server executable whose stale path ends in ` (deleted)`.

## Development

```bash
python3 -m unittest discover -s tests -v
```

Core behavior is tested and reviewed in Herdr itself; this repository tests only the permissioned
manifest and action adapter.

## License

MIT — see [LICENSE](LICENSE). The license file also records the tmux-floax lineage acknowledgement.
