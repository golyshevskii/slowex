import logging

logger = logging.getLogger(__name__)


def import_gsheets_leads(from_dtt: str, to_dtt: str):
    """
    Imports leads from Google Sheets

    Params:
        from_dtt: Timestamp from which leads should be imported. Format "YYYY-MM-DD HH:MM:SS"
        to_dtt: Timestamp until which leads should be imported. Format "YYYY-MM-DD HH:MM:SS"
    """
    logger.info(f"Importing leads from {from_dtt} to {to_dtt}")
    pass
