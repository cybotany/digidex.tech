NTAG213 = "213"
NTAG215 = "215"
NTAG216 = "216"

NTAG_IC_CHOICES = (
    (NTAG213, "NTAG 213"),
    (NTAG215, "NTAG 215"),
    (NTAG216, "NTAG 216"),
)

NTAG_EEPROM_SIZES = {
    NTAG213: 180,
    NTAG215: 540,
    NTAG216: 924,
}

NTAG_PERMISSIONS = [
    'change_nfctag',
]
