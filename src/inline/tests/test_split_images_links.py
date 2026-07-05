import unittest
from inline.textnode import TextNode, TextType
from inline.split_images_links import split_nodes_images, split_nodes_links

class TestSplitNodesImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_images_multiple_nodes(self):
        old_nodes = [
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT),
            TextNode("This is another text with an ![image3](https://i.imgur.com/zjjcJKZ1.png) and another ![image4](https://i.imgur.com/3elNhQu2.png)",
            TextType.TEXT,)
        ]

        new_nodes = split_nodes_images(old_nodes)

        self.assertListEqual(
            [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode("This is another text with an ", TextType.TEXT),
            TextNode("image3", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ1.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("image4", TextType.IMAGE,"https://i.imgur.com/3elNhQu2.png")
            ],
            new_nodes
        )
    
    def test_split_images_only_image(self):
        old_nodes = [
            TextNode(
                "![image](https://i.imgur.com/zjjcJKZ.png)",
                TextType.TEXT,
            )
        ]

        new_nodes = split_nodes_images(old_nodes)

        self.assertListEqual(
            [
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                )
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://google.com"),
            ],
            new_nodes,
        )


    def test_split_links_multiple_nodes(self):
        old_nodes = [
            TextNode(
                "This is text with a [link](https://example.com) and another [link2](https://google.com)",
                TextType.TEXT,
            ),
            TextNode(
                "This is another text with a [link3](https://github.com) and another [link4](https://youtube.com)",
                TextType.TEXT,
            ),
        ]

        new_nodes = split_nodes_links(old_nodes)

        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "https://google.com"),
                TextNode("This is another text with a ", TextType.TEXT),
                TextNode("link3", TextType.LINK, "https://github.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link4", TextType.LINK, "https://youtube.com"),
            ],
            new_nodes,
        )


        def test_split_links_only_link(self):
            old_nodes = [
                TextNode(
                    "[link](https://example.com)",
                    TextType.TEXT,
                )
            ]

            new_nodes = split_nodes_links(old_nodes)

            self.assertListEqual(
                [
                    TextNode("link", TextType.LINK, "https://example.com"),
                ],
                new_nodes,
            )

if __name__ == "__main__":
    unittest.main()