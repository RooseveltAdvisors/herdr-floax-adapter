# Vision

`herdr-floax` exists so that every Herdr workspace has one retained floating scratch shell: summoned with a keystroke, dismissed without ceremony, and restored exactly as it was left.
It removes a small, recurring tax on attention: scratch terminals that lose their state when hidden, panes that must be re-created and re-navigated per workspace, and floating behavior each tool reimplements on its own.
The reflex itself is borrowed: this plugin adapts the floating scratch workflow that omerxx/tmux-floax established for tmux, rebinding it to the retained scratch API that Herdr core exposes to plugins.
Its reason to stay small is structural: a plugin that only asks core to retain and float a shell has no multiplexer to maintain, no geometry to break, and no cleanup to forget.

## Who it serves

It serves the Herdr operator on Linux or macOS who wants a scratch shell that behaves like furniture: present when called, out of the way when not, and never a state-management chore.
It serves the per-workspace shape of Herdr's model, one retained scratch owned by each workspace, as the manifest's workspace context declares.
It serves reviewers and maintainers by being auditable in one sitting: a manifest with a single permissioned action and a launcher of a dozen lines.
It deliberately does not serve operators of stock Herdr 0.7.4 or the live local-first core, because neither supports retained scratch actions; this plugin is staged ahead of its core dependency and says so in its README.
It does not serve tmux users: tmux already has tmux-floax, and this repository has nothing to add to it.

## What it owns

This repository owns one manifest declaring exactly one permissioned workspace action, `toggle`, gated on core's `retained_scratch` permission and scoped to the workspace context.
It owns one launcher, `scripts/toggle-floax`, that validates the action context Herdr provides and calls `herdr plugin scratch toggle --width 80% --height 80%`.
It owns the honesty of its dependency posture: the README names the exact in-flight core commit the plugin requires, and the plugin is not to be activated before that dependency lands and passes its gate.
It owns robustness at the one seam it actually has: preferring a live `HERDR_BIN_PATH`, falling back to `herdr` on `PATH`, and surviving a replaced server binary whose stale path ends in ` (deleted)`.
It owns the tests that pin this contract: manifest ownership, permission, launcher delegation, and the lineage credit.
It owns its lineage acknowledgement, kept in the manifest description, the README, and the license file, because credit to omerxx/tmux-floax is a condition of the design, not decoration.

## What it refuses to own

It refuses to own floating geometry, process lifetime, workspace ownership, focus, and cleanup; Herdr core owns those, and the moment the plugin reimplements any of them it becomes a competing terminal multiplexer.
It refuses a pane entrypoint and a plugin binary; the executable artifact is deliberately the small action adapter and nothing else.
It refuses to invent a fallback floating implementation for cores that lack the retained scratch API; on such cores the plugin stays inert, and that is the correct behavior.
It refuses to grow a second action: one toggle, one context, one permission is the whole surface.

## The experience it must create

One keystroke shows an 80% by 80% shell over the active workspace; the same keystroke hides it; the shell process and its terminal state survive the hiding.
Toggling back brings the same process and terminal state, not a fresh shell.
Nothing asks to be managed: no pane to close, no layout to restore, no state to lose.
Installation is equally without ceremony: install the plugin, reload the server, bind the action to a key such as the README's `prefix+p` example.
When the plugin cannot keep its promises, it says so plainly and does nothing: it exits with an error rather than approximating the behavior on a core that cannot support it.

## Principles that decide trade-offs

Delegate to core before implementing in the plugin; the plugin's value is restraint.
One action, one job; surface area is the primary cost in a plugin, and every addition must pay for itself in the operator's reflex.
Honest unavailability beats optimistic breakage: a plugin staged ahead of its core says so and stays out of the way.
Robustness belongs at real seams only: validate what core hands the launcher, tolerate the stale-binary-path reality of a replaced server, and add no defensive machinery beyond that.
Contracts live in tests: the manifest's ownership, permission, and delegation behavior are asserted, not described.
Credit is a contract: the tmux-floax acknowledgement is enforced in three files by a test.
Plainness wins: shell, TOML, and unittest, the tools a reviewer already knows.

## Non-goals

This plugin is not, and must never become:

- a floating-pane backend or a terminal multiplexer inside a plugin;
- a fallback floating implementation for cores without the retained scratch API;
- a multi-pane, multi-layout, or configurable-geometry system beyond what core's retained scratch offers;
- a cross-multiplexer portability layer; tmux support in particular is out of scope.

## Done well, one year out

A compatible Herdr core has shipped; the activation gate has been passed, including its supervised handoff; the plugin is installed and its toggle is muscle memory.
The repository still reads in one sitting: one manifest, one launcher, one test file, and a short README that names its dependency exactly.
Core's retained scratch API will have evolved, and the adapter will have tracked it in a handful of lines rather than grown machinery; where core and plugin disagreed, the plugin waited rather than improvised.
The lineage credit is intact, the contract tests are green, and nobody has had to debug floating geometry here, because there is none.
