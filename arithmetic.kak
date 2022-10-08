declare-option -hidden \
	-docstring 'Path to arithmetic.py script.' \
	str arithmetic_py_source \
	%sh{ echo "${kak_source%%.kak}.py" }

define-command arithmetic %{
	prompt 'arithmetic ' -init 'x' \
	-on-change %{
		info -title 'preview' %sh{
			python3 "$kak_opt_arithmetic_py_source" '--preview' "$kak_text" "$kak_quoted_selections"
		}
	} \
	%{
		evaluate-commands -save-regs dquote %{
			evaluate-commands %sh{
				printf 'set-register dquote '
				python3 "$kak_opt_arithmetic_py_source" "$kak_text" "$kak_quoted_selections"
			}
			execute-keys R
		}
	}
}
