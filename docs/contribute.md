# Contribute

The notes are prepared using markdown.

## Markdown editor

There are quite a few markdown editors out there. Here are three options:

- [Typora](https://typora.io/)
- [Marktext](https://github.com/marktext/marktext)
- [Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)

## BSc-GitHub

Log in to the [BSc-GitHub](https://github.com/bsc-iitm) page with your online degree account.

## Clone

Clone the MLF [repository](https://github.com/bsc-iitm/machine-learning-foundations). If you are on a Linux system or are using [bash for Windows](https://www.laptopmag.com/articles/use-bash-shell-windows-10), you can run the following command:

```
git clone https://github.com/bsc-iitm/machine-learning-foundations.git
```

## Edit a chapter

All the chapters of the notes are arranged in the form of markdown files. There is one markdown file for each concept. These files are organized in a folder called `docs`. You can open any one chapter and start editing it or you can add a new chapter. Markdown is quite easy to learn. Typora has one of the best [tutorials](https://support.typora.io/Markdown-Reference/) for learning markdown.

## Navigation

In case you are adding a new chapter, you have to add a navigation link in the file `mkdocs.yml`. Refer to this file and look at the section `nav` to get an idea of how navigation works.

## Mkdocs

If you want to see how the notes looks like, you need to install a tool called `mkdocs`. You can install it as follows:

```
pip install mkdocs-material
```

To see how the site looks, you would have to serve it:

```
mkdocs serve
```

When you serve a page, you can access it via local host:

```
http://127.0.0.1:8000/
```











