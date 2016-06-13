set number
set hlsearch
set autoindent
set laststatus=2
set encoding=utf-8

colorscheme evening

syntax on

filetype plugin indent on

inoremap kj <Esc>
let mapleader = "\<Space>"

set runtimepath^=~/.vim/bundle/ctrlp.vim
execute pathogen#infect()
