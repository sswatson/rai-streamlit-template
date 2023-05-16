
# RelationalAI-Streamlit Starter Template

This repo will help you get started with building a Streamlit app that uses RelationalAI as a backend.

## Setup

To clone the repo, do

```bash
git clone https://github.com/sswatson/rai-streamlit-template.git
```

### Environment manager

This template follows Streamlit's recommendation to use `pipenv` as the environment manager. To install `pipenv`, run:

```bash
pip install pipenv
```

Then, to install the dependencies, run the following from this directory:

```bash
pipenv install
```

If you want to install more packages, you should do so with `pipenv install foobar` in place of `pip install foobar`.

### Credentials

Use the RelationalAI Console to get your credentials. If you have RelationalAI configured locally, you can find your credentials in `~/.rai/config`. You should put these credentials in a file called `.streamlit/secrets.toml`. The contents should look like this:

```
[rai]
host = "azure.relationalai.com"
client_id = "9a3tabDb898fksdfjasdjQjfp9FMjfk2"
client_secret = 
"9fsdfkqnfs923J-39fjasdfka-fajsafusdDFUDSFNQPFSNdjfs8fsjnwf-DJfnw"
```

Note that quotation marks are required around the values; you'll have to add these if you are copying and pasting from your local configuration file. Also, the name `[rai]` at the top of this block is required.

(The credentials above are fake and are for illustrative purposes only. You have to replace them with your own credentials.)

## Running the app locally

To run the app, run the following from this directory:

```bash
pipenv run streamlit run Welcome.py
```

This starts a server and launches a web browser for you. If everything is set up correctly, you will find a list of the databases in your account in the page `Example`.

## Deploying the app

To deploy this app, create an account at https://streamlit.io and follow the instructions there. You will need to paste the credentials above into the web app. Also, you should choose Python 3.8 for compatibility with the Python version specified in this `pipenv` environment.

## Next Steps

Check out Streamlit's gallery of apps to see what you can build with Streamlit: https://streamlit.io/gallery. For details on the RelationalAI Python library, see https://docs.relational.ai/rkgms/sdk/python-sdk.

# Explanation of Files

`Welcome.py`. This is the main file for the Streamlit app. It contains the code that is run when you run `pipenv run streamlit run Welcome.py`.

`pages/1_Example.py`. Streamlit supports multi-page apps via the `pages` directory. The file name dictates that tab name of the page. The code in this file is run when you click on the tab `Example`. The numeric prefix ensures that the tabs are ordered correctly (the number and underscore are not included in the tab name).

`lib/rai.py`. This is where we put the code that connects to the RelationalAI backend. The context object `ctx` in this file is imported by pages that need to connect to RelationalAI.

`.gitignore`. This file tells Git which files to ignore. This file is important because the `.streamlit/secrets.toml` file should not be committed to version control for security reasons.

`Pipfile` and `Pipfile.lock`. These files are used by `pipenv` to manage the dependencies for this project.
