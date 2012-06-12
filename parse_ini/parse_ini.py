class ParseINI(dict):
    def __init__(self, file, globals_dict=False):
        super(ParseINI, self).__init__(self)
        self.file = file
        self.globals_dict = globals_dict
        self.__read()

    def __read(self):
        with open(self.file, 'r') as file:
            slovnik = self
            for line in file:
                if line.startswith("#") or line.startswith(';') or not line.strip():
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
                        if section not in slovnik:
                            slovnik[section] = {}
                        slovnik = slovnik[section]
                else:
                    if not self and self.globals_dict:
                        slovnik['global'] = {}
                        slovnik = slovnik['global']
                    parts = line.split(":", 1)
                    slovnik[parts[0].strip()] = parts[1].strip()

    def items_from_section(self, section):
        try:
            return self[section]
        except KeyError:
            return []