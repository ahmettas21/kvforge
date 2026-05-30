from setuptools import setup, find_packages

setup(
    name="kvforge",
    version="0.1.0",
    description="Seed-based KV Cache Compression for Transformers",
    author="Ahmet TAS",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "datasets>=2.14.0",
        "psutil>=5.8.0",
    ],
    python_requires=">=3.10",
)
