import importlib.metadata
packages = [
    "langchain",
    "python_dotenv",
    "langchain_core",
]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except:
        print(f"{pkg} (not installed)")