macroScript LaborTools
category:"Custom Tools"
buttontext:"labor tools"
(
    dir = getThisScriptFilename()
    print dir
    python.ExecuteFile(dir + "\..\labor_tools.py")
)