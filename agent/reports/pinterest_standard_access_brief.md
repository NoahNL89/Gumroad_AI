# Pinterest Standard Access Demo Brief

Research verified: 2026-07-16 against Pinterest's official access-tier,
authentication, Pin-creation, rate-limit, and developer-policy documentation.

## Accurate app positioning

> A private, single-user Pinterest content assistant for Schep Digital's own
> Gumroad products. It creates a product-specific Pin draft, shows the title,
> description, destination, image, and board, and publishes only the individual Pin
> I choose. It uses Pinterest OAuth and does not collect Pinterest passwords,
> cookies, or data from other accounts.

Do not describe it as an autonomous bot. Pinterest requires the user to choose each
Pin that is scheduled or published.

## What Trial access can demonstrate

- Read your own account, boards, and Pins.
- Create boards and Pins that are visible only to the creator as sandbox entities.
- Demonstrate a complete OAuth and Create Pin flow.
- Trial Pin creation cannot produce public reach or sales.

## Video recording script

Pinterest explicitly accepts a terminal recording for a single-user app, but the
video must show OAuth and a live Pinterest integration.

1. Start the screen recording with the Pinterest app page showing Trial access.
2. In the terminal, run `scripts/pinterest login`.
3. Open the generated OAuth URL, show the requested minimal scopes, and approve it.
4. Copy only the returned `code`; do not show the app secret or tokens.
5. Run `scripts/pinterest exchange "<code>"`. The command prints token presence,
   not token values.
6. Run `scripts/pinterest draft` and show the individual title, description, link,
   image, product, and approval status.
7. Run `scripts/pinterest sandbox-promote` to execute a live sandbox Create Pin API
   request.
8. Open Pinterest and show the creator-only sandbox Pin or board.
9. Return to the terminal and explain that production uses
   `scripts/pinterest publish <draft.json>` only after choosing that specific Pin.

Keep the recording short and readable. Hide `.env` and all secret values.

## Standard access submission

1. Confirm the privacy policy URL is public and associated with Schep Digital.
2. In **My apps**, choose **Upgrade** on the eligible app.
3. Use the app positioning above and upload the demo video.
4. After approval, create a fresh OAuth token with:
   `user_accounts:read,boards:read,boards:write,pins:read,pins:write`.
5. Only then set `PINTEREST_ALLOW_PRODUCTION=1` and use
   `https://api.pinterest.com/v5`.

## Approved automation boundary

The workspace may automatically:

- refresh the retail catalog;
- select a non-duplicate product and prepare unique copy;
- enforce rate and duplicate limits;
- create a review draft;
- send a Pushover message that a draft is ready;
- publish the one draft you explicitly choose.

It must not publish public Pins unattended, auto-follow accounts, scrape Pinterest,
or create repetitive Pins. This boundary protects the account and is part of the
Standard access story.
