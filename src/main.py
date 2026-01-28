from textnode import TextNode
from textnode import TextType


def main():
    textNode = TextNode("Hello, world!", TextType.PLAIN, "https://www.boot.dev")
    print(f"{textNode}")


if __name__ == "__main__":
    main()
