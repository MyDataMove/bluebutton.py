OIDS = {
    '2.16.840.1.113883.4.6': 'NPI',
    '2.16.840.1.113883.6.12': 'CPT',
    '2.16.840.1.113883.6.96': 'SNOMED-CT'
}

CODING_SYSTEMS = {
    n: o
    for o,n in OIDS.items()
}

def get_name(oid):
    for n,o in CODING_SYSTEMS.items():
        if o == oid:
            return n
    return oid
