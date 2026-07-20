import pathlib
import tomllib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class FloaxManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = tomllib.loads((ROOT / "herdr-plugin.toml").read_text())

    def test_manifest_owns_one_permissioned_workspace_action_and_no_pane(self) -> None:
        self.assertEqual(self.manifest["id"], "RooseveltAdvisors.herdr-floax")
        self.assertNotIn("panes", self.manifest)
        self.assertEqual(len(self.manifest["actions"]), 1)
        action = self.manifest["actions"][0]
        self.assertEqual(action["id"], "toggle")
        self.assertEqual(action["contexts"], ["workspace"])
        self.assertIs(action["retained_scratch"], True)
        self.assertEqual(action["command"], ["./scripts/toggle-floax"])

    def test_launcher_delegates_to_core_and_handles_a_stale_binary_path(self) -> None:
        script = (ROOT / "scripts" / "toggle-floax").read_text()
        self.assertIn('[ -x "$HERDR_BIN_PATH" ]', script)
        self.assertIn("command -v herdr", script)
        self.assertIn("plugin scratch toggle", script)
        self.assertNotIn("tmux ", script)

    def test_public_metadata_credits_tmux_floax(self) -> None:
        self.assertIn("omerxx/tmux-floax", self.manifest["description"])
        self.assertIn("omerxx/tmux-floax", (ROOT / "README.md").read_text())
        self.assertIn("omerxx/tmux-floax", (ROOT / "LICENSE").read_text())


if __name__ == "__main__":
    unittest.main()
