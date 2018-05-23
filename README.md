# notes
Inspired, wholesale, by [Chris Albon's Data Science Notes page](https://github.com/chrisalbon/notes).

## Some Notes on My Build

1. I took the code Chris was using in `make.ipynb` and put it into `make.py` for easier job chaining.
2. I develop on Windows and can't run most of the code locally, lol.
    * So if you're a windows user who forked this, and runs on your computer, a blank `index.html` means your build does the same thing mine does.
3. Chris used a tool called Hugo to build the page, I just downloaded a binary directly to the `binaries` folder...
4. ... so I can build all of the code directly up in TravisCI.
5. I did a ton of rooting around in the `themes` folder to redirect/rename a lot of fields, as well as better match the aesthetic of [my blog's](https://napsterinblue.github.io) css.
6. The strtucture of the way the notes render are more or less hard-coded in `themes/berbera/layouts/index.html`, but I think I could automate a lot of that in Go if I knew Go whatsoever.
7. The navigation bar at the top is to look like it's connected to my blog. It's not. Source code for that is [here](https://github.com/NapsterInBlue/MoviesMetricsMusings).

That's about it. Cheers!
