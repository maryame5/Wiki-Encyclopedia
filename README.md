Wiki Encyclopedia

Project Overview

This project implements a wiki encyclopedia using Django, fulfilling the following requirements:

Features

Entry Page

Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, renders a page displaying the entry’s content.

If the entry exists, the page shows its content, with the title displayed in the page header.

If the entry does not exist, an error page is shown to inform the user.

Index Page

The index page lists all encyclopedia entries.

Users can click on any entry name to navigate directly to its page.

Search

A search box in the sidebar allows users to search for encyclopedia entries.

If the query matches an entry name, the user is redirected to that entry’s page.

If no exact match is found, a search results page displays all entries that contain the query as a substring.

Clicking any entry name in the results takes the user to the corresponding page.

New Page

Clicking "Create New Page" in the sidebar takes the user to a page for creating a new entry.

Users can enter a title and Markdown content for the new entry.

If the title already exists, an error message is displayed.

If the title is unique, the entry is saved, and the user is redirected to the new entry’s page.

Edit Page

Each entry page includes an option to edit the entry.

The editing page pre-populates a textarea with the current Markdown content of the entry.

Users can save changes, which updates the entry and redirects back to the entry’s page.

Random Page

Clicking "Random Page" in the sidebar takes the user to a randomly selected encyclopedia entry.

Markdown to HTML Conversion

Entry content is stored in Markdown format and converted to HTML before rendering.

The python-markdown2 package is used for this conversion. Install it via pip install markdown2.

Advanced users can implement custom Markdown parsing using regular expressions.
