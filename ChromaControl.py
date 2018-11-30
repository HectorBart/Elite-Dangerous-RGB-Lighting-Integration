from ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid

KeyboardGrid = ChromaGrid("Keyboard")

def whiteBright(app):

    # chroma white
    app.Keyboard.setStatic(Colors.WHITE)

def whiteDim(app):

    # chroma white
    app.Keyboard.setStatic(Colors.WHITE)

def orange(app):

    # chroma
    global KeyboardGrid
    KeyboardGrid.set(hexcolor="#ff9900")
    app.Keyboard.setCustomGrid(KeyboardGrid)
    app.Keyboard.applyGrid()

def flashGreen(app):

    # chroma
    app.Keyboard.setStatic(Colors.GREEN)

    # default
    whiteDim(app)

def flashRed(app):

    # chroma
    app.Keyboard.setStatic(Colors.RED)
