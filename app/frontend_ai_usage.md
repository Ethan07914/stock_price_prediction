# Frontend AI Usage

## Terminal Experience

### Prompt

Can streamlit display a terminal like box on the front end. I want to be able to display each stage of the pipeline such as extract, transform, load and complete.

### Generated Code

```python
import streamlit as st
import time

st.title("META Data Pipeline")

# 1. Create a styled container for the 'terminal'
terminal_placeholder = st.empty()
terminal_text = "user@meta-pipeline:~$ starting process...\n"

def log_to_terminal(message):
    global terminal_text
    terminal_text += f"> {message}\n"
    # Wrap in st.code to get the terminal font and background
    terminal_placeholder.code(terminal_text, language="bash")

# --- Example Pipeline ---
if st.button("Run Pipeline"):
    log_to_terminal("Initializing extraction...")
    time.sleep(1)
    
    log_to_terminal("Extracting META stock data from API...")
    time.sleep(2)
    log_to_terminal("Extract Complete. [OK]")
    
    log_to_terminal("Running Transformations...")
    time.sleep(1)
    log_to_terminal("Transformation Complete. [OK]")
    
    log_to_terminal("Pipeline Finished Successfully.")
```