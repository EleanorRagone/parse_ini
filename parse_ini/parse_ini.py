class ParseINI(dict):
    def __init__(self, file):
        self.file = file
        self.__read()

    def __read(self):
        with open(self.file, 'r') as file:
            slovnik = self
            for line in file:
                if line.startswith("#") and not line.startswith(';') and line.strip() != "":
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
                    if not self:
                        slovnik['global'] = {}
                        slovnik = slovnik['global']
                    parts = line.split(":", 1)
                    slovnik[parts[0].strip()] = parts[1].strip()

    def items(self, section):
        try:
            return self[section]
        except KeyError:
            return []
