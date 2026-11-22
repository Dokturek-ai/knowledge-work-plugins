---
name: write-query
description: Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and aggregations, optimizing a query against a large partitioned table, or getting dialect-specific syntax for PostgreSQL, Firebird 3 or another SQL engine.
argument-hint: "<description of what data you need>"
---

> **Doktůrek:** Before the first step, read [the Doktůrek context](../../shared/dokturek-context.md) and apply it: Czech output, sources of truth, data rules, confirmation before anything leaves the company, and routing to the other Doktůrek plugins.

## Doktůrek specifics

- Never write a query that returns patient-level rows from a real database. Prefer aggregates and synthetic test instances.
- **Medplum's PostgreSQL:** a direct SQL query bypasses Medplum's AccessPolicy and leaves no AuditEvent. Write such queries only for a synthetic or test instance, never for an environment with real data. Access to Medplum data belongs to the `dokturek-dev-toolkit` marketplace (`Dokturek-ai/developer-toolkit`); route the user there.
- **Incumbent AIS database copy (Firebird 3):** only `COUNT`, `MAX(date)` and `SUM(IIF(...))` style aggregates, as in `dokturek-docs` → `36-analyza-ambulantniho-ais/01-metodika-a-zdroje.md` (section 5). Never list values of name, rodné číslo, insurance-number or date columns, and suppress groups smaller than 5. The legal basis for the copy is an open question (Q-753).

# /write-query - Write Optimized SQL

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Write a SQL query from a natural language description, optimized for your specific SQL dialect and following best practices.

## Usage

```
/data:write-query <description of what data you need>
```

## Workflow

### 1. Understand the Request

Parse the user's description to identify:

- **Output columns**: What fields should the result include?
- **Filters**: What conditions limit the data (time ranges, segments, statuses)?
- **Aggregations**: Are there GROUP BY operations, counts, sums, averages?
- **Joins**: Does this require combining multiple tables?
- **Ordering**: How should results be sorted?
- **Limits**: Is there a top-N or sample requirement?

### 2. Determine SQL Dialect

If the user's SQL dialect is not already known, ask which they use:

- **PostgreSQL** (Medplum's database; synthetic or test instances only)
- **Firebird 3** (the incumbent AIS database copy; aggregates only, see the Firebird section below)
- **DuckDB** or **SQLite** (local analysis of a synthetic or aggregated file)
- **Other** (ask for specifics and use the engine's standard SQL)

Remember the dialect for future queries in the same session.

### 3. Discover Schema (If a Database Is Connected)

If a database MCP server is connected (Doktůrek has no data warehouse):

1. Search for relevant tables based on the user's description
2. Inspect column names, types, and relationships
3. Check for partitioning or clustering keys that affect performance
4. Look for pre-built views or materialized views that might simplify the query

### 4. Write the Query

Follow these best practices:

**Structure:**
- Use CTEs (WITH clauses) for readability when queries have multiple logical steps
- One CTE per logical transformation or data source
- Name CTEs descriptively (e.g., `daily_signups`, `active_users`, `revenue_by_product`)

**Performance:**
- Never use `SELECT *` in production queries -- specify only needed columns
- Filter early (push WHERE clauses as close to the base tables as possible)
- Use partition filters when available (especially date partitions)
- Prefer `EXISTS` over `IN` for subqueries with large result sets
- Use appropriate JOIN types (don't use LEFT JOIN when INNER JOIN is correct)
- Avoid correlated subqueries when a JOIN or window function works
- Be mindful of exploding joins (many-to-many)

**Readability:**
- Add comments explaining the "why" for non-obvious logic
- Use consistent indentation and formatting
- Alias tables with meaningful short names (not just `a`, `b`, `c`)
- Put each major clause on its own line

**Dialect-specific optimizations:**
- Apply dialect-specific syntax and functions (ask which engine when unclear: Medplum runs on PostgreSQL, the incumbent AIS database copy on Firebird 3)
- Use dialect-appropriate date functions, string functions, and window syntax
- Note any dialect-specific performance features (e.g., PostgreSQL indexes and `EXPLAIN`, Firebird plan output)

### 5. Present the Query

Provide:

1. **The complete query** in a SQL code block with syntax highlighting
2. **Brief explanation** of what each CTE or section does
3. **Performance notes** if relevant (expected cost, partition usage, potential bottlenecks)
4. **Modification suggestions** -- how to adjust for common variations (different time range, different granularity, additional filters)

### 6. Offer to Execute

If a database is connected and it is a synthetic or test instance, offer to run the query and analyze the results. Against the AIS copy run only the allowed aggregates. If the user wants to run it themselves, the query is ready to copy-paste.

## Firebird 3 (AIS Database Copy)

Firebird differs from PostgreSQL in ways that break copied queries:

- **No `LIMIT`.** Use `SELECT FIRST 10 SKIP 20 ...` (right after `SELECT`) or the standard `OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY`. On the AIS copy you should not need either: never return rows.
- **Conditional counts with `IIF`:** `SUM(IIF(DATUM >= DATE '2025-05-20' AND DATUM < DATE '2026-05-21', 1, 0))`. `CASE WHEN` also works.
- **System tables `RDB$...` for the schema:** tables in `RDB$RELATIONS` (user tables have `COALESCE(RDB$SYSTEM_FLAG, 0) = 0`), columns in `RDB$RELATION_FIELDS` joined to `RDB$FIELDS` on `RDB$FIELD_SOURCE = RDB$FIELD_NAME`. Names are padded `CHAR`, so wrap them in `TRIM()`.
- **Dates:** `DATE 'YYYY-MM-DD'` literals, `CURRENT_DATE`, `DATEADD(-12 MONTH TO CURRENT_DATE)`, `DATEDIFF(DAY FROM a TO b)`, `EXTRACT(YEAR FROM d)`.
- **Strings:** `||` concatenates; unquoted identifiers are upper case.
- Run queries through `isql` against a **copy** of the database, never against a practice's live installation.

```sql
-- Allowed shape on the AIS copy: one aggregate row per table
SELECT 'TBL_EXAMPLE' AS table_name,
       COUNT(*) AS n_total,
       MAX(DATUM) AS last_activity,
       SUM(IIF(DATUM >= DATEADD(-12 MONTH TO DATE '2026-05-21'), 1, 0)) AS n_last_12m
FROM TBL_EXAMPLE;
```

## Examples

**Simple aggregation:**
```
/data:write-query Count of orders by status for the last 30 days
```

**Complex analysis:**
```
/data:write-query Cohort retention analysis -- group users by their signup month, then show what percentage are still active (had at least one event) at 1, 3, 6, and 12 months after signup
```

**Performance-critical:**
```
/data:write-query We have a 500M row events table partitioned by date. Find the top 100 users by event count in the last 7 days with their most recent event type.
```

## Tips

- Mention your SQL dialect upfront to get the right syntax immediately
- If you know the table names, include them -- otherwise Claude will help you find them
- Specify if you need the query to be idempotent (safe to re-run) or one-time
- For recurring queries, mention if it should be parameterized for date ranges
