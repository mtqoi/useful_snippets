So I have it all in one place, here are the things I like to install to make my Mac OS terminal experience nicer.

At a high level my setup is
- iTerm2
- `zsh` shell
- `oh-my-zsh` for customisations and plugins
- Monokai-like colour theme
- Bunch of extra command line tools and prettifiers 

## Install these first

[iTerm2](https://www.google.com/search?client=safari&rls=en&q=iterm2&ie=UTF-8&oe=UTF-8) - this will be the main terminal program. Check that it defaults to `zsh`. 

[Homebrew](https://brew.sh) MacOS package manager

`git` should be installed already but just make sure that it is 

## Make `zsh` look cool

[Install](https://ohmyz.sh) `oh-my-zsh` . It will give us the framework to make our `zsh` look nice, plus it has lots of plugins that can add nice functionality

Now install an `oh-my-zsh` theme. Here is a [big list](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes) of preinstalled themes that you can activate by modifying your `~/.zshrc` file. You may need to create this file if it does not already exist.

I like the [powerlevel10k](https://github.com/romkatv/powerlevel10k) theme. When you install it it'll run you through configuration options and then modify your `~/.zshrc` directly.

Note that you can 'refresh' your `zsh` by doing `source ~/.zshrc`. This is useful if you make changes to your `~/.zshrc` file and want to see them reflected in your current terminal window without having to restart. You can also use your `~/.zshrc` to set environment variables which may be useful.

## Some cool `oh-my-zsh` plugins that I like

Here is a [large list](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins) of plugins that are available.

The `git` plugin should be installed automatically already and it's pretty useful. It gives some aliases for common cli `git` commands, which is nice.

I also like:
- [`zsh-autosuggestions`](https://github.com/zsh-users/zsh-autosuggestions/tree/master)
- [`zsh-syntax-highlighting`](https://github.com/zsh-users/zsh-syntax-highlighting)
- [`zsh-completions`](https://github.com/zsh-users/zsh-completions)

## Some more plugins

I like:
- [`scm_breeze`](https://github.com/scmbreeze/scm_breeze)
- [`colorls`](https://github.com/athityakumar/colorls) 

For colorls I have added the alias `alias ls='colorls'` to my `~/.zshrc`. 

In terms of aliases I also like

```
alias gl="git log --all --decorate --oneline --graph"
alias gt="git ls-tree -r --name-only HEAD | tree --fromfile"
```

## Nice tools

I like:
- `tldr`
- `btop`
- `bat`

There are probably more that I use but I can't remember them just now.

These can usually be installed with `brew install bat`, or similar. 

You also probably want to make sure that you can open files in your favourite text editor from terminal. I've been playing around with neovim lately which is easy to get working, but you might want to install the `sublime` `oh-my-zsh` plugin for example which I think just adds some nice aliases.

## Some more iTerm2 changes 
Lots of [iTerm2 themes](https://iterm2colorschemes.com) . You just need to download the file and then point iTerm2 to it. There are instructions in the link. I am currently using DimmedMonokai.

Last thing that I always forget: Natural Text Editing. This lets you use the normal Mac commands (e.g. ⌥ + arrow, etc.) to move around your terminal. Go to iTerm2 > Settings > Profiles > Keys > Key Mappings > Presets and then select 'Natural Text Editing' which is just a builtin keymap. You can change individual mappings to whatever you like.

## Shoutout
Thanks to [High Growth Engineer](https://read.highgrowthengineer.com/p/how-i-setup-my-terminal-for-max-productivity?utm_source=post-email-title&publication_id=1504485&post_id=143547135&utm_campaign=email-post-title&isFreemail=true&r=2m3dh&triedRedirect=true&utm_medium=email) substack for introducing me to `zsh-completions` and `scm_breeze`
