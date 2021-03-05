function v
	if test (count $argv) -ne 1
nvim $PWD +':cd $PWD'
else if test -d $argv[1]
nvim $argv +':cd ' + $argv
else if test -f $argv[1]
nvim $argv +':cd %:h'
end
end
