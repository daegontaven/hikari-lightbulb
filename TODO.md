# TODO

## Main

- [x] Custom Bot Class
  - [x] Bot Checks
  - [x] Multiple Owners
  - [x] Get prefix function (sync or async)

- [x] Plugins
  - [x] Support Prefix Commands
  - [x] Support Slash Commands
  - [x] Support Message Commands
  - [x] Support User Commands
  - [x] Support Listeners
  - [x] Plugin Unload Hook
  - [x] Plugin Check
  - [x] Plugin error handler

- [x] Extensions
  - [x] Load
  - [x] Unload
  - [x] Reload

- [ ] Commands
  - [x] Base Command
  - [x] Base Application Command (needs creation methods)
  - [x] Prefix Commands
    - [x] Invocation
    - [x] Parsing
    - [x] Groups & subcommands
  - [ ] Slash Commands
    - [x] Option Types
    - [x] Channel Types
    - [x] Groups & subcommands
    - [ ] ~~Autocomplete~~ (blocked)
  - [ ] ~~Message Commands~~ (blocked)
  - [ ] ~~User Commands~~ (blocked)
  - [x] Per-Command Error Handler
    - [x] Prefix commands
    - [x] Slash commands
    - [x] ~~Message commands~~ (blocked)
    - [x] ~~User commands~~ (blocked)
  - [ ] Auto-managing of Application Commands
    - [x] Slash Commands
    - [ ] ~~Message commands~~ (blocked)
    - [ ] ~~User commands~~ (blocked)

- [x] Checks (Reuse?)
  - [x] DM Only
  - [x] Guild Only
  - [x] Human Only
  - [x] Bot Only
  - [x] Webhook Only
  - [x] Owner Only
  - [x] Has Roles
  - [x] (Bot) Has Guild Permissions
  - [x] (Bot) Has Role Permissions
  - [x] (Bot) Has Channel Permissions
  - [x] Has Attachment
  - [x] Custom Checks
  - [x] Check Exempt?

- [ ] Context
  - [x] Base Class
  - [x] Prefix Context
  - [x] Slash Context
  - [ ] ~~Message Context~~ (blocked)
  - [ ] ~~User Context~~ (blocked)

- [x] Converters
  - [x] Base Converter
  - [x] User Converter
  - [x] Member Converter
  - [x] Guild Channel Converter
  - [x] Guild Voice Channel Converter
  - [x] Category Converter
  - [x] Guild Text Channel Converter
  - [x] Role Converter
  - [x] Emoji Converter
  - [x] Guild Converter
  - [x] Message Converter
  - [x] Invite Converter
  - [x] Colo(u)r Converter
  - [x] Timestamp Converter

- [ ] Special Converter Support for Slash Commands?

- [x] Special Args
  - [x] Greedy
  - [x] Consume Rest

- [x] Cooldowns (Reuse?)

- [x] Events
  - [x] *Command Completion Event
  - [x] *Command Invocation Event
  - [x] *Command Error Event

- [x] Errors (Reuse?)

- [ ] Parsing
  - [x] Standard Parser
  - [ ] CLI Parser
  - [x] Custom Parsing

- [x] Help Command

- [x] Paginators (Reuse?)

- [x] Navigators (Reuse?)

- [x] Utils (Reuse?)
  - [x] get
  - [x] find
  - [x] permissions_in
  - [x] permissions_for

- [ ] Command validation
  - [x] Prefix commands
  - [x] Slash commands
  - [ ] Message commands
  - [ ] User commands

## Other

- [x] Paginated/Navigated Help Command
- [ ] Embed Help Command
- [x] Default Ephemeral Flags
- [ ] Reinvoke on edits
- [x] Broadcast typing on command invocation
- [x] Default enabled guilds
- [x] Automatically defer responses
