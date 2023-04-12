from skbuild import setup

setup(
    name="hello-pybind11",
    version="1.2.3",
    description="a minimal example package (with pybind11)",
    author="Pablo Hernandez-Cerdan",
    license="MIT",
    packages=["hello"],
    package_dir={"": "src"},
    cmake_install_dir="src/hello",
    python_requires=">=3.7",
)
# setup(
#     name="hello",
#     version="1.2.3",
#     description="a minimal example package (with pybind11)",
#     packages=["hello"],
#     # package_dir={"hello": "src/hello"},
#     package_dir={"": "src"},
#     #cmake_install_dir="src/hello", # final installation dir of so file# src/cpp
#     python_requires=">=3.7",
# )
