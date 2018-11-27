" Set up Vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'kien/ctrlp.vim'
Plugin 'easymotion/vim-easymotion'
Plugin 'vim-syntastic/syntastic'
Plugin 'tpope/vim-surround'
call vundle#end()
filetype plugin indent on

" Basics
set t_Co=256
colors zenburn
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
set ignorecase
set smartcase
set fileformat=unix
let python_highlight_all=1
set splitright
set splitbelow

" highlight BadWhitespace ctermbg=darkred guibg=darkred
" match BadWhitespace /\s\+$/

inoremap kj <Esc>
let mapleader = "\<Space>"

" Persistent undo
set undofile
set undodir=~/.vim/undo

"python with virtualenv support
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
EOF

let g:syntastic_mode_map = { 'mode': 'passive', 'active_filetypes': [],'passive_filetypes': [] }

" Folding - syntax, but not during insert mode - Try SimpylFold instead
" set foldmethod=syntax
" autocmd InsertEnter * if !exists('w:last_fdm') | let w:last_fdm=&foldmethod | setlocal foldmethod=manual | endif
" autocmd InsertLeave,WinLeave * if exists('w:last_fdm') | let &l:foldmethod=w:last_fdm | unlet w:last_fdm | endif

