set number
set autoindent
set hlsearch
set incsearch
set laststatus=2
set encoding=utf-8
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab

" Folding - syntax, but not during insert mode
set foldmethod=syntax
autocmd InsertEnter * if !exists('w:last_fdm') | let w:last_fdm=&foldmethod | setlocal foldmethod=manual | endif
autocmd InsertLeave,WinLeave * if exists('w:last_fdm') | let &l:foldmethod=w:last_fdm | unlet w:last_fdm | endif

" Persistent undo
set undofile
set undodir=~/.vim/undo

set colorcolumn=100
highlight ColorColumn ctermbg=7 

colorscheme evening

syntax on

filetype plugin indent on

inoremap kj <Esc>
let mapleader = "\<Space>"

set runtimepath^=~/.vim/bundle/ctrlp.vim
execute pathogen#infect()
