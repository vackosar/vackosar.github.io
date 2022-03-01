
# HN 1

Conda is a great tool.
But it forks the ecosystem, twice:

First, Conda packages have to be maintained separately from PyPI packages.

Second, the "default" repo is maintained by Anaconda, but the community maintained Conda Forge repo is also separate, and officially the packages in one are not compatible with the packages in the other. (In practice they usually play nice).

Having three incompatible package repos is not ideal.


# HN 2

The real problem (which is solved by conda) is that pypi doesn't solve dealing with non-python packages well (say, compile scipy and make all related native packages communicate well). This is a huge issue for people dealing with scientific packages (and the main pain point which pypi being just python-focused on installing on site-packages doesn't solve well enough IMHO).
Also, while it was initially done by a private company, I'd say it's definitely a community effort right now (it's also the reason I tend to use https://conda-forge.org/, which is community driven and not anaconda).

As for dealing with pypi, it does integrate well enough for me (given that you can just pip install packages on the python for which conda is managing the env), but yes, the other way around isn't true (conda solves a bigger problem than pypi up to the point that it's possible to even have non-python tools available -- one real use case example I have here is having innosetup binaries as a tool in the PATH in some conda env for doing builds).

Note: I don't have any affiliation with any of that, these are just my preferences for managing python envs (when I'm developing pydevd, which is the debugger engine used in pydev/pycharm/vscode, many times I need to reproduce some weird env and before using conda that was pretty annoying).

# HN 3
It provides the needed isolation, you can get lots of packages without having to compile from conda-forge and it still works with pip for the odd cases where a given package is not directly available (as a bonus, it works for other native toolchains, not only Python, which is a huge plus for me).

