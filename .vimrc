call plug#begin('~/.vim/plugged')

" Install YouCompleteMe
Plug 'ycm-core/YouCompleteMe'


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

" gruvbox color scheme
Plug 'morhetz/gruvbox'

" Auto ctags update on file change
Plug 'craigemery/vim-autotag'

Plug 'majutsushi/tagbar'
Plug 'will133/vim-dirdiff'
Plug 'joe-skb7/cscope-maps'
Plug 'mileszs/ack.vim'
Plug 'ekalinin/Dockerfile.vim'
Plug 'andrewradev/linediff.vim'
Plug 'mfukar/robotframework-vim'
Plug 'ojroques/vim-oscyank', {'branch': 'main'}
Plug 'tpope/vim-surround'
Plug 'qpkorr/vim-bufkill'
Plug 'vim-scripts/bash-support.vim'
Plug 'tpope/vim-sleuth'

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

" YCM settings
let g:ycm_log_level = 'debug'
let g:ycm_keep_logfiles = 1
let g:ycm_autoclose_preview_window_after_insertion = 1
let g:ycm_autoclose_preview_window_after_completion = 1
let g:ycm_global_ycm_extra_conf = '~/.vim/.ycm_extra_conf.py'
let g:ycm_filetype_blacklist = { 'nerdtree': 1 }
let g:ycm_semantic_triggers =  {
  \   'c' : ['->', '.','re![_a-zA-z0-9]'],
  \   'objc' : ['->', '.', 're!\[[_a-zA-Z]+\w*\s', 're!^\s*[^\W\d]\w*\s',
  \             're!\[.*\]\s'],
  \   'ocaml' : ['.', '#'],
  \   'cpp,objcpp' : ['->', '.', '::','re![_a-zA-Z0-9]'],
  \   'perl' : ['->'],
  \   'php' : ['->', '::'],
  \   'cs,java,javascript,typescript,d,python,perl6,scala,vb,elixir,go' : ['.'],
  \   'ruby' : ['.', '::'],
  \   'lua' : ['.', ':'],
  \   'erlang' : [':'],
  \ }
let g:ycm_auto_hover=''

"lombok work around for youcompleteme
let $JAVA_TOOL_OPTIONS = '-javaagent:/usr/local/share/vim/lombok-1.18.8.jar'
" let $JAVA_TOOL_OPTIONS = '-javaagent:/usr/local/share/vim/lombok-1.18.8.jar -Xbootclasspath/a:/usr/local/share/vim/lombok-1.18.8.jar'

" Color Schemes
set background=dark
let g:gruvbox_contrast_dark = 'hard'
let g:gruvbox_invert_selection = 0
silent! colorscheme gruvbox
nnoremap <silent> [oh :call gruvbox#hls_show()<CR>
nnoremap <silent> ]oh :call gruvbox#hls_hide()<CR>
nnoremap <silent> coh :call gruvbox#hls_toggle()<CR>

nnoremap * :let @/ = ""<CR>:call gruvbox#hls_show()<CR>*
nnoremap / :let @/ = ""<CR>:call gruvbox#hls_show()<CR>/
nnoremap ? :let @/ = ""<CR>:call gruvbox#hls_show()<CR>?

" Open file from last location
if has("autocmd")
  autocmd BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif

" add yaml stuffs
autocmd! BufNewFile,BufReadPost *.{yaml,yml} set filetype=yaml
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

" add asm stuffs
autocmd BufNew,BufRead *.asm set ft=nasm

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

" autotag settings
let g:autotagStartMethod='fork'

" The NERD tree settings
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-f> :NERDTreeFind<CR>

" Tagbar settings
nmap <F8> :TagbarToggle<CR>

" vim-oscyank settings
nmap <leader>y <Plug>OSCYankOperator
nmap <leader>yc <leader>c_
vmap <leader>y <Plug>OSCYankVisual

" Fix Not Working Backspace in Vi/Vim Mac
set backspace=indent,eol,start

" Use ripgrep for searching ⚡️
" Options include:
" --vimgrep -> Needed to parse the rg response properly for ack.vim
" --type-not sql -> Avoid huge sql file dumps as it slows down the search
" --smart-case -> Search case insensitive if all lowercase pattern, Search case sensitively otherwise
let g:ackprg = 'rg --vimgrep --type-not sql --smart-case'

" Auto close the Quickfix list after pressing '<enter>' on a list item
let g:ack_autoclose = 1

" Any empty ack search will search for the work the cursor is on
let g:ack_use_cword_for_empty_search = 1

set clipboard=unnamed
cnoremap %% <C-R>=expand('%:h').'/'<CR>

" Visualize Tab
noremap <Leader><Tab><Tab> :set invlist<CR>
