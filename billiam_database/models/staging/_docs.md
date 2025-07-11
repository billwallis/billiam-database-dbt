# Staging Objects

The staging objects are the first "layer" of the warehouse (other than the raw layer which is where the raw data is dumped by external processes).

The dbt documentation calls these the "atomic building blocks" of the warehouse:

- https://docs.getdbt.com/guides/best-practices/how-we-structure/2-staging

The staging models are the only ones that should use the `source` Jinja macro, and these models are typically views since the operations that they perform are simple (aligning column names, casting datatypes, etc).

## [stg\_\_daily_tracker](stg__daily_tracker.sql)

{% docs stg__daily_tracker %}

Work tracker history from 2019-04-23.

The source of this model is my "automated" timesheet application, available at:

- https://github.com/billwallis/daily-tracker

Each row corresponds to an interval of work, which has a timestamp, details about the work, and the duration of the interval.

{% enddocs %}

## [stg\_\_finances](stg__finances.sql)

{% docs stg__finances %}

Item-level transaction history from 2018-01-18.

The source of this model is a Google Sheet that I maintain manually (🤮). Each row corresponds to an item, which has details about the item and about the transaction.

This source is already heavily denormalised (it's a single table!) so some of the details aren't quite perfect such as associating payments with transactions. This will hopefully be updated in the future which would mean updating this project to do the denormalisation here.

{% enddocs %}

## [stg\_\_monzo_transactions](stg__monzo_transactions.sql)

{% docs stg__monzo_transactions %}

Transaction-level history from Monzo.

This is a Google Sheet that Monzo provides. This source provides values in two ways:

1. Additional data per transaction, such as the address and local currency
2. Data validation with my item-level history since, as a human, I'm prone to error

{% enddocs %}
