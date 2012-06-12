class ParseINI(dict):
    def __init__(self, file, upper=True, globals_dict=False):
        super(ParseINI, self).__init__(self)
        self.file = file
        self.globals_dict = globals_dict
        self.upper = upper
        self.__read()

    def __read(self):
        with open(self.file, 'r') as file:
            slovnik = self
            for line in file:
                if line.strip().startswith("#") or line.strip().startswith(';') or not line.strip():
                    continue
                if ":" not in line and "=" not in line:
                    print "Skipping line due to no colon or equals: %s" % (line,)
                    continue
                line = line.replace('=', ':')
                line = line.replace(';', '#')
                index = line.find('#')
                line = line[:index]
                line = line.strip()
                if line.startswith("["):
                    sections = line[1:-1].split('.')
                    slovnik = self
                    for section in sections:
                        if self.upper:
                            section = section.upper()
                        if section not in slovnik:
                            slovnik[section] = {}
                        slovnik = slovnik[section]
                else:
                    if not self and self.globals_dict:
                        slovnik['global'] = {}
                        slovnik = slovnik['global']
                    parts = line.split(":", 1)
                    key = parts[0].strip()
                    value = parts[1].strip()
                    if self.upper:
                        key = key.upper()
                    if value.lower() == "true":
                        value = True
                    elif value.lower() == "false":
                        value = False
                    slovnik[key.upper()] = value

    def items_from_section(self, section):
        try:
            return self[section]
        except KeyError:
            return []
