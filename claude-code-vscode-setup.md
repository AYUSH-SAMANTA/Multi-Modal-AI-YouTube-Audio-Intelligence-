# Setting Up Claude Code in VS Code

## Before you start

- VS Code **1.98.0 or later** (check under Help > About).
- A **paid Claude plan** (Pro, Max, Team or Enterprise), or a Claude Console account with prepaid API credits. A free Claude plan is not enough.

## Install and sign in

1. Open Extensions with `Ctrl+Shift+X` (`Cmd+Shift+X` on Mac).
2. Search for **Claude Code** by Anthropic and click **Install**. If VS Code asks whether to trust the publisher, choose to trust and install.
3. Open any file. A Spark icon appears in the top-right of the editor toolbar. Click it to open the Claude Code panel. If no file is open, click "Claude Code" in the bottom-right status bar instead.
4. Sign in when prompted. Choose the **Claude.ai Subscription** option, authorize in your browser, then return to VS Code.
5. The panel is ready when it says "What to do first? Ask about this codebase or we can start writing code."

Tip: open your project folder (File > Open Folder) so Claude Code can see the whole project.

## Useful settings

| Setting | What it does |
|---------|--------------|
| `claudeCode.initialPermissionMode` | Set to plan mode so Claude proposes changes before editing files |
| `claudeCode.useTerminal` | Switches to a CLI-style interface; both modes share conversation history |
| `claudeCode.autosave` | Saves files automatically before Claude reads or writes them (on by default) |

## Useful shortcuts

| Shortcut (Windows/Linux / Mac) | Action |
|--------------------------------|--------|
| `Ctrl+Esc` / `Cmd+Esc` | Toggle focus between the editor and Claude |
| `Alt+K` / `Option+K` | Insert an @-mention with the current file and line range |
| `Ctrl+Shift+Esc` / `Cmd+Shift+Esc` | Open a new conversation tab |

On macOS Tahoe, clear the Game Controllers checkbox under System Settings > Keyboard > Keyboard Shortcuts so `Cmd+Esc` reaches Claude Code.

## Troubleshooting

**Spark icon is missing**
- Make sure a file is open (the icon only shows then).
- Confirm VS Code is 1.98.0 or higher.
- Run "Developer: Reload Window" from the Command Palette.
- Temporarily disable other AI extensions to rule out conflicts.
- Check that workspace trust is not in Restricted Mode.
- Use the status bar entry as a fallback.

**Claude stops responding mid-conversation**
- Check your internet connection and start a new conversation.
- Run `claude` in a terminal for more detailed errors.
- Run `/compact` to free up context space.

**`claude` not found in the terminal**

The extension bundles its own CLI and does not add `claude` to your PATH. To use it in VS Code's integrated terminal, install the standalone CLI:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

## Sources

- [Claude Code IDE Extensions: VS Code and JetBrains Setup Guide](https://fast.io/resources/claude-code-ide-extensions-guide.md)
- [Claude Code Setup for VS Code (UT Dallas)](https://atlas.utdallas.edu/TDClient/30/Portal/KB/Article/1602/Claude-Code-Setup-for-VS-Code)
- Official docs (check for the latest details): https://docs.claude.com/en/docs/claude-code/overview
