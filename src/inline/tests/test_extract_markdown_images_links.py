from inline.extract_markdown_images_links import extract_markdown_images, extract_markdown_links
import unittest

class TestExtractMarkdownImagesLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image1](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/abcd123.png)"
        )
        self.assertListEqual(
            [
                ("image1", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/abcd123.png"),
            ],
            matches,
        )
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to Youtube](https://www.youtube.com/)"
        )
        self.assertListEqual([("to Youtube", "https://www.youtube.com/")], matches)
    
    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to Youtube](https://www.youtube.com/) and another [to Google](https://www.google.com/)"
        )
        self.assertListEqual(
            [
                ("to Youtube", "https://www.youtube.com/"),
                ("to Google", "https://www.google.com/"),
            ],
            matches,
        )

if __name__ == "__main__":
    unittest.main()