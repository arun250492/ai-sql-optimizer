# AI SQL Optimizer

## Overview
The AI SQL Optimizer is a project that leverages the OpenAI API to analyze and optimize SQL and PL/SQL queries. The AI agent can request necessary schema, tables, and other details to perform query optimization, aiming to reduce execution time without affecting the actual functionality or logic of the code.

## Project Structure
```
ai-sql-optimizer
├── src
│   ├── agent.py          # Defines the SQLAgent class for interacting with the OpenAI API
│   ├── optimizer.py      # Contains the QueryOptimizer class for analyzing and optimizing queries
│   ├── schema_utils.py   # Provides utility functions for fetching and validating database schema
│   └── app.py           # Entry point for the Gradio interface
├── requirements.txt      # Lists project dependencies
├── README.md             # Project documentation
└── .gitignore            # Specifies files to ignore in Git
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-sql-optimizer
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Set up your OpenAI API key in your environment variables:
   ```
   export OPENAI_API_KEY='your-api-key'  # On Windows use `set OPENAI_API_KEY='your-api-key'`
   ```

2. Run the application:
   ```
   python src/app.py
   ```

3. Access the Gradio interface in your web browser at `http://localhost:7860`.

## Features
- Analyze large SQL and PL/SQL queries.
- Request necessary schema and table details.
- Perform query optimization to reduce execution time.
- Maintain the original functionality and logic of the queries.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

