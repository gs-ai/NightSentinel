from setuptools import setup, find_packages

setup(
    name="camoufox",
    version="0.4.11",  # Updated version to meet Scrapling's requirements
    description="Camoufox: Browser automation and obfuscation tools",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="pythonlib"),
    package_dir={"": "pythonlib"},
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)