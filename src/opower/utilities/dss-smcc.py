"""Southern Maryland Electric Cooperative (DSS-SMCC/SMECO)."""

from .aepbase import AEPBase
from .base import UtilityBase


class SMECO(AEPBase, UtilityBase):
    """Southern Maryland Electric Cooperative (DSS-SMCC)."""

    @staticmethod
    def name() -> str:
        """Distinct recognizable name of the utility."""
        return "Southern Maryland Electric Cooperative (DSS-SMCC)"

    @staticmethod
    def timezone() -> str:
        """Return the timezone."""
        return "America/New_York"

    @staticmethod
    def hostname() -> str:
        """Return the hostname for login."""
        return "dss-smcc.opower.com"
