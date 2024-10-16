# langchain_cortex
Trying the Langchain notebook integration and will keep building this up. In this example we will be using 

https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/tutorials/cortex-search-tutorial-1-search#introduction


Step 1 - Lets create the conda env

```python
conda create -n snowflake-lanchain python=3.10
conda activate snowflake-lanchain  

```

Step 2 

```python
pip install -r requirements.txt

```

Step 3 

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

Step 4 Follow the tutorial to create the service  [Setup](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/tutorials/cortex-search-tutorial-1-search#step-1-setup)


Step 6 [Load the data ](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/tutorials/cortex-search-tutorial-1-search#step-2-load-the-data-into-snowflake)

 
Step 7 [Creating the service](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/tutorials/cortex-search-tutorial-1-search#step-3-create-the-search-service)


Step 8 [Testing Langchain_cortexsearch notebook ](/src/langchain_cortexsearch.ipynb)


Step 9 [Testing Sreamlit App ](/src/langchain_cortexsearch_app.py)

Step 10 Langchain Tracking 