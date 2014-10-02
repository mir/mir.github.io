---
layout: post
title: "Less pain with LaTeX"
date: 2014-09-22 21:54:53 +0400
comments: true
categories: LaTeX
---

LaTeX is a document preparation system and document markup language ([Wikipedia](http://en.wikipedia.org/wiki/LaTeX)). 
It is widely used within math, physics, computer science, and other fields.
Almost every major conference and journal accepts scientific papers as LaTeX documents
(e.g. [IEEE](http://www.ieee.org/conferences_events/conferences/publishing/templates.html), [ACM](http://www.acm.org/publications/latex_style/), [IFAC](http://www.ifac-control.org/events/information-for-ifac-authors/latex-style-for-ifac-papers), [arXiv](http://arxiv.org/help/submit)).
Since it was invented many different tools were created to help to create documents using LaTeX.
However, using LaTeX is still hard.

Before creating any document, you need to install LaTeX distribution.
On Windows it is [MiKTeX](http://www.howtotex.com/howto/installing-latex-on-windows/)
and [TeX Live](http://en.wikipedia.org/wiki/TeX_Live) on Linux.
There are many packages in these distros, and it is not obvious which one to install.

Setup a text editor or IDE. 
Typing
{% highlight ruby %}
\begin{equation}
	\begin{aligned}
 		& \\ 		
	\end{aligned}
\end{equation}
{% endhighlight %}

and putting cursor between & and \ \
every time you need a mathematical equation is very annoying.
Your text editor should generate those thins typing a couple of letters then hitting tab (e.g. al + tab).
There are plenty of options.
Two most upvoted answers on stackoverflow.com about
text [editor for Latex](http://tex.stackexchange.com/questions/339/latex-editors-ides) are [Emacs](http://en.wikipedia.org/wiki/Emacs) and [Vim](http://en.wikipedia.org/wiki/Vim_(text_editor)).
Both of them require steap learning curve, i.e. 
it is not straight forward hot to configure and start to use them.
Consider Vim editor. 
It is a great tool and it can be extremely effective for editing LaTeX documents.
However, it has following problems. First, vim is a linux tool, it is not common on Windows platform. Second, every Vim user has different configurations, key-bindings and plugins.
Editing document in Vim looks like magic for other person.
It is almost impossible to give keyboard to smb else to edit couple of lines. 
Configuring vim on a fresh-install system takes some time and effort.

After about a year of working in vim, I moved to [Sublime Text](http://www.sublimetext.com/).
Great editor.
It has a very easy to use package installation system,
it doesn't have weired vi-like key bindings. Sublime text works
perfectly well on linux, windows and Mac.
Completion system, spell checker, latex plugins, inverse search capabilities,
easy to use build system.

Use appropriate tools for building documents (latexmk in linux, texify for linux).
They execute pdflatex/bibtex/... appropriate times,
convert eps images to pdf if needed, and compile your document very fast.
They support inverse/forward search (<ctrl>+mouse click in pdf opens an editor
in the right place).
If you have two monitors it is handy to use automatic compilation of the pdf after saving document.

Here are some hints on how to properly setup Latex environment:

1. Install LaTeX distribution (Texlive on Linux, MikTex on Windows, Mactex on Mac)
1. Install build tools (latexmk or texify)
1. Install Sublime Text
1. Install package control for sublime text (see [official docs](https://sublime.wbond.net/installation))
1. Install [Latextools](https://github.com/SublimeText/LaTeXTools) package (hit ctrl-p, then choose Install package, then choose Latextools).
1. Configure inverse search (on Ubuntu you should probably create symlink /usr/bin/subl or /usr/bin/sublime-text or /usr/bin/sublime). Inverse search enables to use ctrl+mouseclick on pdf which will open Sublime text and position mouse over on appropriate line.
1. Configure your favorite snippets (e.g. al+tab) in LaTeX.sublime-completions file (preferences->browse packages->User). My favorite al comletion looks like this:
{% highlight ruby %}
{ "trigger": "al", "contents": "\\begin{equation}\n\\begin{aligned}\n& $0\n\\end{aligned}\n\\end{equation}\n"},
{% endhighlight %}

A good practice is to store sublime user settings in Dropbox (Copy User folder to dropbox and create a symlink to it from /home/user/.config/sublime-text3/).

## How it can be improved
There are online solutions ([papeeria](http://papeeria.com), [sharelatex](https://www.sharelatex.com/), [writelatex](https://www.writelatex.com/), e.t.c.).
Main problems with them: 

1. Internet connection is often not stable/slow.
1. Slow navigation between PDF and source (forward/inverse search).
1. Changes in pictures requires re-uploading.

Hope those things will be solved soon and compiling with LaTeX will be easy as writing an email in Gmail.