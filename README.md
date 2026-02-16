# Jupyter Notebook DevContainer Template

This repository is a GitHub template designed to provide a ready-to-use development environment for Jupyter Notebooks using Docker and VS Code Dev Containers. It simplifies the setup process by encapsulating the Jupyter environment, Python, and necessary tools within a container.

## Features

*   **Jupyter Notebook Environment**: Pre-configured Jupyter Data Science Notebook image.
*   **VS Code Integration**: Seamless development within VS Code using the Dev Containers extension.
*   **Makefile Utility**: Easy command to retrieve the Jupyter Notebook connection token.
*   **Reproducible Environment**: Consistent setup across different machines using Docker.

## Prerequisites

Before you begin, ensure you have the following installed:

1.  **Docker Desktop** (or Docker Engine):
    *   [Install Docker](https://docs.docker.com/get-docker/)
    *   **Windows Users**: It is highly recommended to use **WSL 2** (Windows Subsystem for Linux) backend for Docker. [Install WSL 2](https://docs.microsoft.com/en-us/windows/wsl/install).
2.  **Visual Studio Code**:
    *   [Install VS Code](https://code.visualstudio.com/)
3.  **Dev Containers Extension** for VS Code:
    *   [Install Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## How to Use This Template

### 1. Create a Repository from this Template

You can use this repository as a starting point for your own project without forking it.

1.  Click the **"Use this template"** button at the top of the repository page on GitHub.
2.  Select **"Create a new repository"**.
3.  Give your new repository a name and description.
4.  Click **"Create repository"**.

### 2. Clone Your Repository

Once you have created your own repository from this template, clone it to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### 3. Open in VS Code

Open the cloned folder in Visual Studio Code:

```bash
code .
```

### 4. Reopen in Container

When you open the folder in VS Code, you should see a notification in the bottom right corner suggesting to reopen the folder in a container.

1.  Click **"Reopen in Container"**.
2.  Alternatively, you can open the Command Palette (`Ctrl+Shift+P` or `F1`) and type `Dev Containers: Reopen in Container`.

VS Code will now build the container image (this may take a few minutes the first time) and set up the environment.

## Running Jupyter Notebook

Once the container is running and you are connected (you'll see "Dev Container: ..." in the bottom left corner), the Jupyter server should start automatically.

To access the Jupyter Notebook interface in your browser, you need the connection token.

1.  Open the integrated terminal in VS Code (`Ctrl+` `).
2.  Run the following command:

    ```bash
    make token
    ```
    
    Or simply:
    
    ```bash
    make
    ```

3.  The output will display the running Jupyter servers and a connection URL with the token, like this:

    ```
    --- Jupyter Notebook Server Info ---
    Currently running servers:
    http://c6b308b27dd8:8888/?token=...
     :: /home/jovyan

    --- Connection URL for Host ---
    http://127.0.0.1:8888/?token=...
    ```

4.  **Ctrl+Click** (or **Cmd+Click** on macOS) the link starting with `http://127.0.0.1:8888/?token=...` to open Jupyter Notebook in your default browser.

## Project Structure

*   `.devcontainer/`: Configuration files for the VS Code Dev Container.
*   `notebooks/`: Directory to store your Jupyter Notebooks (`.ipynb`). **This folder is mounted to the container, so your work is persisted.**
*   `docker-compose.yml`: Defines the services and configuration for the Docker container.
*   `Makefile`: Helper commands for the project.

## Data Persistence

Any file you create or modify inside the `/workspace/notebooks` directory within the container is automatically synced to the `notebooks/` folder on your host machine. This ensures your work is saved even if you rebuild or delete the container.

## Customization

You can customize the environment by:

*   Modifying `docker-compose.yml` to change the image or add services.
*   Updating `.devcontainer/devcontainer.json` to add VS Code extensions or settings.
*   Installing additional Python packages within the notebook or by adding a `requirements.txt` and updating the `postCreateCommand` in `devcontainer.json`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## Show Your Support

If you find this template helpful, please give it a ⭐️ on GitHub!

## Contact

Alex - alex@lexdrel.com

Project Link: [https://github.com/lexdrel/jupyter-template](https://github.com/lexdrel/jupyter-template)

