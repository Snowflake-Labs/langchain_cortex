import os
import json
import snowflake.connector
from snowflake.snowpark import Session

connection_parameters = json.load(open("./snow_connection.json"))


def connection() -> snowflake.connector.SnowflakeConnection:
    creds = {
        "account": "",
        "user": "",
        "password": "",
        "role": "accountadmin",
        "warehouse": "",
        "database": "",
        "schema": "public",
        "client_session_keep_alive": "True",
    }
    return snowflake.connector.connect(**creds)


def session() -> Session:
    return Session.builder.configs(connection_parameters).create()

