class DebugRecord:

    def __init__(self, userChoice, programInfo):
        self._userChoice = userChoice
        self._programInfo = programInfo

    def prettyPrint(self):
        print(f"Developer action: {self._userChoice}")
        print("Program info:\n")
        print(self._programInfo)