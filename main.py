import compile, output

class Main():
    def __init__(self):
        self.compile = compile.GetData()
        self.output = output.Output()


if __name__ == "__main__":
    # filename = "source.txt"

    with open("source.txt", "r", encoding="utf-8") as f:
        data = f.read()

    main = Main()
    users, content, time = main.compile.get(data)
    main.output.output(users, content, time)
