# Revenue Automation and Pushover Notifications

## Installed schedule

- Every morning at **08:07 UTC** and evening at **18:07 UTC**: `scripts/go.sh`
- Daily at **20:15 UTC**: `scripts/month_end.sh`

The month-end launcher exits immediately on every day except the final UTC day of
the month. Successful month summaries are deduplicated in `db/store.db`, so only one
message is sent for each month.

## Pushover events

Pushover uses `PUSHOVER_USERKEY` and `PUSHOVER_APPKEY` from the gitignored `.env`.
The keys are never printed by the notification code.

Notifications are sent for:

- a GO run that produces a new commit or measurable sales movement;
- a failed GO run, with the log location;
- an experiment evaluation date and its resulting next action;
- a newly prepared Pinterest draft that requires individual approval;
- the final monthly sales/revenue/target/audience overview.

Informational events use normal priority. Failures and below-target month-end or
zero-sale experiment evaluations use high priority, not emergency priority.

Test safely:

```bash
python3 scripts/ops_notify.py test --dry-run
python3 scripts/ops_notify.py test
```

Logs:

```text
/tmp/schep_go.log
/tmp/schep_month_end.log
```

## Pinterest revenue workflow

The public retail feed is:

```text
https://raw.githubusercontent.com/NoahNL89/GumRoad_AI/main/catalog/pinterest_catalog.csv
```

After Standard access, the workspace will automate catalog refresh, focused draft
selection, educational copy variants, UTM attribution, rate limits, duplicate
protection, and Pushover review alerts. Pinterest policy requires the owner to choose
each Pin, so public publishing remains one explicit command:

```bash
scripts/pinterest publish agent/pinterest_queue/<draft>.json
```

This is the highest automation level that preserves the account's access and avoids
spam behavior.
