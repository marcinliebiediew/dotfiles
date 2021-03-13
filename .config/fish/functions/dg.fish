# Defined in - @ line 1
function dg --wraps='/usr/bin/git --git-dir=$HOME/.digitalgarden/ --work-tree=$HOME/org/roam' --description 'alias dg=/usr/bin/git --git-dir=$HOME/.digitalgarden/ --work-tree=$HOME/org/roam'
  /usr/bin/git --git-dir=$HOME/.digitalgarden/ --work-tree=$HOME/org/roam $argv;
end
