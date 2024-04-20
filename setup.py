import  setuptools

with open("README.md", "r", encoding="utf-8")as f:
    long_description = f.read()


_version_ = "0.0.0"

REPO_NAME = "MLOPS PROJECT"
AUTHOR_USER_NAME = "ranju"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "ranjania474@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Asmall python package for ml app",
    Long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker": f"https://githup.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
package_dir={"": "src"},
packages=setuptools.find_packages(where="src")

)