---
layout: post
title: "Less pain with LaTeX"
date: 2014-09-22 21:54:53 +0400
comments: true
categories: LaTeX
---

## Why to use LaTeX. Main alternatives

LaTeX is a document preparation system and document markup language ([Wikipedia](http://en.wikipedia.org/wiki/LaTeX)). 
It is widely used within math, physics, computer science, and other fields.
Almost every major conference and journal accepts scientific papers as LaTeX documents
(e.g. [IEEE](http://www.ieee.org/conferences_events/conferences/publishing/templates.html), [ACM](http://www.acm.org/publications/latex_style/), [IFAC](http://www.ifac-control.org/events/information-for-ifac-authors/latex-style-for-ifac-papers), [arXiv](http://arxiv.org/help/submit)).
Since it was invented many different tools were created to help to create documents using LaTeX.
However, using LaTeX is still hard.

1. Before creating any document, you need to install LaTeX distribution.
On Windows it is [MiKTeX](http://www.howtotex.com/howto/installing-latex-on-windows/)
and [TeX Live](http://en.wikipedia.org/wiki/TeX_Live) on Linux.
There are many packages in these distros, and it is not obvious which one to install.

2. Setup a text editor or IDE. 
Typing
\begin{equation}
\begin{aligned}
 & \\
\end{aligned}
\end{equation}
every time you need a mathematical equation is very noisy.
Your text editor should generate those thins typing al<tab>.
There are plenty of options.
Two most upvoted answers on stackoverflow.com about
text [editor for Latex]() are Emacs and Vim.
Both of them require steap learning curve, i.e. 
it is not straight forward hot to configure and start to use them.
Consider Vim editor. 
It is a great tool and it can be extremely effective for editing LaTeX documents.
However, it has following problems:

* vim is a linux tool, it is not common on Windows platform
* every Vim user has different configurations, key-bindings and plugins.
Editing document in Vim looks like magic for other person.
It is almost impossible to give keyboard to smb else to edit couple of lines.
* configuring vim on a fresh-install system takes some time and effort.

After about a year of working in vim, I moved to Sublime Text.
Great editor.
It has a very easy to use package installation system,
it doesn't have weired vi-like key bindings. Sublime text works
perfectly well on linux, windows and Mac.
Completion system, spell checker, latex plugins, inverse search capabilities,
easy to use build system.

3. Use tools for building documents (latexmk in linux, texify for linux).
They execute pdflatex/bibtex/... appropriate times,
convert eps images to pdf if needed, and compile your document very fast.
They support inverse/forward search (<ctrl>+mouse click in pdf opens an editor
in the right place).
If you have two monitors it is handy to use automatic compilation of the pdf after saving document.

## How it can be improved
There are online solutions ([papeeria](http://papeeria.com), [sharelatex](https://www.sharelatex.com/), [writelatex](https://www.writelatex.com/), e.t.c.).
Main problems with them: 

1. Internet connection is often not stable/slow.
1. Slow navigation between PDF and source (forward/inverse search).
1. Changes in pictures requires re-uploading.