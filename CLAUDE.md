# CLAUDE.md - Go Cron Per Second

## Module Purpose

Sub-minute cron scheduling for Odoo 18. Enables second-level job execution.

## Key Models

- `go.cron.second`: Configuration model for second-level scheduling
- Extension of `ir.cron`: Adds second interval support

## Extension Points

- Inherit `ir.cron` to add custom second-level jobs
- Override scheduling logic for custom intervals

## Testing

Test scheduled actions with second intervals manually via Settings > Technical > Scheduled Actions.
