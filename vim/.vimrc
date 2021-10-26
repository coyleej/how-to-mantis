""" Example vimrc file
"
" Use double quotes to comment out text
"
" Negate things by prepending no
" Toggle boolean by appending !
" (Settings without equal signs are boolean)
"
" Run command line stuff by prepending !
" E.g., to make directory test/ within vim, you would type
":!mkdir test
"

""" LINE NUMBERING
" nu is number, rnu is relativenumber
" Setting both gives a hybrid numbering
":set nu
":set rnu
:set nu rnu

""" FOLDING
augroup vimrc
  " Set indent as the fold method before file is loaded
  au BufReadPre * setlocal foldmethod=indent
  " You can still use manual folds, even when foldmethod=indent
  au BufWinEnter * if &fdm == 'indent' | setlocal foldmethod=manual | endif
augroup END
":set foldmethod=indent
:set foldminlines=1
:set foldnestmax=5
:set foldlevel=3
:set nofoldenable

""" MAPPINGS
:nmap s <C-w>

""" OTHER USEFUL THINGS
" Highlist all search result matches
:set hlsearch

" Highlist all search result matches
" Remove highlighting post search with :nohl
:set hlsearch

" Specify multiple columns by using a comma-separated list
" To remove, use :set cc=
:set cc=79

" Show existing tab with 4 spaces width
set tabstop=4
" When indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab

" Automatically adjust behavior by filetype
filetype plugin indent on

""" BUFFER OPTIONS
"Make cursor jump to open window instead of duplicating
:set switchbuf=useopen

""" ADDONS
