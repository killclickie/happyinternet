# Slop Stopper collects no data

Slop Stopper is a set of instructions and one local script that run inside your own Claude session.

- **Nothing collected or stored.** The plugin has no servers, accounts, analytics or telemetry. It keeps no copy of your drafts.
- **No network calls.** The scanner (`skills/final-review/scripts/scan.py`) reads the draft file it's given, prints results and exits. It sends nothing anywhere.
- **No connected services.** The plugin declares no MCP servers, hooks or outside integrations.
- **Your drafts go only where Claude already sends them.** Reviews run in your Claude session, under Anthropic's privacy policy and your account's settings.

Questions: open an issue at https://github.com/killclickie/happyinternet/issues.
