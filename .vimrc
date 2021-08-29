call plug#begin('~/.vim/plugged')

" Nerdtree plugin
Plug 'scrooloose/nerdtree'
Plug 'xuyuanp/nerdtree-git-plugin'

" Nerdcommenter plugin
Plug 'scrooloose/nerdcommenter'

" ALE lint plugin
Plug 'w0rp/ale'

" Vim-Airline plugin
Plug 'vim-airline/vim-airline'

" Vim-Airline theme plugin
Plug 'vim-airline/vim-airline-themes'

" Vim-fugitive git plugin
Plug 'tpope/vim-fugitive'

" Show git diff in gutter
Plug 'airblade/vim-gitgutter'

" fzf
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'

" Solarized color scheme
Plug 'altercation/vim-colors-solarized'

" Onedark color scheme
Plug 'joshdick/onedark.vim'

" Auto ctags update on file change
Plug 'craigemery/vim-autotag'

Plug 'francoiscabrol/ranger.vim'
Plug 'rbgrouleff/bclose.vim'


Plug 'majutsushi/tagbar'
Plug 'will133/vim-dirdiff'
Plug 'joe-skb7/cscope-maps'
Plug 'chun-yang/auto-pairs'
Plug 'mileszs/ack.vim'

call plug#end()

filetype plugin on

" nerdtree short cut to toggle open/close
nnoremap <silent> <expr> <Leader>nt g:NERDTree.IsOpen() ? "\:NERDTreeClose<CR>" : bufexists(expand('%')) ? "\:NERDTreeFind<CR>" : "\:NERDTree<CR>"

" Airline settings
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'
let g:airline#extensions#ale#enabled = 1
let g:airline#extensions#ycm#enabled = 1
let g:airline#extensions#ycm#error_symbol = 'E:'
let g:airline#extensions#ycm#warning_symbol = 'W:'
let g:airline_powerline_fonts = 1

" fzf settings
let g:fzf_tags_command = 'ctags -R'
let g:fzf_layout = { 'window': 'enew' }

let g:NERDSpaceDelims = 1
let g:NERDTrimTrailingWhitespace = 1
let g:NERDTreeMinimalUI=1

" Color Schemes
let g:solarized_termcolors = 256
set background=light
silent! colorscheme solarized
silent! call togglebg#map("<F5>")
" silent! colorscheme onedark

" Open file from last location
if has("autocmd")
  autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif

" add yaml stuffs
autocmd! BufNewFile,BufReadPost *.{yaml,yml} set filetype=yaml
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

set encoding=utf-8
set switchbuf=usetab
set tabline=[%t]
set cursorline
set number
set incsearch
set ignorecase smartcase
set tabstop=4
set shiftwidth=4
set expandtab smarttab

"set mouse=a
"set ttymouse=sgr

set mouse=a

" The NERD tree settings
nmap <F3> :NERDTreeFocus<CR>

" Tagbar settings
nmap <F8> :TagbarToggle<CR>

" Fix Not Working Backspace in Vi/Vim Mac
set backspace=indent,eol,start
