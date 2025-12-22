class Version:
    """Basic class to represent a version.
    """
    def __init__(self, major: int = 1, minor: int = 0, patch: int = 0):
        self._major = major
        self._minor = minor
        self._patch = patch
    
    @property
    def major(self): return self._major
    @property
    def minor(self): return self._minor
    @property
    def patch(self): return self._patch

    def __repr__(self) -> str:
        return f'Version({self._major}, {self._minor}, {self._patch})'

    def __str__(self) -> str:
        return f'{self._major}.{self._minor}.{self._patch}'