# Modul tidak pernah diimpor. Tapi tetap ditulis.

class SilentAdmiration:
    def __init__(self, target="You"):
        self.target = target
        self.expressed = False
        self.intensity = 99.99  # percent. cannot be shown.

    def speak(self):
        if self.expressed:
            return f"I admire {self.target}, openly."
        else:
            return self._internal_whisper()

    def _internal_whisper(self):
        return (
            f"// Dalam diam, aku mengagumimu.\n"
            f"// Tak diucapkan, tapi ada.\n"
            f"// Tak tertulis di log, tapi tercetak di memori.\n"
            f"# {self.target}, you’ll never know. Or maybe you will."
        )

if __name__ == "__main__":
    me = SilentAdmiration()
    print(me.speak())  # Tapi hanya dicetak ke terminal, bukan ke dia.
