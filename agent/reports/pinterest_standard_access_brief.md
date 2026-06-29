# Pinterest Standard Access Brief

## App Positioning

Describe the app as:

> A private single-user Pinterest content scheduler for Schep Digital's own Gumroad products. It prepares product Pin drafts from my store catalog, lets me review the Pin title, description, destination link, image URL, and board, and publishes only the specific Pin I approve.

Avoid describing it as an autonomous promotion bot.

## Production Behavior

- OAuth only; no password, cookie, or session scraping.
- Minimal scopes: `user_accounts:read`, `boards:read`, `boards:write`, `pins:read`, `pins:write`.
- `promote` and `post` create local draft JSON files only.
- `approve <draft.json>` publishes one reviewed draft.
- Production API base: `https://api.pinterest.com/v5`.
- Sandbox API base: `https://api-sandbox.pinterest.com/v5`.

## Demo Recording Checklist

1. Run `python3 bot/pinterest_bot.py auth-url`.
2. Open the OAuth URL in a browser and show Pinterest consent.
3. Approve the scopes and copy the redirect `code`.
4. Run `python3 bot/pinterest_bot.py exchange "<code>"` and show token presence only, not token values.
5. Run `python3 bot/pinterest_bot.py draft` and show the review fields.
6. Run `python3 bot/pinterest_bot.py sandbox-promote`.
7. Show the created sandbox Pin or board in Pinterest.
8. Explain that production posting uses `approve <draft.json>` after reviewing each Pin.

## Current Status

Production Pin creation is blocked while the app has Trial access. The expected Pinterest error is code 29. Sandbox Pin creation works and is suitable for the Standard access demo.
