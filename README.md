<div align="center" markdown="1">
<img src="https://raw.githubusercontent.com/thewildaihq/.github/refs/heads/main/assets/logo-flat.jpg" alt="thewildai.com" width="200"/>
<br/>
</div>

## PDF Document Chat with AI using Python, OpenAI Embeddings, and AstraDB

Welcome to the comprehensive guide for building an AI-driven PDF document chat application using Python, OpenAI embeddings, and AstraDB. This project is designed to harness the power of artificial intelligence to facilitate seamless interactions with PDF documents, allowing users to query and retrieve information efficiently. This README provides detailed instructions on setting up the environment, configuring necessary components, and running your PDF chat application. Whether you are a beginner or an experienced developer, this guide will assist you in getting started with ease.

## Introduction

In an era where digital documents are ubiquitous, the ability to quickly access and interact with information within PDFs is invaluable. This project aims to bridge that gap by using advanced machine learning models to process and understand the content of PDFs. By leveraging OpenAI embeddings and AstraDB, we create a robust system that can handle complex queries and provide accurate responses, transforming the way you interact with PDF documents.

## Technologies Used
This project utilizes the following technologies and tools:
- **OpenAI:** For generating embeddings and natural language processing capabilities.
- **AstraDB:** As the vector database for storing and managing embeddings.
- **LangChain:** For managing and chaining language processing tasks.


## Getting Started

To embark on this journey, you need to clone the repository from GitHub. This repository contains all the necessary code and resources to set up your PDF document chat application. Execute the following command to clone the repository:

```bash
git clone https://github.com/thewildai/pdfchat_astra_openai
```

### Prerequisites

Before diving into the installation and setup, ensure you have the following API keys and configuration details ready. These credentials are crucial for connecting to the required services:

- `ASTRA_DB_API_ENDPOINT`: The endpoint for your AstraDB instance.
- `ASTRA_DB_APPLICATION_TOKEN`: The application token for authentication.
- `ASTRA_DB_NAMESPACE`: The namespace for your database.
- `OPENAI_API_KEY`: Your API key for accessing OpenAI services.

### Step-by-Step Setup

This section outlines the step-by-step process for setting up the environment and getting the application up and running.

1. **Create a Vector Database:**
   - Begin by creating a vector database on [AstraDB](https://astra.datastax.com/). This database will store the vector embeddings generated from your PDF documents. If you're unsure how to create a database, refer to [this video tutorial](#) for a comprehensive walkthrough.

2. **Environment Setup:**
   - Once you have your database set up, rename the `env.sample` file to `.env`. Populate this file with the API keys and configuration details you gathered in the prerequisites section. This file is crucial as it allows your application to connect to the necessary services.

3. **Python Environment Setup:**
   - Setting up a virtual environment is essential to ensure your project dependencies do not interfere with your system's Python installation. Follow these commands to set up the environment and install the required packages:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     pip3 install -r requirements.txt
     ```

4. **Add PDF Files:**
   - For the application to process and interact with PDF documents, you need to place your PDF files in the `documents` directory. This directory serves as the input source for the application.

5. **Generate Vector Embeddings:**
   - With your PDF files in place, you can now generate vector embeddings. These embeddings are crucial as they transform the textual content of your PDFs into a format that the AI models can understand. Run the following command to initiate this process:
     ```bash
     python insert.py
     ```

6. **Query Your PDF Document:**
   - With the embeddings generated, you can now interact with your PDF documents. Use the following command to start querying:
     ```bash
     python search.py
     ```

### Troubleshooting

During the setup and execution process, you might encounter certain issues. This section addresses a common problem and provides a solution:

- **Error with New Langchain Version:**
  - It's recommended to always create a virtual environment due to compatibility issues with certain package versions. If you encounter errors related to the Pydantic version, specifically the following:
  
  **Error Message:**
  ```
  pydantic.errors.PydanticUserError: The `__modify_schema__` method is not supported in Pydantic v2. Use `__get_pydantic_json_schema__` instead in class `SecretStr`.
  ```
  - Ensure that your `requirements.txt` specifies the exact versions of the dependencies. This will prevent compatibility issues and ensure smooth operation.

For more in-depth information about the flow and process, consider reading [this blog post](https://www.thewildai.com/blog/build-an-ai-pdf-document-chatbot-in-python-using-langchain-openai-embeddings-and-astradb). The blog provides insights into the underlying technology and offers a detailed explanation of the project's architecture.

## Contributing

We welcome contributions from the community! Whether you're looking to fix a bug, add a new feature, or improve the documentation, your efforts are appreciated. Please adhere to our code of conduct and review the contribution guidelines before submitting a pull request. Join us in enhancing this project and making it more robust and versatile.

## License

This project is licensed under the Apache 2.0 License. This license allows for permissive use, modification, and distribution of the project. For more details, please refer to the [LICENSE](LICENSE) file included in the repository.

## Conclusion

Thank you for choosing to explore the PDF Document Chat project. We hope this guide has provided you with the necessary information to set up and run your application successfully. Enjoy the seamless experience of interacting with your PDFs using AI, and feel free to reach out with any questions or feedback. Happy coding!