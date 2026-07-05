# Static Site Generator

A static site generator written in Python that parses Markdown into a custom HTML node tree before generating a complete static website.

Instead of relying on an existing Markdown library, this project implements the entire parsing pipeline from scratch, including inline and block-level Markdown parsing, HTML tree construction, recursive content generation, and GitHub Pages deployment.

Built as part of the **Boot.dev – Build a Static Site Generator** course.

---

## Demo

🌐 **GitHub Pages:** https://ha0ch.github.io/static_site_generator/

---

## Features

- Custom Markdown parser (built from scratch)
- Custom HTML node tree using `LeafNode` and `ParentNode`
- Block-level Markdown parsing
  - Headings
  - Paragraphs
  - Ordered lists
  - Unordered lists
  - Blockquotes
  - Code blocks
- Inline Markdown parsing
  - Bold
  - Italic
  - Inline code
  - Links
  - Images
- HTML templating
- Recursive Markdown content generation
- Recursive static asset copying
- Preserves directory structure
- GitHub Pages base path support

---

## Project Structure

```
.
├── content/         # Markdown content
├── docs/            # Generated static site (GitHub Pages)
├── src/             # Source code
├── static/          # Static assets (CSS, images, etc.)
├── template.html    # HTML template
├── build.sh         # Production build script
└── main.sh          # Local development script
```

---

## Technologies

- Python 3
- HTML
- Markdown
- Regular Expressions
- Object-Oriented Programming
- File I/O
- Git
- GitHub Pages

---

## How It Works

The generator follows these steps:

1. Recursively traverses the `content/` directory.
2. Parses Markdown into block and inline nodes.
3. Builds a custom HTML node tree.
4. Injects the generated HTML into a template.
5. Copies static assets.
6. Outputs the complete website to the `docs/` directory for GitHub Pages.

---

## Local Development

Generate the site using the default base path:

```bash
python3 src/main.py
```

Or use the helper script:

```bash
./main.sh
```

Then serve the generated site:

```bash
cd docs
python3 -m http.server 8888
```

Open:

```
http://localhost:8888
```

---

## Production Build

Generate the site with the GitHub Pages base path:

```bash
./build.sh
```

The generated website will be written to:

```
docs/
```

---

## What I Learned

This project gave me hands-on experience with:

- Recursive directory traversal
- Recursive file generation
- Object-oriented design
- Tree data structures
- Markdown parsing
- HTML generation
- Regular expressions
- File system manipulation
- Path handling with `os.path`
- Static site generation
- GitHub Pages deployment

---

## Future Improvements

- Nested Markdown lists
- Tables
- Footnotes
- Syntax highlighting for code blocks
- Live reload development server
- Incremental builds
- Additional Markdown extensions

---

## Acknowledgements

This project was built while completing the **Build a Static Site Generator** course on **Boot.dev**.