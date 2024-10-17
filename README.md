# langchain_cortex
Trying the Langchain notebook integration and will keep building this up. In this example we will be using Two quickstarty add langchain integration 

1. [Quickstart-Cortex Search ](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/tutorials/cortex-search-tutorial-1-search#introduction)

     Integrarating langchain at [Step 4 Stremlit App ](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/tutorials/cortex-search-tutorial-1-search#step-4-create-a-streamlit-app) 


2. [Quickstart-Cortex RAG LLM ](https://quickstarts.snowflake.com/guide/ask_questions_to_your_own_documents_with_snowflake_cortex_search/index.html?index=..%2F..index#0)


Step 1 - Lets create the conda env

```python
conda create -n snowflake-langchain python=3.10
conda activate snowflake-langchain  

```

Step 2 

```python
pip install -r requirements.txt

```

step 3 
```python
cp connect.json snow_connect.json
cp connect.json langchain_cs.json
```


step 4

For [Quickstart-Cortex Search ](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/tutorials/cortex-search-tutorial-1-search#introduction)

```
snow_connect.json-- Parameters please update youer id/password 
{
    "account": "xxxx",
    "user": "xxxx",
    "password": "xxxx",
    "role": "ACCOUNTADMIN",
    "warehouse": "cortex_search_tutorial_wh",
    "database": "cortex_search_tutorial_db",
    "schema": "public",
    "client_session_keep_alive": "True"
}

```
For [Quickstart-Cortex RAG LLM ](https://quickstarts.snowflake.com/guide/ask_questions_to_your_own_documents_with_snowflake_cortex_search/index.html?index=..%2F..index#0)

if you don't have WH configured 

```CREATE OR REPLACE WAREHOUSE cortex_search_tutorial_wh WITH
     WAREHOUSE_SIZE='X-SMALL'
     AUTO_SUSPEND = 120
     AUTO_RESUME = TRUE
     INITIALLY_SUSPENDED=TRUE;```

```
```
langchain_cs.json-- Parameters please update youer id/password 
{
    "account": "xxxx",
    "user": "xxxx",
    "password": "xxxx",
    "role": "ACCOUNTADMIN",
    "warehouse": "cortex_search_tutorial_wh",
    "database": "CC_QUICKSTART_CORTEX_SEARCH_DOCS",
    "schema": "DATA",
    "client_session_keep_alive": "True"
}
```

step 5 Run For [Quickstart-Cortex Search Stremlit app](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/tutorials/cortex-search-tutorial-1-search#step-4-create-a-streamlit-app)

[USe this Sreamlit App on your local env with langchain](/src/langchain_cortexsearch.py)

step 6 to run  For [Quickstart-Cortex RAG LLM ](https://quickstarts.snowflake.com/guide/ask_questions_to_your_own_documents_with_snowflake_cortex_search/index.html?index=..%2F..index#4)

[USe this Sreamlit App on your local env with langchain](/src/langchain_RAG.py)


Optional - Connecting Cortex https://pypi.org/project/langchain-snowflake/ from local env 


```python
## In your directory 
touch .env 

### In env file 
LANGCHAIN_API_KEY="XXXXXX"
LANGCHAIN_PROJECT="Cortex-langchainintegration"

SNOWFLAKE_ACCOUNT=XXXXX
SNOWFLAKE_USERNAME=XXXX
SNOWFLAKE_PASSWORD=XXXXX
SNOWFLAKE_DATABASE=XXXXX
SNOWFLAKE_SCHEMA=XXXXX
SNOWFLAKE_WAREHOUSE=XXXXX
SNOWFLAKE_ROLE=XXXXX

```
[Testing Langchain_cortexsearch notebook ](/src/langchain_cortexsearch.ipynb)
