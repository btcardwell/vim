set number
set hlsearch
set autoindent
set laststatus=2
set encoding=utf-8
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab

colorscheme evening

syntax on

filetype plugin indent on

inoremap kj <Esc>
let mapleader = "\<Space>"

set runtimepath^=~/.vim/bundle/ctrlp.vim
execute pathogen#infect()
