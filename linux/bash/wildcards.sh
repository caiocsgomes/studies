# ? -> match one character
# * matches one, many or no character
# [a-b] matches a sequence
# [^a-b] does not match a sequence
# {var} matches specific (exactly) variables
# examples

ls *a
ls a* 
ls a?c
ls m[a-b]
ls m[tv]
ls w?{list}*
cp raas* dest